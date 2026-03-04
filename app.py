import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

st.title("Gemini Chatbot 🤖")

api_key = st.secrets["GOOGLE_API_KEY"]

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=api_key
)

user_input = st.text_input("Enter your question:")

if user_input:
    response = model.invoke(user_input)
    st.write(response.content)
