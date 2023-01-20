from preprocess import PreProcessor
from postprocess import PostProcessor
from notetaker import NoteTaker
from notebot import NoteBot

import streamlit as st
from streamlit_chat import message

import re
import time

# Page Config
st.set_page_config(layout='wide')

# Session States
if "generated" not in st.session_state:
    st.session_state["generated"] = False
    st.session_state["downloaded"] = True
    st.session_state["asked"] = False
    st.session_state["most_recent_note"] = ""
    

# Welcome page
st.title("i-Note-it")
st.caption("---Enhance Note-Taking Experience with Artificial Intelligence.")

# All the Services
PreProcessService = PreProcessor()
PostProcessService = PostProcessor()
NoteTakingService = NoteTaker()
NoteBotService = NoteBot()

col1, col2 = st.columns(2, gap="medium")

with col1:
    st.header("Your Text")
    generate_button = st.button("Generate")
    text = st.text_area(":keyboard: Input the text ", height=300, max_chars=5000, help="Copy & Paste the text you want to convert into markdown note")  # Corresponds to approximately 2040 tokens (max. tokens for the model)
    
with col2:
    st.header("Your Note")

    if generate_button:
        st.session_state["generated"] = True

    if st.session_state["generated"]:

        generate_success = False

        try:
            generated_note = NoteTakingService.run(text)
            generate_success = True
        except KeyError:
            st.error("Try with fewer text!")

        if generate_success:
            post_processed_note = PostProcessService.process_text(generated_note)

            with st.spinner('Wait for it...'):
                time.sleep(3)

            # if st.session_state["downloaded"]:
            #     download_button = st.download_button("Download", post_processed_note, 'i-Note-it.md')
            st.session_state["most_recent_note"] = post_processed_note
            st.session_state["generated"] = False
    
    st.markdown(st.session_state["most_recent_note"])

with st.expander("Ask your NoteBot!"):
    question = st.text_input("Question")
    if st.button("Ask"):
        message(question, is_user=True)
        message(NoteBotService.run(text,question))