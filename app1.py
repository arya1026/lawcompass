import streamlit as st

st.set_page_config(page_title="LawCompass", page_icon="⚖️")

st.title("⚖️ LawCompass – AI Legal Educator")
st.write("Ask me about Indian or International laws. I’ll explain simply!")

# Demo Q&A (offline, no API needed)
laws = {
    "What are my rights if arrested in India?": "You must be presented before a magistrate within 24 hours. You have the right to a lawyer. Police cannot force a confession.",
    "What is freedom of speech under UN law?": "Under Article 19 of the UN Declaration of Human Rights, everyone has the right to express opinions without interference.",
    "What are consumer rights in India?": "You have rights to safety, information, choice, and redressal under the Consumer Protection Act, 2019."
}

user_input = st.text_input("Your Question:")

if user_input:
    if user_input in laws:
        st.success(laws[user_input])
    else:
        st.warning("This is a demo. Try: 'What are my rights if arrested in India?'")
