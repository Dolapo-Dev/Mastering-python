#Fix the code below 👇

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

print("Hello world!\nHello world!")

print("Hello" + " " + "Angela")
print("Hello " + "Angela")
print("Hello" + " Angela")
input("where do you live ? ")
print("You typed " + input("where do you live ? "))
# "input("where do you live ?")" will become what you type to the prompt, it can be otutput using print()
print("Good to know you are from " + input("where are you from ? "))


print("Hello " + input("what is your name ? "))

print( len( input("what is your name ? ") ) )

name = "Jack"
print(name)


name = "Angela"
print(name)

name = input("what is your name? ")
length = len(name)

print(length)

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
############################################
# 🚨 Don't change the code above 👆
####################################
#Write your code below this line 👇
c = a
a = b
b = c
#Write your code above this line 👆
####################################
# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
##############################################################
# Day 1 Challenge
#1. Create a greeting for your program.
print("Hello! Welcome to portal where Band names are generated")
#2. Ask the user for the city that they grew up in.
city = input("what is the name of the city you grew up?\n")
#3. Ask the user for the name of a pet.
pet = input("what is the name of your pet?\n")
#4. Combine the name of their city and pet and show them their band name.
print('Your band name could be ' +city + " " + pet)
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/

