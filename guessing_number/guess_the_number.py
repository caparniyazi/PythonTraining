import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5


def get_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    elif user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")
        return None


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    # print(f"The correct answer is {answer}")

    turns = get_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the  number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses. You lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()
