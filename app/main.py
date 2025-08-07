import streamlit as st
from qa_engine import configure_gemini, get_gemini_response

st.set_page_config(page_title="JalBot 💧", page_icon="💧")
st.title("💧 JalBot: Your Water Conservation Assistant")

st.markdown("""
Welcome to **JalBot** – your personal assistant for learning how to save water, maintain clean water, and practice good sanitation.  
Click a topic below or ask your own question!
""")

# 🌐 Language selection
language_map = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Tamil": "ta"
}
language_choice = st.selectbox("🌐 Choose your language:", list(language_map.keys()))
lang_code = language_map[language_choice]

# Load Gemini model (no need to ask for API key now)
try:
    model = configure_gemini()
except Exception as e:
    st.error(str(e))
    st.stop()

# Define topic buttons
topics = {
    "💧 Water-Saving Methods": "List effective techniques to conserve water at home, school, and in the community.",
    "🚿 Reduce Daily Water Usage": "Give daily habits people can adopt to reduce water usage.",
    "🧼 Sanitation Awareness": "Why is sanitation important and how does it relate to clean water?",
}

# Topic buttons
for label, prompt in topics.items():
    if st.button(label):
        with st.spinner("Thinking..."):
            response = get_gemini_response(model, prompt, language=lang_code)
            st.success(response)

# Freeform question
st.markdown("---")
user_input = st.text_input("💬 Or ask your own question:")

if user_input:
    with st.spinner("Thinking..."):
        response = get_gemini_response(model, user_input, language=lang_code)
        st.success(response)
