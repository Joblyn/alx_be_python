# This program calculates the age of a person in 2050.
# Assuming the current year is 2023.
# The script prompts the user for their current age.
# The user enters their age.
# The script calculates and prints how old the user will be in 2050.

current_year = 2023
future_year = 2050
user_input = input("How old are you? ")

while not user_input.isdigit():
    user_input = input("How old are you? ")

current_age = int(user_input)
age_in_2050 = current_age + (future_year - current_year)
print("In 2050 you will be", age_in_2050, "years old.")