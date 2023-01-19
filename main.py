from postprocess import PostProcessor
from notetaker import NoteTaker

import streamlit as st

import re
import time

# Page Config
st.set_page_config(layout='wide')

# Welcome page
st.title("i-Note-it")
st.caption("---Enhance Note-Taking Experience with Artificial Intelligence.")

# All the Services
PostProcessService = PostProcessor()
NoteTakingService = NoteTaker()


col1, col2 = st.columns(2, gap="medium")

with col1:
    st.header("Input a text")
    generate_button = st.button("Generate")
    text = st.text_area(":keyboard: Input the text ", height=300)
    
with col2:
    st.header("Your Note")
    if generate_button:
        generated_note = NoteTakingService.run(text)
        post_processed_note = PostProcessService.process_text(generated_note)

        with st.spinner('Wait for it...'):
            time.sleep(3)

        download_button = st.download_button("Download", post_processed_note, 'i-Note-it.md')
        st.markdown(post_processed_note)