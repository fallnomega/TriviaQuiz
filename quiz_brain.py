#TODO asking the quesitons
#TODO checking if the answer was correct
#TODO checking if we're at the end of the quiz
import random


class QuizBrain:
    def __init__(self,q_list):
        self.question_number =0
        self.questions_list =q_list
    def askQuestion(self):
        self.question_number+=1
        self.question = random.choices(self.questions_list)
        print(f"Q{self.question_number}. True or False - {self.question[0]['text']}")