import streamlit as st
from langchain.chat_models import init_chat_model

st.title("Gemini Chatbot 🤖")

# Correct way
api_key = st.secrets["GOOGLE_API_KEY"]

model = init_chat_model(
    "google_genai:gemini-1.5-flash",
    google_api_key=api_key
)

user_input = st.text_input("Enter your prompt:")

if user_input:
    response = model.invoke(user_input)
    st.write(response.content)
