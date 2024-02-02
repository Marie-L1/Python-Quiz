import pyfiglet

# intro to the quiz
def print_intro():
    # create art for the title of the quiz
    quiz_art = pyfiglet.figlet_format("Python Quiz", font="bulbhead")
    print(quiz_art)

    # intro sentance for the quiz
    print("This is a test of your Python Knowledge!\n")


def main():
    # print the introduction- only once at the beginning of the quiz
    print_intro()

    # questions and answers dict
    quiz = [
        {"question": "What is the correct extension for Python files?", "options": ["a) .pi", "b) .p", "c) .py", "d) .python"], "correct_answer": "c"},
        {"question": "What does OOP stand for?", "options": ["a) other-object programming", "b) object-oriented programming", "c) object-orientation programming", "d) none of the mentioned"], "correct_answer": "b"},
        {"question": "What is the construct called for creating anonymous functions?", "options": ["a) anonymous", "b) lambda", "c) pi", "d) llama"], "correct_answer": "b"},
        {"question": "Key words such as true and false are ___.", "options": ["a) lower case", "b) UPPER CASE", "c) Capitlaized", "d) italicized"], "correct_answer": "c"},
        {"question": "Which keyword is used for functions in Python?", "options": ["a) def", "b) function", "c) define", "d) fun"], "correct_answer": "a"}
    ]

    # playing the quiz
    user_response =[]
    score = 0
    for question_data in quiz:
        user_answer = ask_question(question_data["question"], question_data["options"])
        user_response.append(user_answer)
        is_correct = user_answer == question_data["correct_answer"]
        feedback(is_correct, user_answer, question_data["correct_answer"])
        if is_correct:
            score += 1
    calculate_score(user_response, quiz) # pass the quiz into the calculate_score function


def ask_question(question, answer_options, user_input_funct=input):
    # present the question to the user
    print("---------------------")
    print(question)

    # give the user the answer options
    for option in answer_options:
        print(option)

    # get and return the user's response
    user_response = user_input_funct("Your answer: ", )

    # check if input is valid or raise error
    valid_options = [option[0].lower() for option in answer_options]
    if user_response.lower() not in valid_options:
        raise ValueError("Answer must be a, b, c, or d.")

    return user_response.lower()


def feedback(is_correct, user_answer, correct_answer):
    # Tell the user whether or not they are correct
    if is_correct:
        print("Correct answer!")
        return True
    else:
        print("Incorrect answer.")
        return False


def calculate_score(user_response, quiz):
    score = 0

    # iterate over each question and user's input
    for user_answer, question_data in zip(user_response, quiz):
        if user_answer == question_data["correct_answer"]:
            score += 1

    # calcualte the % score
    total_questions = len(quiz)
    percentage_score = (score / total_questions) * 100

    print(f"Your score: {score}/{total_questions}")

    # add message based on score
    if percentage_score == 100:
        print("Congratulations, you know your stuff!")
    else:
        print("Keep practing!")

    return percentage_score


if __name__ == "__main__":
    main()
