import my_module

print(my_module.pi)

# Quiz 1
#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random

print("Are you ready to roll the dice? I sense you are, lets do this!")

roll_dice = random.randint(0,1)

if roll_dice == 1:
  print("Heads")
else:
  print("Tails")

# Quiz 2
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(names)

people = (len(names)) - 1
print(people)

random_person = random.randint(0, people)

print(random_person)

print(f"{names[random_person]} is going to buy the meal today!")

