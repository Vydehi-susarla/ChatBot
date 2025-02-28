import streamlit as st
import google.generativeai as genai

API_key="AIzaSyCFFB9Ow6bwHUsqrVSkhYvKwqcI3I0oo28"
genai.configure(api_key=API_key)
model=genai.GenerativeModel('gemini-1.5-flash')

if "chat" not in st.session_state:
    st.session_state.chat=model.start_chat(history=[])
st.title("AI Personalized ChatBot")
st.write("Welcome to my ChatBot,How can i help you!")

if "messages" not in st.session_state:
    st.session_state.messages=[]
for message in st.session_state.messages:
    with st.chat_message(message["role'])
        st.markdowm(message["content"])
if prompt := st.chat_input("Say something..."):
    st.session_state.message.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    response=st.session_state.chat.send_message(prompt)
    st.session_state.messages.append({"role":"assistant","content":response.text})
    with st.chat_messages("assistant"):
        st.markdown(response.text)


