import streamlit as st
import time
import random
import numpy as np

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="AI Cyber Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
body {
    background: linear-gradient(120deg,#0f2027,#203a43,#2c5364);
}
.title {
    font-size: 48px;
    font-weight: bold;
    color: white;
    text-align: center;
}
.card {
    background: rgba(255,255,255,0.08);
    padding: 30px;
    border-radius: 20px;
    color: white;
    box-shadow: 0px 0px 20px rgba(0,255,255,0.2);
    transition: 0.3s;
}
.card:hover {
    transform: scale(1.03);
}
.status-safe {
    color: #00ff9d;
    font-size: 28px;
}
.status-risk {
    color: #ff4b4b;
    font-size: 28px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ LOGIN SYSTEM ------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.markdown("<h1 class='title'>🔐 Secure Login</h1>", unsafe_allow_html=True)
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if user == "admin" and pwd == "admin123":
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error("❌ Invalid Credentials")

if not st.session_state.logged_in:
    login()
    st.stop()

# ------------------ AI LOGIC ------------------
def ai_awareness_score():
    return random.randint(60, 95)

def ai_threat_level(score):
    if score > 85:
        return "LOW"
    elif score > 70:
        return "MEDIUM"
    else:
        return "HIGH"

# ------------------ DASHBOARD ------------------
st.markdown("<h1 class='title'>🛡️ AI Cyber Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

score = ai_awareness_score()
threat = ai_threat_level(score)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="card">
        <h3>🤖 AI Awareness Score</h3>
        <h1>{score} / 100</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <h3>⚠️ Threat Level</h3>
        <h1>{threat}</h1>
    </div>
    """, unsafe_allow_html=True)

with col3:
    status = "Protected ✅" if threat == "LOW" else "At Risk ❌"
    color = "status-safe" if threat == "LOW" else "status-risk"

    st.markdown(f"""
    <div class="card">
        <h3>🔒 Security Status</h3>
        <h2 class="{color}">{status}</h2>
    </div>
    """, unsafe_allow_html=True)

# ------------------ REAL-TIME AI SIMULATION ------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.subheader("📡 Real-Time AI Threat Simulation")

progress = st.progress(0)
status_text = st.empty()

for i in range(100):
    progress.progress(i + 1)
    status_text.text(f"AI Scanning Network Packets... {i+1}%")
    time.sleep(0.03)

st.success("✅ AI Scan Completed – No Active Attacks Detected")

# ------------------ USER ACTION AI ------------------
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("🧠 AI Recommendations")

if score > 85:
    st.info("✔ Excellent cyber hygiene detected. Keep systems updated.")
elif score > 70:
    st.warning("⚠ Enable 2FA and improve password strength.")
else:
    st.error("❌ High risk detected. Immediate training required.")

# ------------------ LOGOUT ------------------
st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("Logout"):
    st.session_state.logged_in = False
    st.experimental_rerun()
