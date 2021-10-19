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
# print(people)

random_person = random.randint(0, people)


#print(random_person)
print(names[random_person] + " is going to buy the meal today!")

# or we use the random.choice() simply below
#print(random.choice(names) + " is going to buy the meal today!")

#third quiz
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
print(position[0])
c = int(position[0]) - 1
d = int(position[1]) - 1

map[c][d] = "x"

# using list() function to seperate the input
# each_position = list(position)
# a = int(each_position[0])
# b = int(each_position[1])

#map[b][a] = "x" 

print(map)

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

# # last quiz : My method
# import random

# choice = input("what do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors:\t")
# user_choice = int(choice)

# if user_choice <= 2:
#   rock = '''
#       _______
#   ---'   ____)
#         (_____)
#         (_____)
#         (____)
#   ---.__(___)
#   '''

#   paper = '''
#       _______
#   ---'   ____)____
#             ______)
#             _______)
#           _______)
#   ---.__________)
#   '''

#   scissors = '''
#       _______
#   ---'   ____)____
#             ______)
#         __________)
#         (____)
#   ---.__(___)
#   '''
#   computer_choice = random.randint(0, 2)
#   game_choice = [rock, paper, scissors]
#   computer = game_choice[computer_choice]
#   user = game_choice[user_choice]

#   if user == paper and computer == scissors:
#     print(f"You have chosen paper {paper} and \n computer chose scissors {scissors}\n You lose!")  
#   elif user == scissors and computer == paper:
#     print(f"You have chosen scissors {scissors} and \n computer chose paper {paper}\n You win!")
  
#   elif user == scissors and computer == rock:
#     print(f"You have chosen scissors {scissors} and \n computer chose rock {rock}\n You lose!") 
#   elif user == rock and computer == scissors:
#     print(f"You have chosen rock {rock} and \n computer chose scissors {scissors}\n You win!")
 
#   elif user == paper and computer == rock:
#     print(f"You have chosen paper {paper} and \n computer chose rock {rock}\n You win!")
#   elif user == rock and computer == paper:
#     print(f"You have chosen rock {rock} and \n computer chose paper {paper}\n You lose!")
  
#   elif user == computer:
#      print(f"You and computer have chosen {computer}\n It is a draw!")

# else:
#   print("Invalid Input! You lost")

# instructors method
import random

rock = '''
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  '''

paper = '''
      _______
  ---'   ____)____
            ______)
            _______)
          _______)
  ---.__________)
  '''

scissors = '''
      _______
  ---'   ____)____
            ______)
        __________)
        (____)
  ---.__(___)
  '''

game_choice = [rock, paper, scissors]
user_choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors:\t"))
if user_choice >=3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
else:
  print(game_choice[user_choice])

  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_choice[computer_choice])

  if user_choice == 0 and computer_choice == 2:
    print("You win")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
  elif computer_choice > user_choice:
    print("You lose!")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice == user_choice:
    print("It is a draw!")
  