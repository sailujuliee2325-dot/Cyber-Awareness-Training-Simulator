import streamlit as st
import random
import time
import pandas as pd
import plotly.express as px

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Cyber Awareness Training Simulator",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
defaults = {
    "page": "home",
    "quiz_index": 0,
    "quiz_score": 0,
    "phish_score": 0,
    "phish_log": [],
    "attack_start": None,
    "current_attack": None
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ---------------- STYLES ----------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
h1,h2,h3 {
    color: white;
    text-align: center;
}
.card {
    background: white;
    color: #111;
    border-radius: 16px;
    padding: 26px;
    margin: 24px auto;
    max-width: 760px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}
.stButton>button {
    border-radius: 12px;
    font-weight: 600;
    padding: 0.6em 1.3em;
}
</style>
""", unsafe_allow_html=True)

# ---------------- DATA ----------------
quiz = [
    ("What is phishing?", ["Malware", "Tricking users to steal data", "Firewall", "Encryption"], "Tricking users to steal data"),
    ("Strong password example?", ["123456", "password", "T!g3r$2026", "admin"], "T!g3r$2026"),
    ("What should you check in emails?", ["Sender", "Links", "Grammar", "All of the above"], "All of the above"),
]

phishing_attacks = [
    ("Email", "⚠️ Your account is locked. Verify immediately.", "Ignore & Report", "Urgency tactic"),
    ("SMS", "🎁 You won ₹50,000! Click to claim.", "Ignore & Report", "Prize scam"),
    ("Website", "http://secure-paypal-login.xyz", "Ignore & Report", "Fake domain"),
    ("Email", "Invoice attached – review urgently.", "Ignore & Report", "Malicious attachment")
]

tips = [
    "Enable multi-factor authentication",
    "Never click unknown links",
    "Verify sender domains carefully",
    "Use password managers",
    "Keep systems updated"
]

# ---------------- HOME ----------------
if st.session_state.page == "home":
    st.markdown("<h1>🛡️ Cyber Awareness Training Simulator</h1>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/3oKIPwoeGErMmaI43C/giphy.gif", width=260)

    c1, c2, c3, c4 = st.columns(4)
    if c1.button("📝 Awareness Quiz"):
        st.session_state.page = "quiz"
    if c2.button("🚨 Live Phishing Simulation"):
        st.session_state.page = "phishing"
    if c3.button("💡 Cyber Tips"):
        st.session_state.page = "tips"
    if c4.button("📊 Security Dashboard"):
        st.session_state.page = "dashboard"

# ---------------- QUIZ ----------------
elif st.session_state.page == "quiz":
    st.title("📝 Cyber Awareness Quiz")

    if st.button("⬅ Back"):
        st.session_state.page = "home"

    if st.session_state.quiz_index < len(quiz):
        q, opts, ans = quiz[st.session_state.quiz_index]
        st.markdown(f"<div class='card'><h3>{q}</h3></div>", unsafe_allow_html=True)

        for o in opts:
            if st.button(o):
                if o == ans:
                    st.success("✅ Correct")
                    st.session_state.quiz_score += 1
                else:
                    st.error(f"❌ Correct: {ans}")
                st.session_state.quiz_index += 1
    else:
        st.success(f"Quiz completed — Score {st.session_state.quiz_score}/{len(quiz)}")
        st.balloons()
        if st.button("Restart Quiz"):
            st.session_state.quiz_index = 0
            st.session_state.quiz_score = 0

# ---------------- LIVE PHISHING ----------------
elif st.session_state.page == "phishing":
    st.title("🚨 Live Phishing Attack Simulation")

    if st.button("⬅ Back"):
        st.session_state.page = "home"

    if st.session_state.attack_start is None:
        st.session_state.attack_start = time.time()
        st.session_state.current_attack = random.choice(phishing_attacks)

    elapsed = int(time.time() - st.session_state.attack_start)
    remaining = max(0, 15 - elapsed)

    st.warning(f"⏳ Respond before: {remaining}s")

    atype, content, correct, reason = st.session_state.current_attack

    st.markdown(f"""
    <div class='card'>
    <b>📩 Incoming {atype}</b><br><br>
    {content}
    </div>
    """, unsafe_allow_html=True)

    decision = st.radio("Your action:", ["Ignore & Report", "Click / Respond", "Forward"])

    if st.button("Respond") or remaining == 0:
        success = decision == correct
        if success:
            st.success("🛡️ Threat blocked")
            st.session_state.phish_score += 1
        else:
            st.error(f"❌ Breach — {reason}")

        st.session_state.phish_log.append({
            "Attack": content,
            "Decision": decision,
            "Time(s)": elapsed
        })

        st.session_state.attack_start = None

# ---------------- TIPS ----------------
elif st.session_state.page == "tips":
    st.title("💡 Cybersecurity Best Practices")

    if st.button("⬅ Back"):
        st.session_state.page = "home"

    for t in tips:
        st.markdown(f"<div class='card'>{t}</div>", unsafe_allow_html=True)

# ---------------- DASHBOARD ----------------
elif st.session_state.page == "dashboard":
    st.title("📊 Security Awareness Dashboard")

    if st.button("⬅ Back"):
        st.session_state.page = "home"

    c1, c2, c3 = st.columns(3)
    c1.metric("Quiz Score", st.session_state.quiz_score)
    c2.metric("Threats Blocked", st.session_state.phish_score)
    c3.metric("Risk Level", "HIGH" if st.session_state.phish_score < 2 else "LOW")

    if st.session_state.phish_log:
        df = pd.DataFrame(st.session_state.phish_log)
        fig = px.histogram(df, x="Time(s)", title="Response Time Distribution")
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(df)
    else:
        st.info("No incidents logged yet.")
