from postprocess import PostProcessor
from notetaker import NoteTaker

import streamlit as st


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
    
    

with col2:
    st.header("Your Note")
    if generate_button:
        st.download_button("Download", text, 'my-note.md')
        generated_note = NoteTakingService.run(text)
        st.markdown(PostProcessService.process_text(generated_note))
