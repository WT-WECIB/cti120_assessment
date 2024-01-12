import random
import time
import threading

# List of sample variable names, some are valid and others are not
sample_variable_names = {
    "var1": "v",
    "1var": "i",
    "_myvar": "v",
    "my var": "i",
    "my_var": "v",
    "for": "i",
    "helloWorld": "v",
    "True": "i",
    "none": "v",
    "try": "i",
    "var_123": "v",
    "123var": "i",
    "my-var": "i",
    "var!": "i",
    "varName": "v",
    "if": "i",
    "elif": "i",
    "else": "i",
    "while": "i",
    "break": "i",
    "lambda": "i",
    "pass": "i",
    "import": "i",
    "from": "i",
    "as": "i"
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


def quiz_question(variable_name, correct_answer):
    global user_answer
    input_with_timeout(
        f"Is '{variable_name}' a valid Python variable name? (Type 'v' for valid, 'i' for invalid): ",
        5)
    return user_answer is not None and user_answer.lower() == correct_answer.lower()


def start_quiz():
    print("Welcome to the Python Variable Name Quiz!")
    print(
        "You will be presented with 25 names. For each, indicate if it's a valid ('v') or invalid ('i') Python variable name.")
    print("You have 5 seconds to answer each question.")
    print(
        "Type 'v' for valid or 'i' for invalid and press Enter. The quiz will automatically proceed to the next question after 5 seconds.")
    print("Let's get started! Press Enter to begin the quiz.")
    input()

    questions = random.sample(list(sample_variable_names.items()), 25)
    score = 0

    for variable_name, correct_answer in questions:
        if quiz_question(variable_name, correct_answer):
            print("Correct!")
            score += 1
        else:
            print(
                f"Wrong! The correct answer was {'Valid' if correct_answer == 'v' else 'Invalid'}.")

        input("Press Enter to continue to the next question...")
        print()

    print(f"Quiz finished! Your score: {score}/25")


if __name__ == "__main__":
    start_quiz()
