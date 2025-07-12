#pipenv install streamlit 
#setup upload pdf functionality
#chatbot skeleton (question and answer)

import streamlit as st 

uploaded_file=st.file_uploader(
    "Choose a PDF file", type=["pdf"],
    accept_multiple_files=False
)


user_query=st.text_area('enter your prompt or query u r facing',height=150,placeholder='ask anaything any query u r facing')

ask_question_btn=st.button('ask ai lawyer')

if ask_question_btn:

    if uploaded_file:
        st.chat_message('user').write(user_query)

    else:
        st.error('kindly upload a pdf file to ask question from ')
    
    #RAG pipeline 
    fixed_response='hi this is fixed response'
    st.chat_message('ai lawyer').write(fixed_response)