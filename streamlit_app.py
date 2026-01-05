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

    if score == 3:
        st.balloons()
        st.write("🎉 Excellent! You are cyber aware.")
    elif score == 2:
        st.write("👍 Good job! Stay alert online.")
    else:
        st.write("⚠️ You need to improve your cyber awareness.")

st.divider()

# -----------------------------
# PHISHING EMAIL DEMO
# -----------------------------
st.header("📧 Phishing Email Simulation")

st.markdown("""
**From:** security-alert@paypaI.com  
**Subject:** Urgent: Verify your account immediately  

Dear User,

We noticed suspicious activity in your account.
Please verify your account immediately by clicking the link below,
otherwise your account will be suspended.

👉 http://paypal-verification-secure-login.com

Thank you,  
PayPal Security Team
""")

answer = st.radio(
    "Is this email safe or a phishing attempt?",
    ["Safe Email", "Phishing Email"],
    key="phish1"
)

if answer == "Phishing Email":
    st.success("Correct! 🚨 This is a phishing email.")
    st.write("**Red Flags:**")
    st.write("- Fake sender email (paypaI.com uses capital 'I')")
    st.write("- Urgent threatening message")
    st.write("- Suspicious link URL")
else:
    st.error("This is incorrect. This email shows multiple phishing signs.")
