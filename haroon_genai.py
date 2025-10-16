import streamlit as st
from google import genai
haroon = genai.Client(api_key="AIzaSyAk2kT0-dBYGW0HcjOSE5cYRkVbH2I8VIo")
st.title('haroon new chatgpt')
question = st.text_input("Enter some text")
st.file_uploader('upload multiple files')
if st.button("send"):
    response=haroon.models.generate_content(model="gemini-2.5-flash",contents=question)
    st.write(response.text)

