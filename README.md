
<img src="https://user-images.githubusercontent.com/96039456/213666527-039ee829-2e5d-418a-80a0-d7d2c23d9301.png" alt="drawing" width="400"/>  <img src="https://user-images.githubusercontent.com/96039456/213669053-9c9f7b9a-f34f-4e6d-b970-13d57ad6dc3a.png" alt="ini" width="800"/>   


--------------------------------------------------------------------------------------------------------------------------------------------------

https://zslrmhb-i-note-it-streamlit--scriptsmain-yj2vod.streamlit.app/


I-Note-It is an application for note generation. 

What features do we have?
- Convert text materials, such as lecture transcripts and literatures, into notes formatted in sections. 
- Answer detailed questions by Chatbot about the input materials; useful when users want to explore the note generated. 

How to use this application?
- N/A.
  
How did we make it?
- Preparation: We were using Jurassic-1 provided by Ai21, so we explore the model first.
  - Prompt engineering: Note taking is summarization by nature, so we tried to suggest the model summarizing materials provided. 
    - Zero shot and few shots learning: At the beginning, we gave the model direct prompt to generate notes from given text. However, some parts of the materials are not covered in the notes, and the notes were not logical. We gave the model several examples and tried the few shots learning afterward, and we encountered some other problems, including slow api call in request and response.  
    - Customized model: To solve the problems we have with zero and few shots learning, we decided to train our customized model. we used ChatGPT to generate dataset with over 90 training data: texts and corresponding target notes in assigned formats. 
  - Hyperparameter tuning: Note taking does not require too much randomness. Thus, we reduced the temperature, so the model will produce more rigorous notes. (TO be modified) 
- UI design: For the two main features of our application, we let the major feature, the text  input and note area, to cover most upper area of the main page; we then put Chatbox below it as an auxiliary feature.  
- Implementation: 
  - Tools: 
    - Streamlit for implementing note generation text interface. 
    - Streamlit chatbot for Question-answering bot. 
    - Custom-trained Jurassic-1 grande api for notes generation.
    - Jurassic-1 Jumbo api for Chatbot
  - User Interface:
    - Layout: Two columns for input text and note generated, one expander below for Chatbot. 
  - Prepocessing:
  - Postprocessing:
  - 
    
