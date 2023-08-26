import streamlit as st
from utils import parse_pdf, embed_text, get_answer
import os


with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    

st.header("Doc QA")
uploaded_file = st.file_uploader("Upload a pdf", type=["pdf"])

if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.")
    st.stop()

if uploaded_file is not None and openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key
    index = embed_text(parse_pdf(uploaded_file))
    query = st.text_area("Ask a question about the document")
    button = st.button("Submit")
    if button:
        st.write(get_answer(index, query))
