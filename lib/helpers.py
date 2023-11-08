# lib/helpers.py

from models.answers import Answer
from models.questions import Question

def question_list():
    questions = Question.all()
    for question in questions:
        print(question)

def answer_list():
    answers = Answer.all()
    for answers in answers:
        print(answers)
        return

def question_find_by_id():
    pass

def answer_find_by_id():
    pass

def create_question():
    pass

def create_answer():
    pass

def delete_question():
    pass

def delete_answer():
    pass

def exit_program():
    print("Thanks for coming, Happy Holidays!")
    exit()

def to_go_order():
    pass
