import streamlit as st

st.set_page_config(
    page_title="Cyber Awareness Training Simulator",
    page_icon="🛡️",
    layout="centered"
)

st.sidebar.title("🧭 Navigation")
section = st.sidebar.radio(
    "Go to:",
    ["Home", "Cyber Quiz", "Phishing Demo"]
)

if section == "Home":
    st.title("🛡️ Cyber Awareness Training Simulator")
    st.write(
        "This app helps users understand common cyber threats and learn "
        "how to stay safe online through quizzes and simulations."
    )

    st.info("📌 Use the sidebar to navigate through the app.")

elif section == "Cyber Quiz":
    st.title("🧠 Cyber Awareness Quiz")

    score = 0

    q1 = st.radio(
        "1️⃣ What should you do if you receive a suspicious email?",
        ["Click the link", "Ignore and delete it", "Reply with details"]
    )
    if q1 == "Ignore and delete it":
        score += 1

    q2 = st.radio(
        "2️⃣ Which password is the strongest?",
        ["123456", "password", "P@ssw0rd!2024"]
    )
    if q2 == "P@ssw0rd!2024":
        score += 1

    q3 = st.radio(
        "3️⃣ What information should you never share online?",
        ["Your favorite color", "OTP / Bank details", "Your nickname"]
    )
    if q3 == "OTP / Bank details":
        score += 1

    if st.button("✅ Submit Quiz"):
        st.success(f"Your Score: {score} / 3")

        if score == 3:
            st.balloons()
            st.write("🎉 Excellent! You are cyber aware.")
        elif score == 2:
            st.write("👍 Good job! Stay alert online.")
        else:
            st.warning("⚠️ You need to improve your cyber awareness.")

elif section == "Phishing Demo":
    st.title("📧 Phishing Email Simulation")

    st.markdown("""
    **From:** security-alert@paypaI.com  
    **Subject:** Urgent: Verify your account immediately  

    Dear User,

    We noticed suspicious activity in your account.
    Please verify your account immediately by clicking the link below,
    otherwise your account will be suspended.

    👉 http://paypal-verification-secure-login.com
    """)

    answer = st.radio(
        "Is this email safe or a phishing attempt?",
        ["Safe Email", "Phishing Email"]
    )

    if answer == "Phishing Email":
        st.success("Correct! 🚨 This is a phishing email.")
        st.write("**Red Flags:**")
        st.write("- Fake sender email (paypaI.com uses capital 'I')")
        st.write("- Urgent threatening language")
        st.write("- Suspicious website link")
    else:
        st.error("❌ Incorrect. This email has multiple phishing indicators.")

