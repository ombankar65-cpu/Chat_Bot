import streamlit as st
import os
from langchain.chat_models import init_chat_model

st.title("Gemini 2.5 Flash Chatbot 🤖")

# Get API key from Streamlit Secrets
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize model
model = init_chat_model("google_genai:gemini-2.5-flash-lite")

# User input box
user_input = st.text_input("Enter your prompt:")

if user_input:
    response = model.invoke(user_input)
    st.write("### Response:")
    st.write(response.content)
