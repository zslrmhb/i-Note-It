# from preprocess import PreProcessor
from postprocess import PostProcessor
from notetaker import NoteTaker
from notebot import NoteBot

import time

import streamlit as st
from streamlit_chat import message

# Page Config
st.set_page_config(layout='wide')

# Session States
# We want to use session states to manage the execution of each widget, 
# so a widget that is not click on will not be excuted
if "generated" not in st.session_state:
    st.session_state["generated"] = False
    st.session_state["downloaded"] = False
    st.session_state["asked"] = False
    st.session_state["most_recent_note"] = ""
    st.session_state["user_chat_history"] = []
    st.session_state["notebot_response_history"] = []
    
# Welcome page
st.title("i-Note-It")
st.caption("---Enhance Note-Taking Experience with Artificial Intelligence.")

# All the Services
# PreProcessService = PreProcessor()
PostProcessService = PostProcessor()
NoteTakingService = NoteTaker()
NoteBotService = NoteBot()

# Left, Right Columns
col1, col2 = st.columns(2, gap="medium")

with col1:
    st.header("Your Text")
    generate_button = st.button("Generate")
    text = st.text_area(":keyboard: Input the text ", height=300, max_chars=5000, help="Copy & Paste or type the text you want to convert into markdown note")  
    # Corresponds to approximately 2040 tokens (max. tokens for the model)
    
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

            st.session_state["most_recent_note"] = post_processed_note
            st.session_state["generated"] = False
    
    st.download_button("Download", st.session_state["most_recent_note"], 'i-Note-it.md')
    st.markdown(st.session_state["most_recent_note"])

# NoteBot Section
with st.expander("Ask your NoteBot!"):

    question = st.text_input("Question")
    clear_hist_button = st.button("Clear Chat History")
    if clear_hist_button:
        st.session_state["user_chat_history"].clear()
        bot_hist = st.session_state["notebot_response_history"].clear()

    if question: 
        st.session_state["asked"] = True

    if st.session_state["asked"]:

        user_hist = st.session_state["user_chat_history"]
        bot_hist = st.session_state["notebot_response_history"]
        user_hist.append(question)
        bot_hist.append(NoteBotService.run(text,question))

        # Dialogue Display
        for i in range(len(user_hist)-1, -1, -1):
            message(bot_hist[i], key=str(i) +'_bot')
            message(user_hist[i], is_user=True, key=str(i) + '_user')

        st.session_state["asked"] = False
