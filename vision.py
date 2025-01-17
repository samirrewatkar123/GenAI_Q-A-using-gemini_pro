from dotenv import load_dotenv
load_dotenv() # to load all the env variables

import streamlit as st 
import os
import google.generativeai as genai 

from PIL import Image

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# fUNCTION TO LOAD GEMNI MODEL
model=genai.GenerativeModel('gemini-1.5-flash.')
def gen_ai_response(input,image):
    if input!='':
        
       response=model.generate_content([input,image])
       
    else :
        response=model.generate_content(image)
    return response.text


# making the streamlit app

st.set_page_config(page_title="Gemni Image Q/A")

st.header('Gemni LLM Appllication')

input=st.text_input('Input  Prompt',key='input')

uploaded_file=st.file_uploader('Choose an Image....',type=['jpg','jpeg','png'])

image=""


if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption='Uploaded Image',use_column_width=True)
    
submit=st.button('Tell me about the Image')

if submit:
    response=gen_ai_response(input,image)
    st.subheader('The Response is ')
    st.write(response)