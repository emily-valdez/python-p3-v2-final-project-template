# lib/cli.py

from helpers import (
    exit_program,
    question_list,
    helper_2
)

def main():
    menu() 
    while True:
        
        choice = input("> ")
        if choice == "2":
            exit_program()
        elif choice == "1":
            helper_1()
        elif choice == "0":
            helper_2()
        else:
            print("Invalid option.")


def menu():
    print("Welcome! to Holiday family dinners. In true holiday fashion, your loved ones want updates on your life. Take a seat at the dining table, and get ready for a round of rapid-fire questions! For each question, select a recommended response, or redirect the conversation to the food. Once you have made it through all of the questions, your reward awaits…")
    
    print("1. Get a list of all the Questions ")
    print("2. Get a list of all the Answers")
    print("3. Find specific question by ID")
    print("4. Find specific answer by ID")
    print("5. Create new question")
    print("6. Create new answer")
    print("7. Delete a question")
    print("8. Delete a answer")
    print("9. Exit the dinner ")
    print("10. No capacity for an inquisition? It happens to all of us. Build a plate to-go instead")




if __name__ == "__main__":
    main()
