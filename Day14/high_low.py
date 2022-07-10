import random
from data import data
from art import logo, vs
from replit import clear


def random_account():
    return random.choice(data)

def check_answer(a_followers, b_followers, guess):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def format(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}"

def game(): 
    print(logo)
    continue_game = True
    score = 0
    account_a = random_account()
    account_b = random_account()

    #Make sure there's not anu duplicate accounts


    while continue_game:
        account_a = account_b
        account_b = random_account()

        while account_a == account_b:
            account_b = random_account()

        print(f"Compare A: {format(account_a)}")
        print(vs)
        print(f"Against B: {format(account_b)}")  

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()  

        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]

        is_correct = check_answer(a_followers, b_followers, guess)
        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You are right! Current score: {score}")
        else:
            continue_game = False
            print(f"Sorry, that's wrong. Final score: {score}")

    
game()