import streamlit as st
from streamlit_chat import message
import requests

API_KEY = '1OS8cnPzWvuRAAI1YfLg71UaDevihHbe'        
url = "https://api.ai21.com/studio/v1/j1-grande/i-Note-it/complete"

def get_notes(transcript):
    '''req = requests.post(
        "https://api.ai21.com/studio/v1/j1-large/complete",
        headers={f"Authorization": "Bearer {API_KEY}"},
        json={
            "prompt": 'transcript', 
            "numResults": 1, 
            "maxTokens": 8, 
            "stopSequences": ["."],
            "topKReturn": 0,
            "temperature": 0.2
        }
    )
    
    return req.json()   # testing'''
    instruction = "Imagine you are the best notetaker in the world. Write the most streamlined and hierarchical bullet point notes with sections for this text:\n"

    
    payload = {
        "prompt": f"{instruction}{transcript}",
        "numResults": 1,
        "maxTokens": 2048,
        "temperature": 0,
        "topKReturn": 0,
        "topP":1,
        "countPenalty": {
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        "frequencyPenalty": {
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        "presencePenalty": {
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
      },
    "stopSequences":[]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer {API_KEY}"
    }
    # print(payload['prompt'])

    response = requests.post(url, json=payload, headers=headers)
    print(response.json())
    #print(response.json()['completions'][0]['data']['text'])


    


transcript = ""
left, right = st.columns(2)

with left:
    st.header("Lecture Notes AI")
    transcript = st.text_area("Video Transcript", height=50)
    if st.button("Submit"):
        st.write(get_notes(transcript))    
    
    
with right:
    st.header("Lecture Chat AI")
    message("My message") 
    message("Hello bot!", is_user=True) 
    
