<p align="center">
<img src="assets/logo.png" width="300" height="350" />
</p>

--------------------------------------------------------------------------------------------------------------------------------------------------

I-Note-It is an application for AI note generation

<!-- toc -->
- [Features](#features)
- [How to use?](#how-to-use)
  - [Web Version](#web-streamlit-demo)
  - [Local Version](#local-streamlit-demo)
    - [Prerequisites](#prerequisites)
- [Behind the Scene](#behind-the-scene)


## Latest Features 
- Convert textual input, such as lecture transcripts and literature, into **streamlined** and **hierarchical** markdown formatted note.
- The note generation performs best with English lecture transcripts that *start* and *end* with **complete** word.
  - Other textual content, such as emoji, math formulas and programming language(especially **Python**) are supported.
  - Language other than English is supported.
    - Languages Tested: English, Chinese

- Able to **download** the markdown file of the formatted note.
- A **chatbot** that can answer detailed inquiry related to the input.
  - This is really useful when the user want to have a deeper understanding of the material. 
    - For example, the user can input the class lecture transcript and generate the note. The user is then able to ask question related to the class lecture that is inputted.

## How to use?



### Web Streamlit Demo
[Web Demo](https://zslrmhb-i-note-it-streamlit--scriptsmain-yj2vod.streamlit.app/)

### Local Streamlit Demo

#### Prerequisites
- Python 3.7 - 3.10 
  - The demo uses Python 3.9
- Streamlit: https://github.com/streamlit/streamlit
- st-chat: https://github.com/AI-Yash/st-chat
- API Key from AI21 Studio: https://docs.ai21.com/

#### Steps
> NOTE: If you want to have a local version of the demo, you will need a custom-train Jurassic-1 Grande Model. For more information in obtaining your own model, feel Free to reach out in the **Discussions** or **Issues** sections for a more detail.

##### Environment Configuration

###### 

-  Install the environment listed in the prerequisite (suggest using Anaconda to manage the environment) 

## Behind the Scene

### Language Model
#### Note Generation

##### Original Approach
- Prompt Engineering
  - Zero-Shot Prompt
  - Few-Shots Prompt
##### Final Approach
- AI21 Lab Customized Jurassic-1 Grande Model 
  - Trained a customized note generation model on the top of Jurassic-1 Grande
  - Training data comes from video transcripts from various platform such as Canvas, Youtube， TED Talks and Coursera covering various domains/subjects. In addition, English literature such as passage from William Shakespeare are included in the training data
    - Feel Free to reach out, such as in the **Discussions** or **Issues** for a more detail explanation of the training process
  - Overall better performance and lower latency from the original approach

#### Chatbot
- AI21 Lab Jurassic-1 Jumbo Model

### UI Design





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
    
