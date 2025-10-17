import streamlit as st
from google import genai
import mimetypes
haroon = genai.Client(api_key="AIzaSyAk2kT0-dBYGW0HcjOSE5cYRkVbH2I8VIo")
st.title('haroon new chatgpt')
question = st.text_input("Enter some text")
my_file=st.file_uploader('upload multiple files',type=None,accept_multiple_files=True)
if my_file:
    st.success("files uploaded")
else:
    st.error("not file uploaded yet")
if st.button("send"):
    if my_file:
        file_refs=[]
        for file in my_file:
            file_name=file.name
            with open(file_name,"wb") as f:
                f.write(file.getbuffer())
            uploaded=haroon.files.upload(file=file_name)
            file_refs.append(uploaded)
        response=haroon.models.generate_content(model="gemini-2.5-flash",contents=[question,file_refs])
        st.write(response.text)
    else:
        response=haroon.models.generate_content(model="gemini-2.5-flash",contents=question)
        st.write(response.text)


