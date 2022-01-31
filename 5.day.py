#Using the for loop with Python Lists
#for Loop

fruits =["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)
    
fruits =["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit+" pie")
    print(fruits)    
print(fruits) # indent position is important

# -Code Exercise-

#Average Height Exercise

# First write type

student_heights = input("Input a list of student heights:").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
len_student=len(student_heights)
y=0
for x in student_heights:
    y +=x
print(f"you wrote,{len_student} number")
print(f"total:{y}")    
print(f"average:{y/len_student}")    

#Second write type

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")
  
average_height = round(total_height / number_of_students)
print(average_height)

# Thrid write type -we didin't use for

student_heights = input("Input a list of student heights:").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height=sum(student_heights)
number_of_students=len(student_heights)
average_height=round(total_height/number_of_students)
print(average_height)










