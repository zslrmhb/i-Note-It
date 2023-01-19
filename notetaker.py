from config import API_TOKEN, NOTETAKER_MODEL_URL
import requests


class NoteTaker:
    """_summary_
    """
    def __init__(self, instruction=None):
        """_summary_
        """
        if instruction == None:
            self.instruction = "Imagine you are the best notetaker in the world. Write the most streamlined and hierarchical bullet point notes with sections for this text:\n"
        else: 
            self.instruction = instruction

    def request_note(self, input_text, to_json=True):
        """

        Args:
            input_text (_type_): _description_
        """
        payload = {
                    "prompt": f"{self.instruction}{input_text}",
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
                    "Authorization": "Bearer {TOKEN}".format(TOKEN=API_TOKEN)
                }

        response = requests.post(NOTETAKER_MODEL_URL, json=payload, headers=headers)

        if to_json:
            return response.json()
        else:
            return response

    def run(self, input_text, to_json=True):
        """_summary_

        Args:
            input_text (_type_): _description_
            to_json (bool, optional): _description_. Defaults to True.

        Returns:
            _type_: _description_
        """
        if to_json:
            return self.request_note(input_text, to_json)['completions'][0]['data']['text']
        else:
            return self.request_note(input_text, to_json)



# input_text = "Hello everyone. Welcome to Math 13, a place. You might notice I just locked in. I teach right before this. So if I am ever late, I, I don't think I will be, but if I ever am just wait a few minutes and probably just delayed by my previous class. So my name is Brandon Seward. I'd prefer you just told me Brandon. My pronouns, are they them? Or you can say he him if you prefer.\n##\n"

# NoteTakingService = NoteTaker()
# print(NoteTakingService.run(input_text))