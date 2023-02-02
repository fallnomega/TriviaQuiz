class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list

    def nextQuestion(self):
        self.question = self.questions_list[self.question_number]
        self.question_number += 1
        self.answer = input(f"Q{self.question_number}. {self.question.question} (True/False) - : ").lower()
        if self.answer != 'true' and self.answer != 'false':
            print("Please answer with True or False")
        else:
            self.checkAnswer()

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def checkAnswer(self):
        if self.answer == self.question.answer.lower():
            print(f"\nCorrect, the answer is: {self.answer}")
        else:
            print(f"\nWrong, the correct answer is: {self.question.answer.lower()}")
