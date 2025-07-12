#pipenv install streamlit 
#setup upload pdf functionality
#chatbot skeleton (question and answer)

import streamlit as st 

uploaded_file=st.file_uploader(
    "Choose a PDF file", type=["pdf"],
    accept_multiple_files=False
)

