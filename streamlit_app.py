import streamlit as st
import plotly.graph_objects as go
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Cyber Awareness Simulator",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "persona"
    st.session_state.quiz_score = 0
    st.session_state.phishing_score = 0
    st.session_state.hesitation = 0
    st.session_state.persona = ""
    st.session_state.persona_risk = 0
    st.session_state.missed_flags = 0

# ---------------- AI PERSONA ENGINE ----------------
def ai_persona_engine(role, experience, pressure):
    risk = 0
    risk += 30 if role == "Employee" else 15 if role == "Manager" else 5
    risk += 30 if experience == "Beginner" else 15 if experience == "Intermediate" else 5
    risk += 30 if pressure == "High" else 15 if pressure == "Medium" else 5

    persona = (
        "High-Risk Persona" if risk >= 70 else
        "Medium-Risk Persona" if risk >= 40 else
        "Low-Risk Persona"
    )
    return risk, persona

# ---------------- AI PHISHING GENERATOR ----------------
def generate_phishing_email(role, pressure):
    emails = [
        {
            "subject": "Urgent: Payroll Update Required",
            "body": "Your salary bonus is pending. Login within 30 minutes to avoid cancellation.",
            "flags": ["Urgency", "Suspicious Link", "Unexpected Bonus"]
        },
        {
            "subject": "Security Alert: Account Compromised",
            "body": "We detected unusual activity. Verify your identity immediately.",
            "flags": ["Fear Tactic", "Generic Greeting", "Link Mismatch"]
        },
        {
            "subject": "HR Notice: Policy Acknowledgement",
            "body": "New company policy attached. Download and sign.",
            "flags": ["Unexpected Attachment", "No Internal Signature"]
        }
    ]
    return random.choice(emails)

# ---------------- AI RISK ENGINE ----------------
def ai_risk_engine(quiz, phishing, persona_risk, missed_flags):
    risk = (persona_risk * 0.4) + ((100 - quiz) * 0.25) + ((100 - phishing) * 0.25) + (missed_flags * 5)
    level = "High" if risk >= 70 else "Medium" if risk >= 40 else "Low"
    return int(risk), level

# ---------------- AI RECOMMENDATIONS ----------------
def ai_recommendations(persona, missed):
    tips = []
    if persona == "High-Risk Persona":
        tips.append("Mandatory phishing awareness training recommended.")
    if missed > 1:
        tips.append("Improve identification of urgency and emotional manipulation.")
    tips.append("Always verify sender domains and avoid clicking embedded links.")
    tips.append("Enable MFA and report suspicious emails immediately.")
    return tips

# ---------------- GAUGE ----------------
def gauge(score):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        gauge={
            "axis": {"range": [0, 1000]},
            "bar": {"color": "#4CC9F0"},
            "steps": [
                {"range": [0, 400], "color": "#8B0000"},
                {"range": [400, 700], "color": "#FF8C00"},
                {"range": [700, 1000], "color": "#006400"},
            ],
        },
    ))
    fig.update_layout(height=350)
    return fig

# ---------------- SIDEBAR ----------------
st.sidebar.title("🛡 Cyber Simulator")
st.sidebar.success("AI Engine Active")

# ---------------- PERSONA PAGE ----------------
if st.session_state.page == "persona":
    st.title("👤 AI Persona Profiling")

    role = st.selectbox("Role", ["Employee", "Manager", "Administrator"])
    experience = st.selectbox("Cyber Awareness Level", ["Beginner", "Intermediate", "Advanced"])
    pressure = st.selectbox("Work Pressure Level", ["Low", "Medium", "High"])

    if st.button("Next → Start Quiz"):
        risk, persona = ai_persona_engine(role, experience, pressure)
        st.session_state.persona_risk = risk
        st.session_state.persona = persona
        st.session_state.page = "quiz"
        st.rerun()

# ---------------- QUIZ PAGE ----------------
elif st.session_state.page == "quiz":
    st.title("🧠 Security Awareness Quiz")

    answer = st.radio(
        "You receive an urgent password reset email. What do you do?",
        [
            "Click the link immediately",
            "Ignore it",
            "Verify sender and report phishing"
        ]
    )

    if st.button("Submit Answer"):
        if answer == "Verify sender and report phishing":
            st.session_state.quiz_score = 90
        else:
            st.session_state.quiz_score = 40
            st.session_state.hesitation += 1

        st.session_state.page = "phishing"
        st.rerun()

# ---------------- PHISHING SIMULATION ----------------
elif st.session_state.page == "phishing":
    st.title("🎣 AI Phishing Simulation")

    email = generate_phishing_email("", "")
    st.subheader(email["subject"])
    st.info(email["body"])

    st.markdown("### 🔍 Identify phishing red flags")
    selected_flags = st.multiselect(
        "Select all that apply:",
        ["Urgency", "Suspicious Link", "Unexpected Bonus",
         "Fear Tactic", "Generic Greeting", "Link Mismatch",
         "Unexpected Attachment", "No Internal Signature"]
    )

    if st.button("Analyze Email"):
        correct = set(email["flags"])
        chosen = set(selected_flags)

        missed = len(correct - chosen)
        st.session_state.missed_flags = missed

        if missed == 0:
            st.session_state.phishing_score = 95
            st.success("Excellent! All red flags identified.")
        else:
            st.session_state.phishing_score = max(40, 95 - missed * 15)
            st.warning(f"You missed {missed} red flags.")

        st.session_state.page = "dashboard"
        st.rerun()

# ---------------- DASHBOARD ----------------
elif st.session_state.page == "dashboard":
    st.title("📊 Cyber Security Operations Dashboard")

    risk, threat = ai_risk_engine(
        st.session_state.quiz_score,
        st.session_state.phishing_score,
        st.session_state.persona_risk,
        st.session_state.missed_flags
    )

    security_score = max(0, 1000 - risk * 7)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.plotly_chart(gauge(security_score), use_container_width=True)

    with col2:
        st.metric("Threat Level", threat)
        st.metric("Persona", st.session_state.persona)
        st.metric("Missed Red Flags", st.session_state.missed_flags)

    st.markdown("## 🤖 AI Recommendations")
    for tip in ai_recommendations(st.session_state.persona, st.session_state.missed_flags):
        st.info(tip)

    if st.button("Restart Simulation"):
        st.session_state.clear()
        st.rerun()
