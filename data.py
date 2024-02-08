import requests
import html
from question_model import Question

API_URL = 'https://opentdb.com/api.php'

class Question_Data:

    def __init__(self):
        self.api_parameters = {"amount":25,'type':'boolean'}
        self.response = requests.get(url=API_URL, params=self.api_parameters)
        self.response.raise_for_status()
        self.question_data = self.response.json()['results']
        for data in self.question_data:
            data['question'] = html.unescape(data['question'])

    def question_bank(self) -> list:
        question_bank = []
        for question in self.question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            question_bank.append(new_question)
        return question_bank


