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
                    "prompt": f"{self.instruction}{input_text}\n##\n",
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

    def run(self, input_text, to_json=True, get_text=True):
        """_summary_

        Args:
            input_text (_type_): _description_
            to_json (bool, optional): _description_. Defaults to True.

        Returns:
            _type_: _description_
        """
        if get_text:
            return self.request_note(input_text, to_json)['completions'][0]['data']['text']
        else:
            return self.request_note(input_text, to_json)