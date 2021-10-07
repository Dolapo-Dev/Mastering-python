# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(type(height))
print(type(weight))
a = int(weight) / float(height) ** 2
print(type(a))
new_a = int(a)
print(new_a)
print(round( 8 / 3, 2)) # round up 8 divided by 3 to 2 decimal places

# ANother quz
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new_age = int(age)
rem_age = 90 - new_age
print(rem_age)
rem_months = rem_age * 12
rem_weeks = rem_age * 52
rem_days = rem_weeks * 7
# Using the f string
message = f"You have {rem_days} days, {rem_weeks} weeks, and {rem_months} months left."
print(message)

# Tip Calculator
print("Welcome to the tip calculator!")
amount = input("what does the bill amount to ? $")
print("Our hardworking staff will greatly appreciate your kind tips!")
bill = float(amount)
tip = int((input("How much percentage tip will you like to give ? 10, 12, 15: Please select -")))
percent_tip = float((tip / 100) + 1)
new_bill = round(bill * percent_tip, 2) # round up the new_bill to 2 decimal places
people = int(input("This bill will be split between what number of people? "))
each_person_in_five_people_pays = float(new_bill / people)
individual_pay = "{:.2f}".format(each_person_in_five_people_pays) # "{:.2f}".format(each_person_in_five_people_pays) gives result in 2 decimal places
print(f"Each person pays ${individual_pay}")


