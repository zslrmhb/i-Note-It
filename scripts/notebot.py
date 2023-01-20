from config import NOTEBOT_MODEL_URL, API_TOKEN

import requests

class NoteBot():
    def __init__(self):
        """_summary_

        Args:
            instruction (_type_, optional): _description_. Defaults to None.
        """
        self.instruction1 = "Context: "
        self.instruction2 = "\nQuestion: "
        self.instruction3 = "\nAnswer: "



    def get_response(self, transcript, question, to_json=True):
        """_summary_

        Args:
            transcript (_type_): _description_
            question (_type_): _description_
        """
        payload = {
                    "prompt": f"{self.instruction1}{transcript}{self.instruction2}{question}{self.instruction3}",
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
                    "stopSequences":["↵"]
                }
        headers = {
                    "accept": "application/json",
                    "content-type": "application/json",
                    "Authorization": "Bearer {TOKEN}".format(TOKEN=API_TOKEN)
               }
        response = requests.post(NOTEBOT_MODEL_URL, json=payload, headers=headers)

        if to_json:
            return response.json()
        else:
            return response

    def run(self, transcript, question, to_json=True, get_text=True):
        """_summary_

        Args:
            input_text (_type_): _description_
            to_json (bool, optional): _description_. Defaults to True.

        Returns:
            _type_: _description_
        """
        if get_text:
            return self.get_response(transcript, question, to_json)['completions'][0]['data']['text']
        else:
            return self.get_response(transcript, question, to_json)

        