import requests

input_text = "Hello everyone. Welcome to Math 13, a place. You might notice I just locked in. I teach right before this. So if I am ever late, I, I don't think I will be, but if I ever am just wait a few minutes and probably just delayed by my previous class. So my name is Brandon Seward. I'd prefer you just told me Brandon. My pronouns, are they them? Or you can say he him if you prefer.\n##\n"
instruction = "Imagine you are the best notetaker in the world. Write the most streamlined and hierarchical bullet point notes with sections for this text:\n"

url = "https://api.ai21.com/studio/v1/j1-grande/i-Note-it/complete"

payload = {
    "prompt": f"{instruction}{input_text}",
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
# print(payload['prompt'])

response = requests.post(url, json=payload, headers=headers)

print(response.json()['completions'][0]['data']['text'])




# transcript = ""
# left, right = st.columns(2)

# with left:
#     st.header("Lecture Notes AI")
#     transcript = st.text_area("Video Transcript", height=50)
#     if st.button("Submit"):
#         st.write(get_notes(transcript))    
    
    
# with right:
#     st.header("Lecture Chat AI")
#     message("My message") 
#     message("Hello bot!", is_user=True) 
    