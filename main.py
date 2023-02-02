from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from art import logo

list_of_questions = []
for question in question_data:
    list_of_questions.append(Question(question['text'], question['answer']))

the_brain = QuizBrain(list_of_questions)

print(logo)

while the_brain.still_has_questions():
    the_brain.next_question()

print(f"Total answered correctly: {the_brain.score}")
