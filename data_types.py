import random
import time
import threading

# Expanded list of sample variables
sample_variables = {
    "5": "int",
    "5.0": "float",
    "'Hello'": "str",
    "True": "bool",
    "[1, 2, 3]": "list",
    "(1, 2, 3)": "tuple",
    "{1, 2, 3}": "set",
    "{'a': 1, 'b': 2}": "dict",
    "None": "NoneType",
    "'a'": "str",
    "3.14": "float",
    "False": "bool",
    "[True, False]": "list",
    "{'key': 'value'}": "dict",
    "(False,)": "tuple",
    "set([1, 2])": "set",
    "10": "int",
    "'Python'": "str",
    "[5, 'hello', True]": "list",
    "{'x': 10, 'y': 20}": "dict",
    "(4.5, 3.2)": "tuple",
    "{5.5, 6.6}": "set",
    "'c'": "str",
    "20.0": "float",
    "['a', 'b', 'c']": "list"
}

# Global variable to store user's answer
user_answer = None


def input_with_timeout(prompt, timeout):
    def timer_expired():
        global user_answer
        print("\nTime's up!")
        user_answer = None

    print(prompt, end='', flush=True)
    timer = threading.Timer(timeout, timer_expired)
    timer.start()
    global user_answer
    user_answer = input()
    timer.cancel()


def quiz_question(variable, correct_answer):
    global user_answer
    input_with_timeout(f"What is the data type of {variable}? Answer: ", 5)
    return user_answer is not None and user_answer.lower() == correct_answer.lower()


def start_quiz():
    print("Welcome to the Python Data Types Quiz!")
    print(
        "You will be asked 25 questions about the data types of different Python variables.")
    print("You have 5 seconds to answer each question.")
    print(
        "Type your answer and press Enter. Acceptable answers are: 'int', 'float', 'str', 'bool', 'list', 'tuple', 'set', 'dict', 'NoneType'.")
    print(
        "The quiz will automatically proceed to the next question after 5 seconds.")
    print("Let's get started! Press Enter to begin the quiz.")
    input()

    questions = random.sample(list(sample_variables.items()), 25)
    score = 0

    for variable, correct_answer in questions:
        if quiz_question(variable, correct_answer):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")

        input("Press Enter to continue to the next question...")
        print()

    print(f"Quiz finished! Your score: {score}/25")


if __name__ == "__main__":
    start_quiz()
