# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
print(student_heights)
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
print(student_heights)

#Write your code below this row 👇
total_height = 0
sum_height = 0

for height in student_heights:
  sum_height += height
  total_height += 1

print(f"total number of heights inputed is {total_height}")
  
average_height = round(sum_height / total_height)

#new_height = "{:.0f}".format(sum_height / len(student_heights)) Alternative

#print("These are the heights " + student_heights)

print(f"The average height is {average_height} ")

#Write your code below this row 👇
even_number = 0
for even in range(2, 101, 2):
  even_number += even
  #print(even)
print(f"The total of all even numbers from 1 to 100 is {even_number}")

#Write your code below this row 👇 FizzBuzz Challenge
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password_list = []

for letter in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for sym in range(1, nr_symbols +1):
  password_list.append(random.choice(symbols))

for number in range(1, nr_numbers +1):
  password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)

password = ""

for char in password_list:
  password += char

print(password)




  

