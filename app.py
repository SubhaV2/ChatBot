import streamlit as st

# Sidebar
st.sidebar.title("Chats")
st.sidebar.checkbox("Display all")

# Title
st.title("Chat App")
st.write("Chatbot Powered by Groq")
st.divider()

with st.container():
    st.subheader("Navbar")
    st.write("[Chat](./chat)")
