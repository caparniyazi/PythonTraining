"""
The objective is simple: guess which of the two accounts shown has higher followers.
If you get the answer correct, a new account will appear and simply guess again
which you think is higher.
Every game has (almost) infinite questions so try your best to get a high score streak.
"""
import random

from art import logo
from art import vs
from game_data import data


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc} from, {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Take the user's guess and the followers count and returns true if they got it right."""

    if user_guess == "A":
        return a_followers > b_followers
    else:
        return b_followers > a_followers


print(logo)
# Keep score
score = 0
should_continue = True
account_b = random.choice(data)

while should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        # Regenerate account b if account a and account b happen to be the same.
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    # Clear the screen
    print("\n" * 20)
    print(logo)

    # Check the follower accounts for each
    a_follower_count = int(account_a["follower_count"])
    b_follower_count = int(account_b["follower_count"])
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give feedback.
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        should_continue = False
