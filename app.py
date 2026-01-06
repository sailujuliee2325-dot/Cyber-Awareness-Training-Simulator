import streamlit as st
import time
import random

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Cyber Awareness Simulator",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}
.card {
    background-color: #111827;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(0,255,255,0.15);
    margin-bottom: 20px;
}
.title {
    font-size: 36px;
    font-weight: bold;
    color: #38bdf8;
}
.subtitle {
    color: #9ca3af;
}
.alert {
    background-color: #7f1d1d;
    padding: 15px;
    border-radius: 10px;
    color: white;
}
.safe {
    background-color: #064e3b;
    padding: 15px;
    border-radius: 10px;
    color: white;
}
.metric-card {
    background-color: #020617;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🛡 Cyber Simulator")
page = st.sidebar.radio(
    "Navigate",
    ["Dashboard", "Security Quiz", "Phishing Simulator", "Cyber Tips"]
)

# ---------------- SESSION STATE ----------------
if "score" not in st.session_state:
    st.session_state.score = 0

# ---------------- DASHBOARD ----------------
if page == "Dashboard":
    st.markdown('<div class="title">Cyber Awareness Training Simulator</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Advanced Interactive Cybersecurity Training Platform</div>', unsafe_allow_html=True)
    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="metric-card"><h2>Security Score</h2><h1>850 / 1000</h1></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="metric-card"><h2>Threat Detection</h2><h1>High</h1></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="metric-card"><h2>Phishing Risk</h2><h1>Medium</h1></div>', unsafe_allow_html=True)

    st.progress(0.85)
    st.caption("Overall Cyber Hygiene Level")

# ---------------- QUIZ ----------------
elif page == "Security Quiz":
    st.markdown('<div class="title">Security Awareness Quiz</div>', unsafe_allow_html=True)

    questions = [
        ("You receive an email asking to verify your bank account urgently.", "Phishing"),
        ("Password is 'john123'", "Weak"),
        ("Website uses HTTPS and valid domain", "Safe")
    ]

    for q, correct in questions:
        st.markdown(f'<div class="card"><b>{q}</b></div>', unsafe_allow_html=True)
        choice = st.radio("Select answer", ["Safe", "Phishing", "Weak"], key=q)

        if st.button("Submit", key=q+"btn"):
            if choice == correct:
                st.success("Correct! Good cyber judgment.")
                st.session_state.score += 1
            else:
                st.error("Incorrect. This is unsafe behavior.")

    st.progress(st.session_state.score / len(questions))
    if st.session_state.score == len(questions):
        st.balloons()

# ---------------- PHISHING SIMULATOR ----------------
elif page == "Phishing Simulator":
    st.markdown('<div class="title">Live Phishing Attack Simulation</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <b>Email:</b> hr-department@paypa1.com <br>
    <b>Subject:</b> Urgent: Account Verification Required <br><br>
    Click the link below to avoid account suspension.
    </div>
    """, unsafe_allow_html=True)

    decision = st.radio("Is this email safe?", ["Safe", "Phishing"])

    if st.button("Analyze Email"):
        if decision == "Phishing":
            st.markdown('<div class="alert">PHISHING DETECTED 🚨<br>Fake domain: paypa1.com</div>', unsafe_allow_html=True)
            st.success("Excellent detection!")
        else:
            st.markdown('<div class="alert">⚠️ You missed a phishing attack</div>', unsafe_allow_html=True)

# ---------------- CYBER TIPS ----------------
elif page == "Cyber Tips":
    st.markdown('<div class="title">Cyber Safety Best Practices</div>', unsafe_allow_html=True)

    tips = [
        "Never click unknown links",
        "Enable Multi-Factor Authentication",
        "Check sender email carefully",
        "Avoid QR codes from unknown sources",
        "Keep software updated"
    ]

    for tip in tips:
        st.markdown(f'<div class="safe">✔ {tip}</div>', unsafe_allow_html=True)
        time.sleep(0.2)
