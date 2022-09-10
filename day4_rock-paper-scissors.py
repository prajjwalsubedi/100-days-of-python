rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

name = input("Please put your name:   ")

#Write your code below this line 👇
import random

list = [rock, paper, scissors]
computer_choice = random.choice(list)
user_choice = int(
    input("please enter 0 for rock, 1 for paper or 2 for scissors :    "))

if 0 < user_choice > 2:
    print("You typed an invalid number, you lose!")
else:
    user_choice = list[user_choice]

    print("You choosed:")
    print(user_choice)

    print("Computer Choosed:")
    print(computer_choice)

    if user_choice == rock and computer_choice == paper:
        print("""
    _   _ ____ _  _    _    ____ ____ ____ ____ 
     \_/  |  | |  |    |    |  | |  | [__  |___ 
      |   |__| |__|    |___ |__| |__| ___] |___ 
        """)
    elif user_choice == paper and computer_choice == scissors:
        print("""
    _   _ ____ _  _    _    ____ ____ ____ ____ 
     \_/  |  | |  |    |    |  | |  | [__  |___ 
      |   |__| |__|    |___ |__| |__| ___] |___ 
        """)
    elif user_choice == scissors and computer_choice == rock:
        print("""
    _   _ ____ _  _    _    ____ ____ ____ ____ 
     \_/  |  | |  |    |    |  | |  | [__  |___ 
      |   |__| |__|    |___ |__| |__| ___] |___ 
        """)
    elif user_choice == computer_choice:
        print("""
    ___  ____ ____ _ _ _ 
    |  \ |__/ |__| | | | 
    |__/ |  \ |  | |_|_| 
        """)
    else:
        print(f"YAY {name} You WON!!!")
        print("""
     /$$      /$$ /$$$$$$ /$$   /$$ /$$   /$$ /$$$$$$$$ /$$$$$$$ 
    | $$  /$ | $$|_  $$_/| $$$ | $$| $$$ | $$| $$_____/| $$__  $$
    | $$ /$$$| $$  | $$  | $$$$| $$| $$$$| $$| $$      | $$  \ $$
    | $$/$$ $$ $$  | $$  | $$ $$ $$| $$ $$ $$| $$$$$   | $$$$$$$/
    | $$$$_  $$$$  | $$  | $$  $$$$| $$  $$$$| $$__/   | $$__  $$
    | $$$/ \  $$$  | $$  | $$\  $$$| $$\  $$$| $$      | $$  \ $$
    | $$/   \  $$ /$$$$$$| $$ \  $$| $$ \  $$| $$$$$$$$| $$  | $$
    |__/     \__/|______/|__/  \__/|__/  \__/|________/|__/  |__/
    """)
