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


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_case_combined_string = name1.lower()+name2.lower()

t = lower_case_combined_string.count("t")
r = lower_case_combined_string.count("r")
u = lower_case_combined_string.count("u")
e = lower_case_combined_string.count("e")
l = lower_case_combined_string.count("l")
o = lower_case_combined_string.count("o")
v = lower_case_combined_string.count("v")
e = lower_case_combined_string.count("e")

first_number = str(t + r + u + e)
second_number = str(l + o + v + e)

result = int(first_number+second_number)

if result < 10 or result > 90:
  print(f"Your score is {result}, you go together like coke and mentos.")
elif result >= 40 and result <= 50:
  print(f"Your score is {result}, you are alright together.")
else:
  print(f"Your score is {result}.")

# Day 3 major quiz
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

first_question = input("You're at a cross road. Where do you want to go?  Type 'left' or 'right'\n\n")

direction = first_question.casefold()

if direction == "left":
  wait_swim = input("You come to a lake. There is an island in the middle of the lake. \nType 'swim' to swim across or 'wait' to wait for a boat.\n\n")
  lake = wait_swim.casefold()
  if lake == "wait":
    door = input("You arrive at the island unharmed. There is a house with 3 doors. \nOne is red, one yellow and one blue. Which colour do you choose?\n\n")
    which_door = door.casefold()
    if which_door == "yellow":
      print("You Win!")
    elif which_door == "blue":
      print("Eaten by beasts! Game Over")
    elif which_door == "red":
      print("Burned by fire! Game Over")
    else:
      if which_door != "red" or which_door != "blue":
        print("Game Over")
  else:
    #if lake ==  "swim" or lake != "wait":
    print("Attacked by crocodiles! Game Over.")
else:
  #if direction == "right" or direction != "left":
  print("Fall into a hole! Game Over")



