import streamlit as st

st.title("Cyber Awareness Training Simulator")

st.write("Learn how to stay safe online")

choice = st.radio(
    "Choose a topic:",
    ["Phishing Awareness", "Password Safety", "Safe Internet Practices"]
)

if choice == "Phishing Awareness":
    st.error("⚠️ Never click unknown email links. Check sender carefully.")
elif choice == "Password Safety":
    st.success("✅ Use long passwords with symbols and numbers.")
elif choice == "Safe Internet Practices":
    st.info("🔒 Avoid sharing personal details on public websites.")
