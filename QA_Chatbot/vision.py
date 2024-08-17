from dotenv import load_dotenv
load_dotenv() ##loading all the environment variables

import streamlit as st
import os
import google.generativeai as  genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##function write to load  gimini pro model ndget responses

model = genai.GenerativeModel("gemini-1.5-flash") ##for  text genration use gemini-pro
def get_gimini_response(input,image):
    if input != "":
        response = model.generate_content([input,image])
    else:
       response = model.generate_content(image) 
    return response.text


# Initialize our streamlit app --for  frontend application
st.set_page_config(page_title="Generic Image Demo")

st.header("Gemini Application")

input = st.text_input("Input Prompt: ",key="input")

uploaded_file = st.file_uploader("Choose an Image...",type= ["jpg","jpeg","png"])
iamge=""

if uploaded_file is not None:
    image=  Image.open(uploaded_file)
    st.image(image,caption  = "Uplaoded Image",use_column_width=True)
    
    
submit = st.button("Tell me about the image")

##If submit is clicked
if submit:
    response = get_gimini_response(input,image)
    st.subheader("The response is")
    st.write(response)