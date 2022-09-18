start = input(
    "Do you want to play a game of Blackjack? Type \'y\' or \'n\':  ").lower()
numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random
from replit import clear
# from ascii import logo, win, lost, draw
while start == "yes" or "y":
    clear()
    # print(logo)
    comp_numbers = []
    comp_number = random.choice(numbers)
    comp_numbers.append(comp_number)
    number = random.choice(numbers)
    comp_numbers.append(number)
    while sum(comp_numbers) <= 17:
        number1 = random.choice(numbers)
        comp_numbers.append(number1)
        if 11 in comp_numbers and sum(comp_numbers) > 21:
            comp_numbers.remove(11)
            comp_numbers.append(1)

    user_numbers = []
    user_number = random.choice(numbers)
    user_numbers.append(user_number)
    sum_user_number = 0
    user_choice = "y"
    while user_choice == "yes" or user_choice == "y" and sum_user_number <= 21:
        user_number = random.choice(numbers)
        user_numbers.append(user_number)
        print(user_numbers)
        if 11 in user_numbers and sum(user_numbers) > 21:
            user_numbers.remove(11)
            user_numbers.append(1)
        sum_user_number = sum(user_numbers)
        print(
            f"Your cards: {user_numbers}, current score: {sum(user_numbers)} \n Computer's first card: {comp_number}"
        )
        if sum_user_number < 21:
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
        else:
            break
        user_choice = choice

    comp_score = sum(comp_numbers)
    user_score = sum(user_numbers)
    if user_score > 21:
        # print(lost)
        print(
            f"Your final hand: {user_numbers}, final score: {user_score} \n Computer's final hand: {comp_numbers}, final score: {comp_score} \n\n Computer Wins!! You are BUSTED!!"
        )
    elif comp_score > 21:
        # print(win)
        print(
            f"Your final hand: {user_numbers}, final score: {user_score} \n Computer's final hand: {comp_numbers}, final score: {comp_score} \n\n You WIN!! Computer is busted!!"
        )
    elif comp_score == user_score:
        # print(draw)
        print(
            f"Your final hand: {user_numbers}, final score: {user_score} \n Computer's final hand: {comp_numbers}, final score: {comp_score} \n\n Its a DRAW!!"
        )
    elif comp_score > user_score:
        # print(lost)
        print(
            f"Your final hand: {user_numbers}, final score: {user_score} \n Computer's final hand: {comp_numbers}, final score: {comp_score} \n\n Computer Wins!!"
        )
    else:
        # print(win)
        print(
            f"Your final hand: {user_numbers}, final score: {user_score} \n Computer's final hand: {comp_numbers}, final score: {comp_score} \n\n  You WON!!"
        )

    start1 = input("Do you want to play Again? Type \'y\' or \'n\':  ").lower()

    start = start1