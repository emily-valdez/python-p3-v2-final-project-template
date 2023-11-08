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

def question_find_byid():
    id = input('Enter the questions id:')
    question = Question.find_byid(id)
    print(question) if question else print(f'Question {id_} not found')

def answer_find_byid():
    id = input('Enter the answers id:')
    answer = Answer.find_byid(id)
    print(answer) if answer else print(f'Answer {id_} not found')

def create_question():
    question = input('Enter the question:')
    new_question = Question.create(question)
    print(f'Success: {question}')

def create_answer():
    question_id = input('Enter the question_id:')
    answer = input('Enter the answer:')
    new_answer = Answer.create(question_id, answer)
    print(f'Succes: {answer}')

def deletequestion():
    id = input('Enter the questions id:')
    if question := Question.find_byid(id):
        question.delete()
        print(f'Question {id} deleted')
    else:
        print(f'Question {id} not found')

def deleteanswer():
    id = input('Enter the answers id:')
    if answer := Answer.find_byid(id):
        answer.delete()
        print(f'Answer {id} deleted')
    else:
        print(f'Answer {id} not found')

def exit_program():
    print("Thanks for coming, Happy Holidays!")
    exit()

def exit_program():
    print("Thanks for coming, Happy Holidays!")
    exit()

def to_go_order():
    pass
