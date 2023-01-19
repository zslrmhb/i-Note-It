from postprocess import PostProcessor
from notetaker import NoteTaker

import streamlit as st

import re
import time

# Page Config
st.set_page_config(layout='wide')

# Welcome page
st.title("i-Note-it")
st.caption("---Revolutionized Note-Taking Experience with Artificial Intelligence.")

# All the Services
PostProcessService = PostProcessor()
NoteTakingService = NoteTaker()


col1, col2 = st.columns(2, gap="medium")

with col1:
    st.header("Input a text")
    generate_button = st.button("Generate")
    text = st.text_area("", height=300)
    
    # # print(type(text))
    # d = text.replace("\r", "").replace("\n", "")
    # # # d = re.sub(r'([0-9]+\.\s)\s*',r'\n\1', d).strip()
    # print(d)

with col2:
    st.header("Your Note")
    if generate_button:
        st.download_button("Download", text, 'my-note.md')
        generated_note = NoteTakingService.run(text)
        # print(generated_note)
        with st.spinner('Wait for it...'):
            time.sleep(3)
        st.success('Done!')
        st.markdown(PostProcessService.process_text(generated_note))
