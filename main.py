import random
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from art import logo
#
list_of_questions = []
for question in question_data:
    list_of_questions.append(Question(question['text'],question['answer']))
# for x in list_of_questions:
#     print (x.question)
# print(list_of_questions)

the_brain = QuizBrain(list_of_questions)
# print(list_of_questions.)
# # print (the_brain.questions_list)
# # print(logo)
#
# game_on = True
# while game_on:
#     the_brain.nextQuestion()



