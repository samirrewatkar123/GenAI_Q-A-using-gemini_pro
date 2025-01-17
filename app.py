from dotenv import load_dotenv
load_dotenv() # to load all the env variables

import streamlit as st 
import os
import google.generativeai as genai 

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# fUNCTION TO LOAD GEMNI MODEL
model=genai.GenerativeModel('gemini-pro')
def gen_ai_response(question):
    response=model.generate_content(question)
    return response.text


# making the streamlit app

st.set_page_config(page_title="Question and Answer Bot",page_icon='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" id="question"><path fill="#a3d86b" d="M15 10.5h12c1.1 0 2 .9 2 2v7c0 1.1-.9 2-2 2h-1v3l-4-3h-7c-1.1 0-2-.9-2-2v-7c0-1.1.9-2 2-2z"></path><path fill="#67acd5" d="M13 12.5c0-1.1.9-2 2-2h3v-1c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v7c0 1.1.9 2 2 2h1v3l4-3h4v-6z"></path><path fill="#40455a" d="M26 25c-.1 0-.2 0-.3-.1L21.8 22H15c-1.4 0-2.5-1.1-2.5-2.5v-7c0-1.4 1.1-2.5 2.5-2.5h12c1.4 0 2.5 1.1 2.5 2.5v7c0 1.4-1.1 2.5-2.5 2.5h-.5v2.5c0 .2-.1.4-.3.4-.1.1-.1.1-.2.1zM15 11c-.8 0-1.5.7-1.5 1.5v7c0 .8.7 1.5 1.5 1.5h7c.1 0 .2 0 .3.1l3.2 2.4v-2c0-.3.2-.5.5-.5h1c.8 0 1.5-.7 1.5-1.5v-7c0-.8-.7-1.5-1.5-1.5H15z"></path><path fill="#40455a" d="M5 22c-.1 0-.2 0-.2-.1-.2-.1-.3-.3-.3-.4V19H4c-1.4 0-2.5-1.1-2.5-2.5v-7C1.5 8.1 2.6 7 4 7h12c1.4 0 2.5 1.1 2.5 2.5v1c0 .3-.2.5-.5.5h-3c-.8 0-1.5.7-1.5 1.5v6c0 .3-.2.5-.5.5H9.2l-3.9 2.9c-.1.1-.2.1-.3.1zM4 8c-.8 0-1.5.7-1.5 1.5v7c0 .8.7 1.5 1.5 1.5h1c.3 0 .5.2.5.5v2l3.2-2.4c.1-.1.2-.1.3-.1h3.5v-5.5c0-1.4 1.1-2.5 2.5-2.5h2.5v-.5c0-.8-.7-1.5-1.5-1.5H4z"></path><path fill="#40455a" d="M9 16H8c-.8 0-1.5-.7-1.5-1.5v-3c0-.8.7-1.5 1.5-1.5h1c.8 0 1.5.7 1.5 1.5v3c0 .8-.7 1.5-1.5 1.5zm-1-5c-.3 0-.5.2-.5.5v3c0 .3.2.5.5.5h1c.3 0 .5-.2.5-.5v-3c0-.3-.2-.5-.5-.5H8zM23 19c-.3 0-.5-.2-.5-.5v-4c0-.3-.2-.5-.5-.5h-2c-.3 0-.5.2-.5.5v4c0 .3-.2.5-.5.5s-.5-.2-.5-.5v-4c0-.8.7-1.5 1.5-1.5h2c.8 0 1.5.7 1.5 1.5v4c0 .3-.2.5-.5.5z"></path><path fill="#40455a" d="M22.5 17h-3c-.3 0-.5-.2-.5-.5s.2-.5.5-.5h3c.3 0 .5.2.5.5s-.2.5-.5.5zM11 16c-.1 0-.3 0-.4-.1l-2-2c-.2-.2-.2-.5 0-.7s.5-.2.7 0l2 2c.2.2.2.5 0 .7 0 0-.2.1-.3.1z"></path></svg>')

st.header('Gemni LLM Appllication')

input=st.text_input('Input',key='input')

submit=st.button('Ask the Qurestion')

# After Clicking the Submit Button

if submit:
    response=gen_ai_response(input)
    st.subheader('The Response is ')
    st.write(response)
    
    


