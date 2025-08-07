import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env variables
load_dotenv()

def configure_gemini():
    api_key = os.getenv("GEMINI_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file.")
    print("DEBUG API KEY:", api_key)
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-2.5-flash")

def get_gemini_response(model, user_query, language="en"):
    prompt = f"You are JalBot, a helpful assistant for water conservation, sanitation, and clean water practices. Answer the following in {language.upper()}:\n\nQuestion: {user_query}"
    response = model.generate_content(prompt)
    return response.text
