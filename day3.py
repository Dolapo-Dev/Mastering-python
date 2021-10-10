# First Quiz
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print(" Yaay! Please proceed to the rollercoaster")
else:
  print("I am sorry, you are not allowed to the rollercoaster")

  # Second Quiz
  # 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 == 0:
  print(f"{number} is an even number")
else:
  print(f"{number} is an odd number")

# Third quiz
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi_result = weight / (height ** 2)
formatted_bmi = "{:.0f}".format(bmi_result) # this is to round up bmi to the nearest whole number
bmi = int(formatted_bmi)


if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  # print(f"Your BMI is {bmi}, you are '\033[1m' slightly overweight '\033[0m'.")
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  # print(f"Your BMI is {bmi}, you have a '\033[1m' normal weight '\033[0m'.")
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# procedure 1
a = year % 4
b = year % 100
c = year % 400

if (a + c) == b:
  print("Leap Year")
else:
  print("Not Leap")

# Procedure 2
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

# QUIZ 3 (MY Version)
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

# if size == "S":
#   bill = 15
#   if add_pepperoni == "Y":
#     bill += 2
#     if extra_cheese == "Y":
#       bill += 1
#     else:
#       bill += 0
#   else:
#     if extra_cheese == "Y":
#       bill += 1
#     else:
#       bill += 0
#   print(f"Your final bill is: ${bill}.")


# elif size == "M":
#   bill = 20
#   if add_pepperoni == "Y":
#     bill += 3
#     if extra_cheese == "Y":
#       bill += 1
#     else:
#       bill += 0
#   else:
#     if extra_cheese == "Y":
#       bill += 1
#     else:
#       bill += 0
#   print(f"Your final bill is: ${bill}.")

# elif size == "L":
#   bill = 25
#   if add_pepperoni == "Y":
#     bill += 3
#     if extra_cheese == "Y":
#       bill += 1
#     else:
#       bill += 0
#   else:
#     if extra_cheese == "Y":
#       bill += 1
#     else:
#       bill += 0
#   print(f"Your final bill is: ${bill}.")

# else:
#   print("No choice")


# optimized 

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
elif size == "L":
  bill += 25
else:
  print("Not a valid choice")

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1
print(f"Your final bill is ${bill}")



