logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
from replit import clear

print(logo)


def calculate(x, y, z):
    if y == "+":
        calc = x + z
    elif y == "-":
        calc = x - z
    elif y == "/":
        calc = x / z
    elif y == "*":
        calc = x * z
    else:
        print("Please choose proper operator!!!")
    return calc


calc = 0
a = "yes"
b = "no"
while a == "yes" or a == "y":
    if b == "yes" or b == "y":
        x = calc
    else:
        x = float(input("Enter your first number:  "))
    y = input("choose the operater; + or - or * or / :  ")
    z = float(input("Enter your Second number:  "))
    calc = calculate(x, y, z)
    print(f"{x} {y} {z} = {calc}")

    b = input(
        f'Type \"Y\" to continue calculating with {calc}, or \"N\" to restart again :    '
    ).lower()

    if b == "yes" or b == "y":
        a = "yes"
    else:
        clear()
        a = "yes"
        print(logo)
