import streamlit as st

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Cyber Awareness Training Simulator",
    page_icon="🛡️",
    layout="centered"
)

# -----------------------------
# Title and Intro
# -----------------------------
st.title("Cyber Awareness Training Simulator")
st.write(
    "Learn to identify cyber threats and improve your online safety. "
    "This simulator includes a short quiz and a phishing email simulation."
)
st.divider()

# -----------------------------
# QUIZ SECTION
# -----------------------------
st.header("Cyber Awareness Quiz")

# Initialize score
if "score" not in st.session_state:
    st.session_state.score = 0

# Questions dictionary
quiz_questions = [
    {
        "question": "1. What should you do if you receive a suspicious email?",
        "options": ["Click the link", "Ignore and delete it", "Reply with details"],
        "answer": "Ignore and delete it"
    },
    {
        "question": "2. Which password is the strongest?",
        "options": ["123456", "password", "P@ssw0rd!2024"],
        "answer": "P@ssw0rd!2024"
    },
    {
        "question": "3. What information should you never share online?",
        "options": ["Your favorite color", "OTP / Bank details", "Your nickname"],
        "answer": "OTP / Bank details"
    }
]

# Loop through questions
for idx, q in enumerate(quiz_questions):
    st.subheader(q["question"])
    choice = st.radio("", q["options"], key=f"q{idx+1}")
    # Show immediate feedback if user chooses the correct answer
    if choice == q["answer"]:
        st.success("Correct!")
    elif choice != "":
        st.error("Incorrect.")

# Submit quiz button
if st.button("Submit Quiz"):
    # Calculate score
    st.session_state.score = sum(
        1 for idx, q in enumerate(quiz_questions)
        if st.session_state.get(f"q{idx+1}") == q["answer"]
    )
    st.info(f"Your Total Score: {st.session_state.score} / {len(quiz_questions)}")

    # Personalized feedback
    if st.session_state.score == len(quiz_questions):
        st.success("Excellent! You have strong cyber awareness.")
    elif st.session_state.score == len(quiz_questions) - 1:
        st.warning("Good job! A little more attention will make you safer.")
    else:
        st.error("You need to improve your cyber awareness. Review the tips below.")

st.divider()

# -----------------------------
# PHISHING EMAIL SIMULATION
# -----------------------------
st.header("Phishing Email Simulation")

st.markdown("""
**From:** security-alert@paypaI.com  
**Subject:** Urgent: Verify your account immediately  

Dear User,

We noticed unusual activity in your account.
Please verify your account immediately by clicking the link below,
otherwise your account will be suspended.

[Click here to verify](http://paypal-verification-secure-login.com)

Thank you,  
PayPal Security Team
""")

phish_choice = st.radio(
    "Is this email safe or a phishing attempt?",
    ["Safe Email", "Phishing Email"],
    key="phish_sim"
)

if phish_choice == "Phishing Email":
    st.success("Correct! This is a phishing email.")
    st.markdown("""
**Red Flags to notice:**
- Fake sender email (paypaI.com uses capital 'I')  
- Urgent threatening language  
- Suspicious link that doesn't match official domain  
- Generic greeting instead of your real name
""")
else:
    st.error("Incorrect. This email contains several phishing indicators.")

st.divider()

# -----------------------------
# CYBER TIPS SECTION
# -----------------------------
st.header("Quick Cyber Safety Tips")
st.markdown("""
- Use strong, unique passwords for all accounts.  
- Never click links from unknown senders.  
- Enable two-factor authentication (2FA) whenever possible.  
- Regularly update your software and devices.  
- Verify websites before entering personal or financial information.
""")

