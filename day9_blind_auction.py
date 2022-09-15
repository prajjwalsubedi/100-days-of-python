logo = '''
       ___________
       \         /
        )_______(
        |"""""""|_.-._,.---------.,_.-._
        |       | | |               | | ''-.
        |       |_| |_             _| |_..-'
        |_______| '-' `'---------'` '-'
        )"""""""(
       /_________\\
     .-------------.
    /_______________\\
'''

from replit import clear
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the blind Auction!!!")
item = input("What item are we bidding for??")
clear()
bidding = []

status = "yes"
while status == "yes" or status == "y":
  print(f"Your are Bidding for \"{item}\"!!! ")
  name = input("What is your name?")
  amount = int(input("What is your bid amount?"))
  dict = {
    "name" : name,
    "amount" : amount,
  }
  bidding.append(dict)
  status = input("Are there any other bidders?? type yes or no:  ")
  clear()

  
winner_amount = 0
winner_name = ""
for x in range(len(bidding)):
  if bidding[x]["amount"] > winner_amount:
    winner_amount = bidding[x]["amount"]
    winner_name = bidding[x]["name"]
    
print(f"The winner is {winner_name} with the bid of ${winner_amount}.")