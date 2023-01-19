import re
class PostProcessor:
    """_summary_
    """
    def __init__(self):
        """_summary_
        """
        pass

    def process_text(self, text):
        """ Post Process the bullet points text completion generated by the custom language model to suit the format of a markdown file

        Args:
            text (str): generated bullet points completion text

        Returns:
            str: post processed text
        """

        new_text = ""
        for char in text:
            if char == '-': 
                new_text += '- '
            elif char == ' ': 
                new_text += '  '
            else: 
                new_text += char
        return new_text

# text = "-Deep learning is scalable machine learning\n -Classical machine learning is more dependent on human intervention\n -Artificial neural networks are comprised of node layers\n-Artificial neurons have associated weights and thresholds\n-Output of any individual node is above specified threshold to activate it\n-Artificial neural networks are credited with accelerating progress in areas such as computer vision, natural language processing, and speech recognition "
# a = PostProcessor()
# print(a.process_text(text))