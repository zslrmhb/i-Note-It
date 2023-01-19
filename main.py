import streamlit as st
from streamlit_chat import message
import requests

'''API_KEY = '1OS8cnPzWvuRAAI1YfLg71UaDevihHbe'''


def get_notes(transcript):
    instruction = "Imagine you are the best notetaker in the world. Write the most streamlined and hierarchical bullet point notes with sections for this text:\n"
    transcript = "i like apple"
    url = "https://api.ai21.com/studio/v1/j1-grande/i-Note-it/complete"
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
        "Authorization": "Bearer 9LpqTGIFLsKwtjtVHwIwGRLxIeP9tQDT"
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.json())
    return(response.json()['completions'][0]['data']['text'])


    
def get_message(transcript,question):

    headers={"Authorization": "Bearer 1OS8cnPzWvuRAAI1YfLg71UaDevihHbe"},
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer 1OS8cnPzWvuRAAI1YfLg71UaDevihHbe"
    }
    url = "https://api.ai21.com/studio/v1/j1-jumbo/complete"
    transcript = "The 1881 world tour of King Kalākaua of the Hawaiian Kingdom was his attempt to save the Hawaiian culture and population from extinction by importing a labor force from Asia-Pacific nations. His efforts brought the small island nation to the attention of world leaders, but sparked rumors that the kingdom was for sale. Critics in Hawaii believed the labor negotiations were just an excuse to see the world. The 281-day trip gave Kalākaua the distinction of being the first monarch to circumnavigate the globe; his 1874 travels had made him the first reigning monarch to visit the United States and the first honoree of a state dinner at the White House."
    instruction1 = "Context: "
    instruction2 = "\nQuestion: "
    question = "what happened in 1881?"
    instruction3 = "\nAnswer: "
    payload = {
        "prompt": f"{instruction1}{transcript}{instruction2}{question}{instruction3}",
        "numResults": 1,
        "maxTokens": 64,
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
        "stopSequences":["↵"]
    }
    response = requests.post(url,json=payload,headers=headers)
    print(response.json()['completions'][0]['data']['text'])

    

transcript = ""
left, right = st.columns(2)

with left:
    st.header("Lecture Notes AI")
    transcript = st.text_area("Video Transcript", height=50)
    if st.button("Submit"):
        st.write(get_notes(transcript))
            
    
    
with right:
    st.header("Lecture Chat AI")
    message("Hi!") 
    message("Hello bot!", is_user=True) 
    
    
