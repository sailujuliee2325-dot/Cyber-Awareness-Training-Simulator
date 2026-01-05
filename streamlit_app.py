import streamlit as st

# -----------------------------
# Title
# -----------------------------
st.title("Cyber Awareness Training Simulator 🛡️")
st.write("Test your cyber security knowledge and learn about phishing attacks.")

# -----------------------------
# QUIZ SECTION
# -----------------------------
score = 0

st.subheader("Quiz: Test Your Knowledge")

st.write("Answer the following questions:")

st.markdown("**Question 1:** What should you do if you receive a suspicious email?")
q1 = st.radio(
    "",
    ["Click the link", "Ignore and delete it", "Reply with details"],
    key="q1"
)
if q1 == "Ignore and delete it":
    score += 1

st.markdown("**Question 2:** Which password is the strongest?")
q2 = st.radio(
    "",
    ["123456", "password", "P@ssw0rd!2024"],
    key="q2"
)
if q2 == "P@ssw0rd!2024":
    score += 1

st.markdown("**Question 3:** What information should you never share online?")
q3 = st.radio(
    "",
    ["Your favorite color", "OTP / Bank details", "Your nickname"],
    key="q3"
)
if q3 == "OTP / Bank details":
    score += 1

if st.button("Submit Quiz"):
    st.success(f"Your Score: {score} / 3")

