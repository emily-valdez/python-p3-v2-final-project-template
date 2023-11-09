# lib/cli.py

from helpers import (
    exit_program,
    question_list,
    answer_list,
    question_find_by_id,
    answer_find_by_id,
    create_question,
    create_answer,
    delete_question,
    delete_answer,
    find_related_question,
    find_related_answer
)

def main():
    menu() 
    while True:
        
        choice = input("> ")
        if choice == "1":
            question_list()
        elif choice == "2":
            answer_list()
        elif choice == "3":
            question_find_by_id()
        elif choice == "4":
            answer_find_by_id()
        elif choice == "5":
            create_question()
        elif choice == "6":
            create_answer()
        elif choice == "7":
            delete_question()
        elif choice == "8":
            delete_answer()
        elif choice == "9":
            find_related_question()
        elif choice == "10":
            find_related_answer()
        elif choice == "11":
            exit_program()
        else:
            print("Invalid option.")


def menu():
    print("Welcome! to Holiday family dinners. In true holiday fashion, your loved ones want updates on your life. Take a seat at the dining table, and get ready for a round of rapid-fire questions! For each question, select a recommended response, or redirect the conversation to the food. If you are not in the mood to be questioned, you can exit the dinner by selecting option 11.")
    
    print("1. Get a list of all the Questions ")
    print("2. Get a list of all the Answers")
    print("3. Find specific question by ID")
    print("4. Find specific answer by ID")
    print("5. Create new question")
    print("6. Create new answer")
    print("7. Delete a question")
    print("8. Delete a answer")
    print("9. Find related questions")
    print('10. Find related answers')
    print("11. Exit the dinner ")
    




if __name__ == "__main__":
    main()
