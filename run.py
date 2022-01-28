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
        "question": "What does “www” stand for in a website browser?",
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


def get_name():
    name = input("Enter your name: ")

    print("Welcome", name, "to The Brainy Maze!")


def get_question():
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


def check_ans(question, answer, attempts, score):
    if quiz[question]['answer'].lower() == answer.lower():
        print(f"Correct Answer! \n Your score is {score + 1}!")
        return True
    else:
        print(f"Wrong Answer :( \nYou have {attempts -1} left! \nTry again...")
        return False


def main():
    name = get_name()
    question = get_question()
    check = check_ans()


main()
