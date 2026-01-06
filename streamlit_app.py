import streamlit as st
import plotly.graph_objects as go
import random
import re

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

    persona = "High-Risk Persona" if risk >= 70 else "Medium-Risk Persona" if risk >= 40 else "Low-Risk Persona"
    return risk, persona

# ---------------- AI MESSAGE DETECTION ----------------
def ai_message_detector(text):
    patterns = ["urgent", "verify", "click", "otp", "password", "account blocked", "limited time"]
    score = sum(1 for p in patterns if p in text.lower())
    return score >= 2, patterns

# ---------------- AI SENSITIVE DATA DETECTION ----------------
def ai_sensitive_data_detector(text):
    bank = bool(re.search(r"\b\d{12,16}\b", text))
    otp = bool(re.search(r"\b\d{4,6}\b", text))
    personal = any(k in text.lower() for k in ["aadhaar", "pan", "address", "phone", "email"])
    return bank, otp, personal

# ---------------- AI AD SCAM DETECTION ----------------
def ai_ad_detector(ad_text):
    scam_words = ["free", "win", "bonus", "click now", "limited offer", "guaranteed"]
    score = sum(1 for w in scam_words if w in ad_text.lower())
    return score >= 2

# ---------------- AI RISK ENGINE ----------------
def ai_risk_engine(quiz, phishing, persona_risk, missed_flags):
    risk = (persona_risk * 0.4) + ((100 - quiz) * 0.25) + ((100 - phishing) * 0.25) + (missed_flags * 5)
    level = "High" if risk >= 70 else "Medium" if risk >= 40 else "Low"
    return int(risk), level

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
st.sidebar.success("🤖 AI Protection Engine Active")

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
        st.session_state.page = "ai_protection"
        st.rerun()

# ---------------- AI PROTECTION SIMULATOR ----------------
elif st.session_state.page == "ai_protection":
    st.title("🤖 AI Protection Simulator")

    st.subheader("1️⃣ AI Message Detection")
    msg = st.text_area("Paste a message or email:")
    if msg:
        detected, patterns = ai_message_detector(msg)
        if detected:
            st.error("⚠️ AI detected a suspicious message (phishing indicators found)")
        else:
            st.success("✅ Message appears safe")

    st.subheader("2️⃣ AI Sensitive Data Detection")
    data = st.text_area("Enter data you want to share:")
    bank, otp, personal = ai_sensitive_data_detector(data)
    if bank:
        st.error("🚨 Bank card details detected")
    if otp:
        st.error("🚨 OTP detected – never share OTP")
    if personal:
        st.warning("⚠️ Personal data detected")

    st.subheader("3️⃣ AI Ad / Scam Detection")
    ad = st.text_input("Paste an advertisement text:")
    if ad:
        if ai_ad_detector(ad):
            st.error("🚫 Scam / deceptive advertisement blocked by AI")
        else:
            st.success("✅ Advertisement appears safe")

    if st.button("Next → Dashboard"):
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
        st.metric("AI Protection Status", "Active")

    st.success("✅ AI continuously monitoring messages, data sharing, and ads")

    if st.button("Restart Simulation"):
        st.session_state.clear()
        st.rerun()
