logo = """
 ██████  ██    ██ ███████ ███████ ███████     ████████ ██   ██ ███████     ███    ██ ██    ██ ███    ███ ██████  ███████ ██████  
██       ██    ██ ██      ██      ██             ██    ██   ██ ██          ████   ██ ██    ██ ████  ████ ██   ██ ██      ██   ██ 
██   ███ ██    ██ █████   ███████ ███████        ██    ███████ █████       ██ ██  ██ ██    ██ ██ ████ ██ ██████  █████   ██████  
██    ██ ██    ██ ██           ██      ██        ██    ██   ██ ██          ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██      ██   ██ 
 ██████   ██████  ███████ ███████ ███████        ██    ██   ██ ███████     ██   ████  ██████  ██      ██ ██████  ███████ ██   ██   
  """

import random
from replit import clear


#life function
def life(level):
    if level == "easy":
        life = 10
    elif level == "hard":
        life = 5
    return life


#guess comparison:
def compare(guess, number):
    high = guess - number
    low = number - guess
    if high >= 5:
        print("Too High")
    elif high > 0:
        print("High")
    elif low >= 5:
        print("Too Low")
    elif low > 0:
        print("Low")
    else:
        print(f"You got it! The answer was {number}.")


#play again
play = "y"
while play == "y":
    #choosing a random number
    clear()
    number = random.choice(range(1, 100))
    print(logo)
    print("""
  Welcome to the Number Guessing Game!
  I'm thinking of a number between 1 and 100.
  """)
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    life = life(level)
    guess = 0
    while life != 0 or number != guess:
        if life == 0:
            print(
                f"You've run out of guesses, you lose. The answer was {number}."
            )
            break
        else:
            print(f"You have {life} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            life -= 1
            if guess == number:
                print(f"You got it! The answer was {number}.")
                break
            else:
                compare(guess, number)
                print("Guess again.")
    play = input("Do you want to play again?? Type 'Y' or 'N': ").lower()
