from project import ask_question, feedback, calculate_score
import pytest

def test_ask_question():
    # test for invalid input from the user
    question_data = {"question": "What is the correct extension for Python files?", "options": ["a) .pi", "b) .p", "c) .py", "d) .python"], "correct_answer": "c"}

    # User input not one of the options
    user_input = lambda prompt: "cat"

    # Raise a TypeError for invalid input
    with pytest.raises(ValueError, match="Answer must be a, b, c, or d."):
        ask_question(question_data["question"], question_data["options"], user_input)


def test_feedback():
    # if correct, return True
    question_data = {"question": "Which keyword is used for functions in Python?", "options": ["a) .pi", "b) .p", "c) .py", "d) .python"], "correct_answer": "a"}
    user_answer = "a"
    assert feedback(True, user_answer, question_data["correct_answer"]) is True

    # if incorrect, return False
    question_data = {"question": "Which keyword is used for functions in Python?", "options": ["a) .pi", "b) .p", "c) .py", "d) .python"], "correct_answer": "a"}
    user_anwer = "c"
    assert feedback(False, user_answer, question_data["correct_answer"]) is False


def test_calculate_score():
    # test the score calculation- all correct
    quiz = [
    {"question": "What is the correct extension for Python files?", "options": ["a) .pi", "b) .p", "c) .py", "d) .python"], "correct_answer": "c"},
        {"question": "What does OOP stand for?", "options": ["a) other-object programming", "b) object-oriented programming", "c) object-orientation programming", "d) none of the mentioned"], "correct_answer": "b"},
        {"question": "What is the construct called for creating anonymous functions?", "options": ["a) anonymous", "b) lambda", "c) pi", "d) llama"], "correct_answer": "b"},
        {"question": "Key words such as true and false are ___.", "options": ["a) lower case", "b) UPPER CASE", "c) Capitlaized", "d) italicized"], "correct_answer": "c"},
        {"question": "Which keyword is used for functions in Python?", "options": ["a) def", "b) function", "c) define", "d) fun"], "correct_answer": "a"}
    ]
    user_answer = ["c", "b", "b", "c", "a"]

    # calling score function to calculate
    score = calculate_score(user_answer, quiz)

    # check if the calculated score matches the expected score
    assert score == 100

    # test the score calculation- some incorrect
    quiz = [
        {"question": "What is the correct extension for Python files?", "options": ["a) .pi", "b) .p", "c) .py", "d) .python"], "correct_answer": "c"},
        {"question": "What does OOP stand for?", "options": ["a) other-object programming", "b) object-oriented programming", "c) object-orientation programming", "d) none of the mentioned"], "correct_answer": "b"},
        {"question": "What is the construct called for creating anonymous functions?", "options": ["a) anonymous", "b) lambda", "c) pi", "d) llama"], "correct_answer": "b"},
        {"question": "Key words such as true and false are ___.", "options": ["a) lower case", "b) UPPER CASE", "c) Capitlaized", "d) italicized"], "correct_answer": "c"},
        {"question": "Which keyword is used for functions in Python?", "options": ["a) def", "b) function", "c) define", "d) fun"], "correct_answer": "a"}
    ]
    user_answer = ["c", "c", "d", "a", "b"] # only one is correct (first one)

    # calling score function to calculate
    score = calculate_score(user_answer, quiz)

    # check if the calculated score matches the expected score
    assert score == 20

