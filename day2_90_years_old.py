print("Find out how much time have you left to reach 90 years old??")

current_age = input("What is your current age? :")
current_int_age = int(current_age)

days = 1*365*90
weeks = 1*52*90
months = 1*12*90

new_days = days - current_int_age * 365
new_weeks = weeks - current_int_age * 52
new_months = months - current_int_age * 12

print(f"You have {new_days} days, {new_weeks} weeks, and {new_months} months left.")

