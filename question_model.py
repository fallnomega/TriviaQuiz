import random
import data

class Question:
    def __init__(self):
        self.list_of_questions = []
        for x in data.question_data:
            self.list_of_questions.append(x)
        self.selection = random.choices(self.list_of_questions)
        self.question = self.selection[0]['text']
        self.answer = self.selection[0]['answer']



