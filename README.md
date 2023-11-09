# Phase 3 CLI+ORM Project: Holiday Table

#### Made with :white_heart: by Kassidy Matos, Tom Golebiewski, and Emily Valdez

---

## Introduction
:snowflake: :snowflake: :snowflake: Welcome to the Holidays!!! :snowflake: :snowflake: :snowflake:

In true holiday fashion, your loved ones want updates on your life. Take a seat at the dining table, and get ready for a round of rapid-fire questions! For each question, select a recommended response, or redirect the conversation to the food. If you are not in the mood to be questioned, you can exit the dinner by selecting option 11.

---

### The directory structure for this project:

```console
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── answers.py
    │   └── config.py
    │   └── questions.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```
---

### Generating The Environment

Run the following commands to set up the environment:

```console
pipenv install
pipenv shell
```

---

## Holiday Table CLI
Note: In your terminal, run the CLI with `python lib/cli.py`

Our CLI prompts the user with questions they might encounter at a holiday gathering. The main menu welcomes the user to the holiday table, then lists the options available for the user to interact with. 

* Option 1 allows the user to see all the questions they will be asked at the holiday gathering.
* Option 2 shows a list of all of the answer choices the user can respond with.
* Option 3 lets the user navigate to a specific question by typing in the question id.
* Option 4 lets the user navigate to a specific answer choice by typing in its id.
* Option 5 gives the user the ability to create their own question.
* Option 6 gives the user the ability to create their own answer.
* Option 7 lets the user delete a question by entering its id.
* Option 8 lets the user delete an answer by entering its id.
* Option 9 displays all related questions to the input answer text.
* Option 10 displays all related answers to the input question id.
* Option 11 allows the user to exit the program.

--- 

## Questions

The `questions` model begins with the constructor function, initializing a question and id. The default id is "None". The `__repr__` method is used to format the questions. Next, we have included an `all` function which selects all questions from the questions table in the database. The `from_db` method retrieves a question instance by its id. `Delete` retrieves a question by its id and performs a delete to remove this question from the database. `Save` will insert into the database the question created by the user and allow it to persist. The `create` method creates a new question. `find_by_id` fetches a specific question from the table using its id. `find_related_answers` retrieves all answers related to a given question by its id. Lastly, there is a question property that raises an error if the user enters an empty string.


---

## Answers

Much like the previous model, `answers` begins with the constructor function, initializing a response and its id. The default id is "None". The `__repr__` method is used to format the answers / responses. Next, we have included an `all` function that selects all answers from the answers table in the database. The `from_db` method retrieves an answer instance by its id. `Delete` finds the answer by its id and performs a delete to remove this answer from the database. `Save` will insert into the database the answer created by the user and allow it to persist. The `create` method creates a new answer. `find_by_id` fetches a specific answer from the table using its id. `find_related_questions` retrieves all questions related to a given answer. Lastly, there is an answer property that raises an error if the user enters an empty string.
