#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


from random import randint
from art import logo

HARD_LEVEL = 5
EASY_LEVEL = 10
def check_answer(answer, guess, turn):
    if guess > answer:
        print("To High")
        return turn -1
    elif guess < answer:
        print("To Low")
        return turn -1

def choose_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "hard":
        return HARD_LEVEL
    elif level == "easy":
        return EASY_LEVEL
def game():
    print(logo)
    print("Choose a difficulty. Type 'easy' or 'hard':")
    print("I'm thinking of a number between 1 and 100.")

    turn = choose_difficulty()

    answer = randint(1, 101)

    guess = 0

    while guess != answer:
        print(f"You have {turn} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turn = check_answer(answer, guess, turn)

        
        if turn == 0:
            print("You've run out of guesses, you lose.")
            return
        elif turn != 0:
            print("Guess again")

game()
        