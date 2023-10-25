# lib/helpers.py

from models.answers import Answer
from models.questions import Question

def question_list():
    questions = Question.all()

    while True:
        for idx, question in enumerate(questions, 1):
            print(f"{idx}. {question}")

        selected_question_number = int(input("Enter the number of the question to start some holiday Q&A (or enter 0 to exit): "))

        if selected_question_number == 0:
            print("Exiting the question list back to main menu...")
            break

        if 1 <= selected_question_number <= len(questions):
            selected_question = questions[selected_question_number - 1]

            answers = Answer.all()
            answers_for_question = [answer for answer in answers if answer.question_id == selected_question.id]

            if answers_for_question:
                print(f"One of your family members has asked you: '{selected_question}':")
                for answer in answers_for_question:
                    print(answer)

                selected_answer = int(input("Enter your selected answer (enter 0 to skip): "))

                if selected_answer > 0:
                    print("Congrats on making it through an intrusive family member's questions! Your reward is food! Here is your to-go box <3 ")

            else:
                print(f"No answers found for question '{selected_question}'.")

            continue_option = input("If you feel inclined to stay and hang with the family longer, enter 'continue' to begin the questions and answer game again: ")
            if continue_option.lower() == "continue":
                continue
            else:
                print("Thanks for playing! Exiting the program...")
                break

def answer_list():
    answers = Answer.all()
    for answers in answers:
        print(answers)

def question_find_by_id():
    id = input('Enter the questions id:')
    question = Question.find_by_id(id)
    print(question) if question else print(f'Question {id} not found')

def answer_find_by_id():
    id = input('Enter the answers id:')
    answer = Answer.find_by_id(id)
    print(answer) if answer else print(f'Answer {id} not found')

def create_answer():
    question_id = input('Enter the question_id:')
    answer = input('Enter the answer:')

    try:
        question_id = int(question_id)
        new_answer = Answer.create(question_id, answer)
        print(f'Success: {new_answer}')
    except ValueError:
        print('Invalid question_id. Please enter a valid number.')

def create_question():
   while True:
        question = input('Enter the question:')
    
        if question.strip():
            try:
                new_question = Question.create(question)
                print(f'Success: {new_question}')
                break  
            except ValueError as e:
                print(f'Error: {e}')
        else:
            print('Error: The question cannot be empty. Please try again.')
    

def delete_question():
    id = input('Enter the questions id:')
    if question := Question.find_by_id(id):
        question.delete()
        print(f'Question {id} deleted')
    else:
        print(f'Question {id} not found')

def delete_answer():
    id = input('Enter the answers id:')
    if answer := Answer.find_by_id(id):
        answer.delete()
        print(f'Answer {id} deleted')
    else:
        print(f'Answer {id} not found')

def exit_program():
    print("Thanks for coming - Happy Holidays!")
    exit()

def find_related_answer():
    question_id = input('Enter the question_id for which you want to find related answers:')
    related_answers = Question.find_related_answers(question_id)

    if related_answers:
        for answer in related_answers:
            print(answer)
    else:
        print(f"No related answers found for question with ID {question_id}.")

def find_related_question():
    response = input('Enter the response to find the associated question: ')
    related_question = Answer.find_related_questions(response)

    if related_question:

        print(f"Related question: {related_question}")
    else:
        print(f"No related question found for the response.")
