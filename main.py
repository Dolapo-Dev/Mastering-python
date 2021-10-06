# Data Types
print("Hello"[0])
print("Hello"[4])
print("123"[2])

# integer
print(123 + 456)
# in python 123_456_789 is equivalent to 123456789

# when numbers have decimal point  they are Floating point number or Float

# Boolean can either be True or compile

# Data type conversion

num_char = len(input("what is your name?\t"))

print(type(num_char)) # this give the data type of num_char

new_num_char = str(num_char) #this convert num_char data type to a string

print("Your name has " + new_num_char + " characters")

# First Quiz
###################################
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

new_two_digit_number = str(two_digit_number)
a = int(new_two_digit_number[0])
b = int(new_two_digit_number[1])

print(a + b)
###############################################

# Another way
print(type(two_digit_number[0])) # confirm the data type
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
result = first_digit + second_digit
new_result =str(result) # change int to str
print("your result is " +new_result)

print(3 ** 2)
print(6 * 2)

# Second Quiz
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(type(height))
print(type(weight))
bmi = int(weight) / float(height) ** 2
print(type(bmi))
bmi_as_int = int(bmi)
print(bmi_as_int)

