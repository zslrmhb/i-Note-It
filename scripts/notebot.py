from config import NOTEBOT_MODEL_URL, API_TOKEN

import requests

class NoteBot():
    """ i-Note-it NoteBot
    """
    def __init__(self):
        """init
        """
        self.instruction1 = "Context: "
        self.instruction2 = "\nQuestion: "
        self.instruction3 = "\nAnswer: "

    def get_response(self, transcript, question, to_json=True):
        """ Get NoteBot Model Response

        Args:
            transcript (str): input transcript
            question (str): question to ask
            to_json (bool, optional): convert to json format. Defaults to True.

        Returns:
            dict or str:  to_json=True -> dict, to_json=False -> str
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
        """ Run the Model

        Args:
            transcript (str): input transcript
            question (str): question to ask
            to_json (bool, optional): convert to json format. Defaults to True.
            get_text (bool, optional): Get the model completion response. Defaults to True.

        Returns:
            str or dict: get_text=True -> str, get_text=False -> dict
        """
        if get_text:
            return self.get_response(transcript, question, to_json)['completions'][0]['data']['text']
        else:
            return self.get_response(transcript, question, to_json)  