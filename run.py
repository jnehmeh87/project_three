import time


quiz = {
    1: {
        "question": "How many colors are in the LGBTQ rainbow flag?",
        "answer": "6"
    },
    2: {
        "question": "What is the biggest capital in the EU?",
        "answer": "Berlin"
    },
    3: {
        "question": "What is the real name of Superman?",
        "answer": "Clark Kent"
    },
    4: {
        "question": "What does 'www' stand for in a website browser?",
        "answer": "World Wide web"
    },
    5: {
        "question": "How many languages are written from right to left?",
        "answer": "12"
    },
    6: {
        "question": "What type of animal is a Flemish giant?",
        "answer": "Rabbit"
    },
    7: {
        "question": "Which animal can be seen on the Porsche logo?",
        "answer": "Horse"
    },
    8: {
        "question": "Who was the 1st woman pilot to fly across the Atlantic?",
        "answer": "Amelia Earhart"
    },
    9: {
        "question": "What was the first soft drink in space?",
        "answer": "Coca Cola"
    },
    10: {
        "question": "What is the most consumed hot drink in the world?",
        "answer": "Tea"
    },
    11: {
        "question": "How many teeth does an adult human have?",
        "answer": "32"
    },
    12: {
        "question": "What sport is dubbed the 'king of sports'?",
        "answer": "Soccer"
    },
    13: {
        "question": "Who does the wolf dress up as,in little red riding hood?",
        "answer": "Grandmother"
    },
    14: {
        "question": "Who is the patron saint of Ireland?",
        "answer": "St Patrick"
    },
    15: {
        "question": "What color is a ruby?",
        "answer": "Red"
    },
    16: {
        "question": "In what type of matter are atoms most tightly packed?",
        "answer": "Solids"
    },
    17: {
        "question": "What is the loudest animal on Earth?",
        "answer": "Sperm Whale"
    },
    18: {
        "question": "The unicorn is the national animal of which country?",
        "answer": "Scotland"
    },
    19: {
        "question": "How many legs does a spider have?",
        "answer": "8"
    },
    20: {
        "question": "What is the nearest planet to the sun?",
        "answer": "Mercury"
    }
}


def start_game():
    """
    Get the name of the player and welcome them and describe the game.
    """
    validName = False
    while not validName:
        name = input("Hi there! Please enter your name: \n")
        if len(name.strip()) > 0:
            validName = True
        else:
            print("Please enter your name!\n")

    print("\nWelcome", name, "to The Brainy Maze!\n")
    print("Test your knowledge by answering 20 questions\n")
    print("If you failed to answer right, you have 3 attempts\n")
    print("Answer more to get a higher score!\n")
    time.sleep(2)
    get_question()


def get_question():
    """
    Get the questions from the quiz dictionary and set the score to 0
    also create input for answer. Add score or remove attempts function
    """
    score = 0

    for question in quiz:
        attempts = 3

        while attempts > 0:
            print(quiz[question]['question'])

            answer = input("Enter Answer: ")

            check = check_ans(question, answer, attempts, score)
            if check:
                score += 1
                break
            attempts -= 1
        else:
            print("Game over!\n")
            print(f"Your score is: {score}!\n")
            break
    end_game()


def check_ans(question, answer, attempts, score):
    """
    Get the answer from quiz dictionary and compare it with the user input
    Add one point to the score and give 2 attempts
    """
    if quiz[question]['answer'].lower() == answer.lower():
        print(f"\nCorrect Answer! \nYour score is {score + 1}!\n")
        print("Great Job!\n")
        print("\n")
        return True
    else:
        print(f"\nWrong! \nYou have {attempts -1} attempt(s) left!\n")
        return False


def end_game():
    """
    End the Game and give the finale score
    """
    validChoice = False
    while not validChoice:
        choice = input("\nDo you want to play again? (Y/N)\n")
        if choice.lower() == "y":
            print("\n")
            get_question()
            validChoice = True
        elif choice.lower() == "n":
            print("Thanks for playing!")
            validChoice = True
        else:
            print("That is not a valid option!\n")


def main():
    """
    Run all program functions
    """
    start_game()


main()
