import streamlit as st
import re
import random

st.set_page_config(page_title="Cyber Awareness Simulator", layout="centered")

st.title("🛡️ Cyber Awareness Simulator (AI Assisted)")

menu = st.sidebar.selectbox(
    "Select Awareness Module",
    [
        "Strong Password Checker",
        "Phishing Email Detection",
        "Scam Message Detection",
        "Cyber Attack Simulation",
        "Protective Measures"
    ]
)

# ---------------- PASSWORD CHECKER ----------------
if menu == "Strong Password Checker":
    st.header("🔐 Strong Password Checker")
    password = st.text_input("Enter Password", type="password")

    def check_password_strength(pw):
        score = 0
        if len(pw) >= 8: score += 1
        if re.search(r"[A-Z]", pw): score += 1
        if re.search(r"[a-z]", pw): score += 1
        if re.search(r"[0-9]", pw): score += 1
        if re.search(r"[@$!%*?&]", pw): score += 1
        return score

    if password:
        strength = check_password_strength(password)
        if strength <= 2:
            st.error("Weak Password ❌")
        elif strength == 3:
            st.warning("Moderate Password ⚠️")
        else:
            st.success("Strong Password ✅")

        st.info("Suggested Strong Password:")
        st.code("".join(random.sample("Aa1@Bb2#Cc3$Dd4%", 10)))

# ---------------- EMAIL DETECTION ----------------
elif menu == "Phishing Email Detection":
    st.header("📧 Phishing Email Detection")
    email_text = st.text_area("Paste Email Content")

    phishing_keywords = ["urgent", "verify", "click here", "account suspended", "login now"]

    if email_text:
        if any(word in email_text.lower() for word in phishing_keywords):
            st.error("⚠️ Phishing Email Detected")
        else:
            st.success("✅ Safe Email")

# ---------------- MESSAGE DETECTION ----------------
elif menu == "Scam Message Detection":
    st.header("📱 Scam Message Detection")
    message = st.text_area("Paste SMS / WhatsApp Message")

    scam_keywords = ["won", "lottery", "free", "claim now", "limited offer", "click link"]

    if message:
        if any(word in message.lower() for word in scam_keywords):
            st.error("⚠️ Scam Message Detected")
        else:
            st.success("✅ Message Seems Safe")

# ---------------- ATTACK SIMULATION ----------------
elif menu == "Cyber Attack Simulation":
    st.header("💻 Cyber Attack Simulator")

    attack = st.selectbox(
        "Choose Attack Type",
        ["Phishing Attack", "Brute Force Attack", "Malware Download"]
    )

    if st.button("Simulate Attack"):
        if attack == "Phishing Attack":
            st.warning("Fake Email Sent: 'Your bank account is blocked. Click here.'")
        elif attack == "Brute Force Attack":
            st.warning("Multiple login attempts detected from unknown IP.")
        elif attack == "Malware Download":
            st.warning("User clicked unknown file. System infected.")

# ---------------- PROTECTIVE MEASURES ----------------
elif menu == "Protective Measures":
    st.header("🧠 Cyber Safety Tips")

    tips = [
        "Use strong and unique passwords",
        "Do not click unknown links",
        "Verify sender email address",
        "Enable Two-Factor Authentication",
        "Install antivirus software",
        "Keep software updated",
        "Never share OTP or passwords"
    ]

    for tip in tips:
        st.success("✔️ " + tip)
