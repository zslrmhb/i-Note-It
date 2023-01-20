from config import API_TOKEN, NOTETAKER_MODEL_URL

import requests

class NoteTaker:
    """i-Note-it NoteTaker 
    """
    def __init__(self, instruction=None):
        """init

        Args:
            instruction (str, optional): Prompt for the Note Taking Model. Defaults to None.
        """
        if instruction == None:
            self.instruction = "Imagine you are the best notetaker in the world. Write the most streamlined and hierarchical bullet point notes with sections for this text:\n"
        else: 
            self.instruction = instruction

    def request_note(self, input_text, to_json=True):
        """Get NoteTaker Model Response

        Args:
            input_text (str): input transcript
            to_json (bool, optional): convert to json format. Defaults to True.

        Returns:
            dict or str:  to_json=True -> dict, to_json=False -> str
        """
        payload = {
                    "prompt": f"{self.instruction}{input_text}\n##\n",
                    "numResults": 1,
                    "maxTokens": 2048,
                    "temperature": 0.4,
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

    def run(self, input_text, to_json=True, get_text=True):
        """Run the Model

        Args:
            input_text (str): Input transcript
            to_json (bool, optional): convert to json format. Defaults to True.
            get_text (bool, optional): Get the model completion response. Defaults to True.

        Returns:
            str or dict: get_text=True -> str, get_text=False -> dict
        """
        if get_text:
            return self.request_note(input_text, to_json)['completions'][0]['data']['text']
        else:
            return self.request_note(input_text, to_json)