# lib/helpers.py

from models.answers import Answer
from models.questions import Question

def question_list():
    questions = Question.all()

    for idx, question in enumerate(questions, 1):
        print(f"{idx}. {question}")

    selected_question_number = int(input("Enter the number of the question to choose to start some holiday Q&A: "))

    if 1 <= selected_question_number <= len(questions):
        selected_question = questions[selected_question_number - 1]
        
        answers_for_question = [answer for answer in Answer.all() if answer.question_id == selected_question.id]

        if answers_for_question:
            print(f"One of your family members has asked you: '{selected_question}':")
            for answer in answers_for_question:
                print(answer)

    #         # print(f"No answers found for question '{selected_question}'.")
    #         # create_option = input("Would you like to create a new answer for this question? (yes/no): ")
    #         # if create_option.lower() == "yes":
    #         #     create_answer(selected_question.id)
    # else:
    #     print("Invalid question number. Please try again.")

def answer_list():
    answers = Answer.all()
    for answer in answers:
        print(answers)
        return

def question_find_by_id():
    id = input('Enter the questions id:')
    question = Question.find_byid(id)
    print(question) if question else print(f'Question {id} not found')

def answer_find_by_id():
    id = input('Enter the answers id:')
    answer = Answer.find_byid(id)
    print(answer) if answer else print(f'Answer {id} not found')

def create_question():
    question = input('Enter the question:')
    new_question = Question.create(question)
    print(f'Success: {new_question}')

@classmethod
def create_answer():
    question_id = input('Enter the question_id:')
    answer = input('Enter the answer:')
    new_answer = Answer.create(question_id, answer)
    print(f'Success: {new_answer}')

def delete_question():
    id = input('Enter the questions id:')
    if question := Question.find_byid(id):
        question.delete()
        print(f'Question {id} deleted')
    else:
        print(f'Question {id} not found')

def delete_answer():
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
