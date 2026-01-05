import streamlit as st

st.title("Cyber Awareness Training Simulator 🛡️")
st.write("Test your cyber security knowledge with this short quiz.")

score = 0

st.subheader("Question 1")
q1 = st.radio(
    "What should you do if you receive a suspicious email?",
    ["Click the link", "Ignore and delete it", "Reply with details"]
)
if q1 == "Ignore and delete it":
    score += 1

st.subheader("Question 2")
q2 = st.radio(
    "Which password is the strongest?",
    ["123456", "password", "P@ssw0rd!2024"]
)
if q2 == "P@ssw0rd!2024":
    score += 1

st.subheader("Question 3")
q3 = st.radio(
    "What information should you never share online?",
    ["Your favorite color", "OTP / Bank details", "Your nickname"]
)
if q3 == "OTP / Bank details":
    score += 1

if st.button("Submit Quiz"):
    st.success(f"Your Score: {score} / 3")

    if score == 3:
        st.balloons()
        st.write("🎉 Excellent! You are cyber aware.")
    elif score == 2:
        st.write("👍 Good job! Stay alert online.")
    else:
        st.write("⚠️ You need to improve your cyber awareness.")
