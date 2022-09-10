#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# pl = ""
# pn = 0
# for x in letters:
#     if pn < nr_letters:
#         pl += random.choice(letters)
#         pn += 1

# pn = ""
# nn = 0
# for x in numbers:
#     if nn < nr_numbers:
#         pn += str(random.choice(numbers))
#         nn += 1

# ps = ""
# sn = 0
# for x in symbols:
#     if sn < nr_symbols:
#         ps += random.choice(symbols)
#         sn += 1

# password = str(pl) + str(pn) + str(ps)

# print(f"Here is your Password:   {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

pl = ""
pn = 0
for x in letters:
    if pn < nr_letters:
        pl += random.choice(letters)
        pn += 1

pn = ""
nn = 0
for x in numbers:
    if nn < nr_numbers:
        pn += str(random.choice(numbers))
        nn += 1

ps = ""
sn = 0
for x in symbols:
    if sn < nr_symbols:
        ps += random.choice(symbols)
        sn += 1

password = str(pl) + str(pn) + str(ps)
password_list = []
for x in password:
    password_list.append(x)
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Here is your Password:   {password}")
