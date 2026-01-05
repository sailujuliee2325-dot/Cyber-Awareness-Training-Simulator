import streamlit as st
import pandas as pd
import random
import plotly.express as px
from st_aggrid import AgGrid
import streamlit.components.v1 as components

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Cyber Awareness Simulator", layout="wide")

# ---------- SESSION STATE ----------
if 'page' not in st.session_state:
    st.session_state.page = "home"
if 'quiz_score' not in st.session_state:
    st.session_state.quiz_score = 0
if 'quiz_index' not in st.session_state:
    st.session_state.quiz_index = 0
if 'phishing_attempts' not in st.session_state:
    st.session_state.phishing_attempts = []
if 'phishing_score' not in st.session_state:
    st.session_state.phishing_score = 0

# ---------- STYLES ----------
st.markdown("""
<style>
body {
    background: #f5f7fa;
    color: #333;
    text-align: center;
}
.main-title {
    font-size: 3rem;
    font-weight: bold;
    margin-top: 50px;
    margin-bottom: 50px;
}
.nav-button button {
    width: 220px;
    height: 60px;
    margin: 15px;
    font-size: 1.2rem;
    font-weight: bold;
    color: white;
    border-radius: 15px;
    border: none;
    background: linear-gradient(90deg, #1cb5e0, #000851);
}
.card {
    background: white;
    border-radius: 12px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
    padding: 20px;
    margin: 20px auto;
    max-width: 700px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------- DATA ----------
quiz_questions = [
    {"question": "What is phishing?", "options": ["A type of malware", "Tricking users to get sensitive info", "A network protocol", "A password manager"], "answer": "Tricking users to get sensitive info"},
    {"question": "Which of these is a strong password?", "options": ["12345678", "password123", "T!g3r$2026", "qwerty"], "answer": "T!g3r$2026"},
    {"question": "What should you check in an email before clicking links?", "options": ["Sender address", "Grammatical errors", "Suspicious attachments", "All of the above"], "answer": "All of the above"}
]

phishing_examples = [
    {"type": "Email", "content": "Your account will be suspended! Click here to verify.", "correct_action": "Ignore and report", "explanation": "Legitimate companies never ask for verification like this in email."},
    {"type": "Website", "content": "http://secure-paypal.com-login.xyz", "correct_action": "Ignore and report", "explanation": "The domain is fake; always check URL carefully."},
    {"type": "Message", "content": "Congrats! You won a prize. Send your card details to claim.", "correct_action": "Ignore and report", "explanation": "This is a classic phishing scam trying to steal personal info."}
]

cyber_tips = [
    {"tip": "Use strong, unique passwords for every account."},
    {"tip": "Enable multi-factor authentication (MFA)."},
    {"tip": "Do not click links from unknown sources."},
    {"tip": "Regularly update your software and devices."},
    {"tip": "Backup your data securely."}
]

# ---------- MAIN PAGE ----------
if st.session_state.page == "home":
    st.markdown('<div class="main-title">Cyber Awareness Simulator</div>', unsafe_allow_html=True)
    
    # Robot GIF animation (replace with any GIF you like)
    st.image("https://media.giphy.com/media/3oKIPwoeGErMmaI43C/giphy.gif", width=300)
    
    # Navigation buttons
    col1, col2, col3, col4 = st.columns(4)
    if col1.button("Quiz"): st.session_state.page = "quiz"
    if col2.button("Phishing Simulator"): st.session_state.page = "phishing"
    if col3.button("Cyber Tips"): st.session_state.page = "tips"
    if col4.button("Dashboard"): st.session_state.page = "dashboard"

# ---------- QUIZ PAGE ----------
elif st.session_state.page == "quiz":
    st.title("📝 Cyber Awareness Quiz")
    if st.button("⬅ Back to Home"): st.session_state.page="home"
    
    if st.session_state.quiz_index < len(quiz_questions):
        q = quiz_questions[st.session_state.quiz_index]
        st.markdown(f"<div class='card'><h3>{q['question']}</h3></div>", unsafe_allow_html=True)
        cols = st.columns(2)
        for i, opt in enumerate(q["options"]):
            if cols[i%2].button(opt, key=f"q{st.session_state.quiz_index}_{i}"):
                if opt == q["answer"]:
                    st.session_state.quiz_score += 1
                    st.success("✅ Correct!")
                    # Confetti effect
                    components.html("""<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
                    <script>confetti({ particleCount: 100, spread: 70 });</script>""")
                else:
                    st.error(f"❌ Incorrect! Correct: {q['answer']}")
                
                # Move to next question
                st.session_state.quiz_index += 1

    else:
        st.balloons()
        st.success(f"Quiz Completed! Score: {st.session_state.quiz_score}/{len(quiz_questions)}")
        if st.button("Restart Quiz"):
            st.session_state.quiz_index = 0
            st.session_state.quiz_score = 0

# ---------- PHISHING SIMULATOR ----------
elif st.session_state.page == "phishing":
    st.title("🎣 Phishing Simulator")
    if st.button("⬅ Back to Home"): st.session_state.page="home"
    example = random.choice(phishing_examples)
    st.markdown(f"<div class='card'><b>Type:</b> {example['type']}<br><b>Content:</b><br>{example['content']}</div>", unsafe_allow_html=True)
    action = st.radio("What would you do?", ["Ignore and report", "Click/Submit info", "Forward to friend"], index=0)
    if st.button("Submit Action"):
        correct = action == example["correct_action"]
        if correct:
            st.session_state.phishing_score += 1
            st.success("✅ Correct! You recognized the phishing attempt.")
        else:
            st.error(f"❌ Incorrect! {example['explanation']}")
        st.session_state.phishing_attempts.append({"content": example["content"], "action": action, "correct": correct})

# ---------- CYBER TIPS ----------
elif st.session_state.page == "tips":
    st.title("💡 Cybersecurity Tips")
    if st.button("⬅ Back to Home"): st.session_state.page="home"
    for tip in cyber_tips:
        st.markdown(f"<div class='card'>{tip['tip']}</div>", unsafe_allow_html=True)

# ---------- DASHBOARD ----------
elif st.session_state.page == "dashboard":
    st.title("📊 Performance Dashboard")
    if st.button("⬅ Back to Home"): st.session_state.page="home"
    st.metric("Quiz Score", f"{st.session_state.quiz_score}/{len(quiz_questions)}")
    st.metric("Phishing Score", f"{st.session_state.phishing_score}/{len(st.session_state.phishing_attempts)}")
    
    quiz_df = pd.DataFrame([
        {"Status": "Correct", "Count": st.session_state.quiz_score},
        {"Status": "Incorrect", "Count": len(quiz_questions)-st.session_state.quiz_score}
    ])
    fig1 = px.pie(quiz_df, names='Status', values='Count', color='Status',
                  color_discrete_map={'Correct':'green','Incorrect':'red'},
                  title="Quiz Results")
    st.plotly_chart(fig1, use_container_width=True)
    
    if st.session_state.phishing_attempts:
        phishing_df = pd.DataFrame(st.session_state.phishing_attempts)
        st.subheader("Phishing Attempts")
        AgGrid(phishing_df, height=200, fit_columns_on_grid_load=True)
    else:
        st.info("No phishing attempts recorded yet.")
