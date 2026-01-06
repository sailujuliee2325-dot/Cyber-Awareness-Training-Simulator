import streamlit as st
import time
import plotly.graph_objects as go

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Cyber Awareness Training Simulator",
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
.metric-card {
    background-color: #020617;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 15px;
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
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🛡 Cyber Simulator")
page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Security Quiz", "Phishing Simulator", "Cyber Tips"]
)

# ---------------- SESSION STATE ----------------
if "score" not in st.session_state:
    st.session_state.score = 0

# ================= DASHBOARD =================
if page == "Dashboard":
    st.markdown('<div class="title">Cyber Security Operations Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Live Cyber Awareness Risk Assessment</div>', unsafe_allow_html=True)
    st.divider()

    col1, col2, col3 = st.columns([2, 1, 1])

    # --- SECURITY SCORE GAUGE ---
    with col1:
        score = 850
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            title={'text': "Security Score"},
            gauge={
                'axis': {'range': [0, 1000]},
                'bar': {'color': "#38bdf8"},
                'steps': [
                    {'range': [0, 400], 'color': "#7f1d1d"},
                    {'range': [400, 700], 'color': "#92400e"},
                    {'range': [700, 1000], 'color': "#064e3b"}
                ]
            }
        ))
        fig.update_layout(height=350, margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig, use_container_width=True)

    # --- STRESS & THREAT ---
    with col2:
        st.markdown('<div class="metric-card"><h3>Stress Meter</h3><h1>30%</h1></div>', unsafe_allow_html=True)
        st.progress(0.3)
        st.markdown('<div class="metric-card"><h3>Threat Level</h3><h1>Medium</h1></div>', unsafe_allow_html=True)

    # --- SOCIAL ENGINEERING ---
    with col3:
        st.markdown('<div class="metric-card"><h3>MFA Fatigue</h3><h1>3 / 7</h1></div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="metric-card"><h3>Social Engineering</h3>'
            '<p>✔ Tailgating: Passed</p>'
            '<p>✖ Urgency Cue: Failed</p></div>',
            unsafe_allow_html=True
        )

    st.divider()
    st.caption("Simulated enterprise SOC-style cyber awareness dashboard.")

# ================= QUIZ =================
elif page == "Security Quiz":
    st.markdown('<div class="title">Security Awareness Quiz</div>', unsafe_allow_html=True)

    questions = [
        ("An email asks you to urgently verify your bank account.", "Phishing"),
        ("Using the same password for all websites.", "Unsafe"),
        ("Checking the sender’s domain before clicking a link.", "Safe")
    ]

    for q, correct in questions:
        st.markdown(f'<div class="card"><b>{q}</b></div>', unsafe_allow_html=True)
        choice = st.radio("Select answer", ["Safe", "Phishing", "Unsafe"], key=q)

        if st.button("Submit", key=q+"btn"):
            if choice == correct:
                st.success("Correct decision!")
                st.session_state.score += 1
            else:
                st.error("Incorrect. This behavior is risky.")

    st.progress(st.session_state.score / len(questions))
    if st.session_state.score == len(questions):
        st.balloons()

# ================= PHISHING SIMULATOR =================
elif page == "Phishing Simulator":
    st.markdown('<div class="title">Phishing Attack Simulation</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <b>From:</b> security@paypa1.com <br>
    <b>Subject:</b> Immediate Action Required <br><br>
    Your account will be suspended unless you verify now.
    </div>
    """, unsafe_allow_html=True)

    decision = st.radio("Is this email safe?", ["Safe", "Phishing"])

    if st.button("Analyze"):
        if decision == "Phishing":
            st.markdown('<div class="alert">🚨 PHISHING DETECTED<br>Fake domain: paypa1.com</div>', unsafe_allow_html=True)
            st.success("Excellent detection!")
        else:
            st.markdown('<div class="alert">⚠️ Incorrect decision – this was phishing</div>', unsafe_allow_html=True)

# ================= CYBER TIPS =================
elif page == "Cyber Tips":
    st.markdown('<div class="title">Cyber Safety Best Practices</div>', unsafe_allow_html=True)

    tips = [
        "Enable Multi-Factor Authentication",
        "Never trust urgent or threatening emails",
        "Verify URLs carefully",
        "Avoid unknown QR codes",
        "Keep systems and apps updated"
    ]

    for tip in tips:
        st.markdown(f'<div class="safe">✔ {tip}</div>', unsafe_allow_html=True)
        time.sleep(0.2)
