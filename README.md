<p align="center">
<img src="assets/logo.png" width="300" height="350" />
</p>


[![Presentation](http://img.youtube.com/vi/ptGuxOxiN30/maxresdefault.jpg)](https://youtu.be/ptGuxOxiN30 "Video Title")


## i-Note-It: Enhanced Note-Taking Experience with Artificial Intelligence
![GitHub](https://img.shields.io/github/license/zslrmhb/i-Note-It)
![GitHub Repo stars](https://img.shields.io/github/stars/zslrmhb/i-Note-It)
![GitHub forks](https://img.shields.io/github/forks/zslrmhb/i-Note-It)
![GitHub watchers](https://img.shields.io/github/watchers/zslrmhb/i-Note-It)

<!-- toc -->
- [Latest Features](#latest-features)
- [How to use?](#how-to-use)
  - [Web Streamlit Demo](#web-streamlit-demo)
  - [Local Streamlit Demo](#local-streamlit-demo)
    - [Prerequisites](#prerequisites)
    - [Steps](#steps)
      - [Environment Configuration](#environment-configuration)
        - [Recommended (For Win64 Platform Only, Unfortunately)](#recommended-for-win64-platform-only-unfortunately)
        - [Alternative](#alternative)
      - [config.py](#configpy)
- [Behind the Scene](#behind-the-scene)
  - [Language Model](#language-model)
    - [Note Generation](#note-generation)
      - [Original Approach](#original-approach)
      - [Final Approach](#final-approach)
    - ["Hyperparameter" Tuning](#hyperparameter-tuning)
    - [Chatbot](#chatbot)
  - [UI Design](#ui-design)
    - [Tools:](#tools)
    - [Layout:](#layout)
    - [Logo:](#logo)
- [Future Plans and Improvements](#future-plans-and-improvements)


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
| Tool | Version/Link|
| --- | --- |
| Python | 3.7 - 3.10 (The demo sues Python 3.9) |
| Streamlit | https://github.com/streamlit/streamlit |
| st-chat | https://github.com/AI-Yash/st-chat |
| AI21 Studio API Key | https://docs.ai21.com/ |


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
- You are going to set it up in your local environment, here is how:
  1. Once you have done all the steps above(Configured the environment), go to your cloned repository.
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
- Prompt Engineering (Jurassic-1 Grande Model)
  - Zero-Shot Prompt
    - Simply asking the model to generate note without providing examples 
    - Worse Performance, give illogical and inconsistent outputs
  - Few-Shots Prompt
    - Asking the model to generate note by providing it with few examples
    - Better than the zero-shot prompt, but have a higher latency
##### Final Approach
- AI21 Lab Customized Jurassic-1 Grande Model 
  - Trained a customized note generation model on the top of Jurassic-1 Grande
  - Training data comes from video transcripts from various platform such as Canvas, Youtube，TED Talks and Coursera covering various domains/subjects. In addition, English literature such as passage from William Shakespeare are included in the training data
    - Feel Free to reach out, such as in the **Discussions** or **Issues** for a more detail explanation of the training process
  - Overall better performance and lower latency from the original approach

#### "Hyperparameter" Tuning
- Note taking does not require too much randomness, but low temperature makes the notes tedious. Thus, we kept the temperature at about 0.3 to let the model be creative. We also tuned max-token of the model to optimize for best note generation result

#### Chatbot
- AI21 Lab Jurassic-1 Jumbo Model
  - Use 3 instructions as prompt, see [notebot.py](scripts/notebot.py)
  - Feed the input transcript as the *Context* for the Question *Inquiry*

### UI Design
#### Tools 
  - Streamlit for implementing note generation text interface. 
  - Streamlit chatbot for Question-answering bot. 
  - Figma for logo design.
#### Layout 
- For the two main features of our application, we let the major feature, the text input and note area, to cover most upper area of the main page; we then put Chatbot below it as an auxiliary feature.
#### Logo
- The three parts of the logo match "i", "Note", and "It", respectively. This AI note generation idea reminds us of how people took note in the ancient China with writing brush, which required so much efforts and preparations. Now, not only have "i" changed from human to A"I", but the writing brush we used for "N"ote have changed to keyboard. We are excited about how AI will bring more convenience to other aspects of human lives, just like  the way we take notes can be revolutionized by AI, and just like the way this logo design was inspired by ideas from Stable Diffusion. 

### Future Plans and Improvements
- Domain-Specific Note Generation
- Accept larger input size for note generation
  - Slice the input into chunks to make note generation more efficient
- Accept input other than text for note generation
  - Audio
  - Video 
  - Web URL
  - ...
- User-Specific Note-Taking Model
- Multiple Platform
- And much more!!!
