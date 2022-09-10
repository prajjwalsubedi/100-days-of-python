print("Welcome to The Tips Calculator")

bill = int(input("What was the total bill?:"))
tip = int(input("How much of a tip would you like to give? [Popular tips = 10 / 12 / 15]? :"))
people = int(input("Between how many people would you like to split the bill? :"))

bill_share = round((bill + bill * tip / 100) / people,2)

print(f"Each person has to pay ${bill_share}")