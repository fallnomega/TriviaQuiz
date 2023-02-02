class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q{self.question_number}. {question.question} (True/False) - : ").lower()
        if answer != 'true' and answer != 'false':
            print("Please answer with True or False")
        else:
            self.check_answer(answer, question)

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, answer, question):
        if answer == question.answer.lower():
            print(f"\nYou got it right!")
            self.score += 1
        else:
            print(f"\nWrong")
        print(f"The correct answer is: {question.answer.lower()}")
        print(f"Your current score is {self.score}/{self.question_number}\n")
