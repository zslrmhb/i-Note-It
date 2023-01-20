<p align="center">
<img src="assets/logo.png" width="300" height="350" />
</p>

--------------------------------------------------------------------------------------------------------------------------------------------------

I-Note-It is an application for AI note generation

<!-- toc -->
- [Features](#latest-features)
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
> NOTE BEFORE PROCEEDING: If you want to have a local version of the demo, you will need a custom-train Jurassic-1 Grande Model. For more information in obtaining your own model, feel Free to reach out in the **Discussions** or **Issues** sections for a more detail.

##### Environment Configuration

###### Recommended (For Win64 Platform Only, Unfortunately)
1. Clone this Github Repository
2. Follow the instruction in the [requirements.txt](requirements.txt) to initialize the conda environment

###### Alternative
1. Install the packages listed in the prerequisite (suggest using Anaconda to manage the environment) 

##### config.py
- As you may or may not notice, the program requires a config.py and we did not included it for the purpose of not sharing the API token. 
- You going to set it up in your local environment, here is how:
  1. Once you have done all the steps above(Configured te environment), go to your cloned repository.
  2. Navigate into the **scripts** folder of the cloned repository.
  3. create a **config.py** file with content in the following format
  ```PYTHON
  API_TOKEN = ""       
  NOTETAKER_MODEL_URL = ""
  NOTEBOT_MODEL_URL = ""
  ```
    - API_TOKEN: Your AI21 Studio API KEY
    - NOTETAKER_MODEL_URL = The URL of your customized note generation model
    - NOTEBOT_MODEL_URL = The URL of your chatbot model
      - ex
        ```PYTHON
        NOTEBOT_MODEL_URL = "https://api.ai21.com/studio/v1/j1-jumbo/complete"
        ```


## Behind the Scene

### Language Model
#### Note Generation

##### Original Approach
- Prompt Engineering
  - Zero-Shot Prompt: Incomplete or ilogical notes.
  - Few-Shots Prompt: Slow API response. 
##### Final Approach
- AI21 Lab Customized Jurassic-1 Grande Model 
  - Trained a customized note generation model on the top of Jurassic-1 Grande
  - Training data comes from video transcripts from various platform such as Canvas, Youtube， TED Talks and Coursera covering various domains/subjects. In addition, English literature such as passage from William Shakespeare are included in the training data
    - Feel Free to reach out, such as in the **Discussions** or **Issues** for a more detail explanation of the training process
  - Overall better performance and lower latency from the original approach
- Hyperparameter tuning(temperature): Note taking does not require too much randomness, but low tempeature makes the notes tedious. Thus, we kept the temperature at about 0.3 to let the model be creative. 

#### Chatbot
- AI21 Lab Jurassic-1 Jumbo Model

### UI Design
#### Tools: 
  - Streamlit for implementing note generation text interface. 
  - Streamlit chatbot for Question-answering bot. 
  - Figma for logo design.
#### Layout: 
- For the two main features of our application, we let the major feature, the text input and note area, to cover most upper area of the main page; we then put Chatbox below it as an auxiliary feature.
#### Logo: 
- The three parts of the logo match "i", "Note", and "It" respectively. This AI note generation project reminds us of how people took note in the ancient China with writing brush, when writing took so much efforts and preparations. Not only have "i" changed from human to A"I", but the writing brush we used for "N"ote have changed to copy paste and click. We are excited about how AI will bring more convenience to other aspects of human lives, just like how the way we take notes can be revolutionlized by AI. 



