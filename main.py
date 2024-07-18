import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from youtubeproj.langchain_helper import get_qa_chain, create_vector_db,create_csv_from_youtube_comments

st.title("Youtube Comment Analyser 🎬 🎥 🔴 ▶")
btn = st.button("Create Knowledgebase")
Url = st.text_input("Youtube video link: ")
if btn:
    create_csv_from_youtube_comments(Url)
    create_vector_db()

question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain.invoke({"input": question})

    st.header("Answer")
    st.write(response["answer"])
