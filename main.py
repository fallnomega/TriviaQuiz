import random

from question_model import Question
import quiz_brain




selected_question = Question()
print(selected_question.question)
print(selected_question.answer)

print ("\n\n\n")
print(selected_question.list_of_questions)
print(random.choices(selected_question.list_of_questions))