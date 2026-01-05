import streamlit as st
import pandas as pd
import random
import plotly.express as px
from st_aggrid import AgGrid

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Cyber Awareness Simulator",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

if "phishing_score" not in st.session_state:
    st.session_state.phishing_score = 0

if "phishing_attempts" not in st.session_state:
    st.session_state.phishing_attempts = []

# ---------------- STYLES (FIXED) ----------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}

h1, h2, h3 {
    color: white;
    text-align: center;
}

.card {
    background-color: #ffffff;
    color: #111111;
    border-radius: 14px;
    padding: 24px;
    margin: 24px auto;
    max-width: 720px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.25);
}

.stButton > button {
    border-radius: 12px;
    padding: 0.6em 1.2em;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---------------- DATA ----------------
quiz_questions = [
    {
        "question": "What is phishing?",
        "options": [
            "A type of malware",
            "Tricking users to get sensitive info",
            "A network protocol",
            "A password manager"
        ],
        "answer": "Tricking users to get sensitive info"
    },
    {
        "question": "Which password is strongest?",
        "options": [
            "12345678",
            "password123",
            "T!g3r$2026",
            "qwerty"
        ],
        "answer": "T!g3r$2026"
    },
    {
        "question": "Before clicking a link, what should you check?",
        "options": [
            "Sender address",
            "Spelling errors",
            "Suspicious URLs",
            "All of the above"
        ],
        "answer": "All of the above"
    }
]

phishing_examples = [
    {
        "type": "Email",
        "content": "Your account will be suspended! Click here to verify.",
        "correct": "Ignore and report",
        "reason": "Urgent threats are a common phishing tactic."
    },
    {
        "type": "Website",
        "content": "http://secure-paypal-login.xyz",
        "correct": "Ignore and report",
        "reason": "Fake domain pretending to be PayPal."
    },
    {
        "type": "Message",
        "content": "You won a prize! Send card details to claim.",
        "correct": "Ignore and report",
        "reason": "Never share financial details."
    }
]

cyber_tips = [
    "Use strong, unique passwords",
    "Enable multi-factor authentication",
    "Do not click unknown links",
    "Update software regularly",
    "Backup important data"
]

# ---------------- HOME PAGE ----------------
if st.session_state.page == "home":
    st.markdown("<h1>🛡️ Cyber Awareness Simulator</h1>", unsafe_allow_html=True)

    st.image(
        "https://media.giphy.com/media/3oKIPwoeGErMmaI43C/giphy.gif",
        width=260
    )

    col1, col2, col3, col4 = st.columns(4)

    if col1.button("📝 Quiz"):
        st.session_state.page = "quiz"

    if col2.button("🎣 Phishing Simulator"):
        st.session_state.page = "phishing"

    if col3.button("💡 Cyber Tips"):
        st.session_state.page = "tips"

    if col4.button("📊 Dashboard"):
        st.session_state.page = "dashboard"

# ---------------- QUIZ PAGE ----------------
elif st.session_state.page == "quiz":
    st.title("📝 Cyber Awareness Quiz")

    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"

    if st.session_state.quiz_index < len(quiz_questions):
        q = quiz_questions[st.session_state.quiz_index]

        st.markdown(
            f"<div class='card'><h3>{q['question']}</h3></div>",
            unsafe_allow_html=True
        )

        for opt in q["options"]:
            if st.button(opt):
                if opt == q["answer"]:
                    st.success("✅ Correct")
                    st.session_state.quiz_score += 1
                else:
                    st.error(f"❌ Correct answer: {q['answer']}")

                st.session_state.quiz_index += 1

        st.progress(st.session_state.quiz_index / len(quiz_questions))

    else:
        st.success(
            f"Quiz completed! Score: {st.session_state.quiz_score}/{len(quiz_questions)}"
        )
        st.balloons()

        if st.button("Restart Quiz"):
            st.session_state.quiz_index = 0
            st.session_state.quiz_score = 0

# ---------------- PHISHING SIMULATOR ----------------
elif st.session_state.page == "phishing":
    st.title("🎣 Phishing Simulator")

    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"

    example = random.choice(phishing_examples)

    st.markdown(
        f"""
        <div class='card'>
        <b>Type:</b> {example['type']}<br><br>
        <b>Message:</b><br>{example['content']}
        </div>
        """,
        unsafe_allow_html=True
    )

    choice = st.radio(
        "What would you do?",
        ["Ignore and report", "Click / Respond", "Forward to others"]
    )

    if st.button("Submit"):
        if choice == example["correct"]:
            st.success("✅ Correct decision")
            st.session_state.phishing_score += 1
        else:
            st.error(f"❌ Wrong. {example['reason']}")

        st.session_state.phishing_attempts.append({
            "Message": example["content"],
            "Your Action": choice
        })

# ---------------- CYBER TIPS ----------------
elif st.session_state.page == "tips":
    st.title("💡 Cybersecurity Tips")

    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"

    for tip in cyber_tips:
        st.markdown(
            f"<div class='card'>{tip}</div>",
            unsafe_allow_html=True
        )

# ---------------- DASHBOARD ----------------
elif st.session_state.page == "dashboard":
    st.title("📊 Dashboard")

    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"

    st.metric("Quiz Score", st.session_state.quiz_score)
    st.metric("Phishing Score", st.session_state.phishing_score)

    if st.session_state.phishing_attempts:
        df = pd.DataFrame(st.session_state.phishing_attempts)
        AgGrid(df, height=220)
    else:
        st.info("No phishing attempts yet.")


