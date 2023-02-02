from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from art import logo

list_of_questions = []
for question in question_data:
    list_of_questions.append(Question(question['question'], question['correct_answer']))

the_brain = QuizBrain(list_of_questions)

print(logo)

while the_brain.still_has_questions():
    the_brain.next_question()
print("You've completed the quiz")
print(f"Total answered correctly: {the_brain.score}/{the_brain.question_number}")
