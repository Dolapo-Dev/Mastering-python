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




