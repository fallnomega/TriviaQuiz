# TODO checking if the answer was correct
# TODO checking if we're at the end of the quiz
import random


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list

    def nextQuestion(self):
        self.question_number += 1
        self.index_choice = random.randint(0, len(self.questions_list) - 1)
        print(self.index_choice)
        self.question = self.questions_list[int(self.index_choice)]
        # print(type(self.index_choice))
        # print(type(self.questions_list))
        # self.questions_list.remove(9)
        # print(len(self.questions_list))
        # print(self.question)
        # exit()
        self.answer = input(f"Q{self.question_number}. {self.question['text']} (True/False) - : ").lower()
        if self.answer != 'true' and self.answer != 'false':
            print("Please answer with True or False")
        else:
            self.checkAnswer()
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)


    def checkAnswer(self):
        if self.answer == self.question['answer'].lower():
            print(f"\nCorrect, the answer is: {self.answer}")

        else:
            print(f"\nWrong, the correct answer is: {self.question['answer'].lower()}")
