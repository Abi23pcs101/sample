import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyCj2bshMo8Uo3_EuRWytkEKEWoIu0riVR8")
model=genai.GenerativeModel('gemini-2.0-flash')

name=st.text_input("Name")
if name:
    file = st.file_uploader("MyFile")
    if file:
        
        content=file.read().decode("utf-8")

        ques=st.text_input("Enter your Query")
        if ques:
            result=model.generate_content(f"question :{ques} content : {content} give the relevant information from the content")
            st.write(result.text)



    

