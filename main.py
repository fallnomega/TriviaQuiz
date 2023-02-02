import random
import data
from question_model import Question
from quiz_brain import QuizBrain
from art import logo

list_of_questions =[]
for x in data.question_data:
    list_of_questions.append(x)
the_brain = QuizBrain(list_of_questions)
# print(list_of_questions)
# print (the_brain.questions_list)
print(logo)
the_brain.askQuestion()

# selected_question = random.choices(list_of_questions)
# selected = Question(selected_question[0]['text'],selected_question[0]['answer'])
# print(selected.question)
# print(selected.answer)
#
# print ("\n\n\n")
# print(selected_question.list_of_questions)
# print(random.choices(selected_question.list_of_questions))