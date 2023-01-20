# i-Note-it
---------------------
I-Note-It is an application for note generation. 

What features do we have?
- Convert text materials, such as lecture transcripts and literatures, into notes formatted in sections. 
- Answer detailed questions by Chatbot about the input materials; useful when users want to explore the note generated. 

How to use this application?
- N/A.
  
How did we make it?
- Preparation: We were using Jurassic-1 provided by Ai21, so we explore the model first.
  - Prompt engineering: Note taking is summarization by nature, so we tried to suggest the model summarizing materials provided. After we failed several trials, we realized that a single prompt might not be effective. Thus, we decided to stick to one prompt and apply few shots learning and train our own model. 
  - Few shots learning: In order to collect enough examples for few shots learning, we used ChatGPT to generate dataset: texts and corresponding target notes in assigned formats. 
  - Hyperparameter tuning: Note taking does not require too much randomness. Thus, we reduced the temperature, so the model will produce more determined notes. (TO be modified) 
- UI design: For the two main features of our application, we let the major feature, the text  input and note area, to cover most upper area of the main page; we then put Chatbox below it as an auxiliary feature.  
- Implementation: 