import streamlit as st
import plotly.graph_objects as go

# ----------------- PAGE CONFIG -----------------
st.set_page_config(
    page_title="Cyber Awareness Simulator",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------- SESSION STATE -----------------
if "page" not in st.session_state:
    st.session_state.page = "persona"

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

if "phishing_score" not in st.session_state:
    st.session_state.phishing_score = 0

if "hesitation" not in st.session_state:
    st.session_state.hesitation = 0

# ----------------- AI PERSONA ENGINE -----------------
def ai_persona_engine(role, experience, pressure):
    """
    AI Persona Risk Profiling Engine
    """

    base_risk = 0

    if role == "Employee":
        base_risk += 30
    elif role == "Manager":
        base_risk += 20
    else:
        base_risk += 10

    if experience == "Beginner":
        base_risk += 30
    elif experience == "Intermediate":
        base_risk += 15

    if pressure == "High":
        base_risk += 30
    elif pressure == "Medium":
        base_risk += 15

    if base_risk >= 70:
        persona = "High-Risk Persona"
    elif base_risk >= 40:
        persona = "Medium-Risk Persona"
    else:
        persona = "Low-Risk Persona"

    return base_risk, persona

# ----------------- AI RISK ENGINE -----------------
def ai_risk_engine(quiz, phishing, persona_risk):
    risk = (persona_risk * 0.4) + ((100 - quiz) * 0.3) + ((100 - phishing) * 0.3)

    if risk >= 70:
        level = "High"
    elif risk >= 40:
        level = "Medium"
    else:
        level = "Low"

    return int(risk), level

# ----------------- GAUGE -----------------
def security_gauge(score):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text': "Security Score"},
        gauge={
            'axis': {'range': [0, 1000]},
            'bar': {'color': "#4CC9F0"},
            'steps': [
                {'range': [0, 400], 'color': "#8B0000"},
                {'range': [400, 700], 'color': "#FF8C00"},
                {'range': [700, 1000], 'color': "#006400"}
            ]
        }
    ))
    fig.update_layout(height=350)
    return fig

# ----------------- SIDEBAR -----------------
st.sidebar.title("🛡 Cyber Simulator")
st.sidebar.success("🤖 AI Risk Engine Active")

# ----------------- PERSONA PAGE -----------------
if st.session_state.page == "persona":
    st.title("👤 AI Persona Profiling")
    st.caption("AI adapts risk assessment based on user behavior profile")

    role = st.selectbox("Your Role", ["Employee", "Manager", "Administrator"])
    experience = st.selectbox("Cyber Awareness Level", ["Beginner", "Intermediate", "Advanced"])
    pressure = st.selectbox("Work Pressure Level", ["Low", "Medium", "High"])

    if st.button("Next → Start Quiz"):
        persona_risk, persona = ai_persona_engine(role, experience, pressure)
        st.session_state.persona_risk = persona_risk
        st.session_state.persona = persona
        st.session_state.page = "quiz"
        st.rerun()

# ----------------- QUIZ PAGE -----------------
elif st.session_state.page == "quiz":
    st.title("🧠 Security Awareness Quiz")

    q = st.radio(
        "You receive an urgent email asking to reset your password. What do you do?",
        [
            "Click link immediately",
            "Ignore the email",
            "Verify sender & report phishing"
        ]
    )

    if st.button("Submit Quiz Answer"):
        if q == "Verify sender & report phishing":
            st.session_state.quiz_score = 90
        else:
            st.session_state.quiz_score = 40
            st.session_state.hesitation += 1

        st.session_state.page = "phishing"
        st.rerun()

# ----------------- PHISHING SIMULATION -----------------
elif st.session_state.page == "phishing":
    st.title("🎣 AI Phishing Simulator")
    st.warning("⚠ Simulated phishing email detected")

    p = st.radio(
        "Email claims: *Your salary bonus will be credited today. Login now.*",
        [
            "Click Login Button",
            "Check sender domain",
            "Report as phishing"
        ]
    )

    if st.button("Analyze Action"):
        if p == "Report as phishing":
            st.session_state.phishing_score = 90
        else:
            st.session_state.phishing_score = 30
            st.session_state.hesitation += 1

        st.session_state.page = "dashboard"
        st.rerun()

# ----------------- DASHBOARD -----------------
elif st.session_state.page == "dashboard":
    st.title("📊 Cyber Security Operations Dashboard")
    st.caption("Live AI-based cyber awareness risk assessment")

    risk, threat = ai_risk_engine(
        st.session_state.quiz_score,
        st.session_state.phishing_score,
        st.session_state.persona_risk
    )

    security_score = max(0, 1000 - (risk * 7))

    col1, col2 = st.columns([2, 1])

    with col1:
        st.plotly_chart(security_gauge(security_score), use_container_width=True)

    with col2:
        st.metric("Threat Level", threat)
        st.metric("Persona Type", st.session_state.persona)
        st.metric("Stress Indicator", f"{st.session_state.hesitation * 10}%")
        st.metric("MFA Fatigue", f"{st.session_state.hesitation}/5")

    st.success("✅ AI analysis complete. Personalized cyber risk profile generated.")

    if st.button("Restart Simulation"):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()
