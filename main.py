import streamlit as st
st.set_page_config(layout='wide')

# Welcome page
st.title("i-Note-it")
st.caption("---Revolutionized Note-Taking Experience with Artificial Intelligence.")


col1, col2 = st.columns(2, gap="medium")

with col1:
    st.header("Input a text")
    generate = st.button("Generate")
    text = st.text_area("", height=300)
    

with col2:
    st.header("Your Note")
    if generate:
        st.download_button("Download", text, 'my-note.md')
        st.markdown(text)