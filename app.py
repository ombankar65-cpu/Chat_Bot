import streamlit as st
import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage

# --- App Configuration ---
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("🤖 Gemini 2.5 Flash-Lite Chat")

# --- Sidebar: API Key ---
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter Google API Key", type="password")
    if api_key:
        os.environ["GOOGLE_API_KEY"] = api_key
    st.info("Get your API key from Google AI Studio.")

# --- Initialize Chat History ---
# We use Streamlit's session_state to store the list of messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display Old Chat Messages ---
for message in st.session_state.messages:
    role = "user" if isinstance(message, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(message.content)

# --- Chat Input & Logic ---
if prompt := st.chat_input("How can I help you today?"):
    if not api_key:
        st.warning("Please enter your Google API Key in the sidebar.")
    else:
        # 1. Display and store user message
        st.chat_message("user").markdown(prompt)
        user_msg = HumanMessage(content=prompt)
        st.session_state.messages.append(user_msg)

        # 2. Initialize the model
        model = init_chat_model("google_genai:gemini-2.5-flash-lite")

        # 3. Generate response
        with st.chat_message("assistant"):
            try:
                # We pass the entire history so the model knows the context
                response = model.invoke(st.session_state.messages)
                st.markdown(response.content)
                
                # 4. Store assistant message
                st.session_state.messages.append(AIMessage(content=response.content))
            except Exception as e:
                st.error(f"Error: {str(e)}")
