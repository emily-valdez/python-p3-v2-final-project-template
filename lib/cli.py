# lib/cli.py

from helpers import (
    exit_program,
    helper_1,
    helper_2
)

from lib.models.answers import Answer
from lib.models.questions import Question

def main():
    while True:
        menu()
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
    print("Welcome to the Holidays! Please select an option:")
    print("0. Holiday Dishes")
    print("1. Recommended Responses")
    print("2. The baby is tired -- gotta go!")


if __name__ == "__main__":
    main()
