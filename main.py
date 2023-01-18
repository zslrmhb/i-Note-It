import streamlit as st
import requests

API_KEY = 'BVO7yd0kvpc2UMo95zY70Jt56E6NnBxY'        

def get_notes(transcript):
    req = requests.post(
        "https://api.ai21.com/studio/v1/j1-large/complete",
        headers={f"Authorization": "Bearer {API_KEY}}"},
        json={
            "prompt": transcript, 
            "numResults": 1, 
            "maxTokens": 8, 
            "stopSequences": ["."],
            "topKReturn": 0,
            "temperature": 0.2
        }
    )
    
    return req.json()   # testing
    


transcript = ""
left, right = st.columns(2)

with left:
    st.header("Lecture Notes AI")
    transcript = st.text_area("Video Transcript", height=50)
    if st.button("Submit"):
        st.write(get_notes(transcript))    
    
    
with right:
    st.header("Lecture Chat AI")
    st.write("借鉴https://github.com/AI-Yash/st-chat")
    
