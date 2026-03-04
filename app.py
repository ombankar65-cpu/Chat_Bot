import streamlit as st
import os
from langchain.chat_models import init_chat_model

st.title("Gemini 2.5 Flash Chatbot 🤖")

# Get API key from Streamlit Secrets
api_key = st.secrets["AIzaSyB6YhkmPcVg0ToZU85pOtYVgor3PQxUa_w"]

# Initialize model properly
model = init_chat_model(
    "google_genai:gemini-2.5-flash-lite",
    google_api_key=api_key
)

user_input = st.text_input("Enter your prompt:")

if user_input:
    response = model.invoke(user_input)
    st.write("### Response:")
    st.write(response.content)
