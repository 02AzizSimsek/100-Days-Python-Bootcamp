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


# -Code Exercise-

#Highest Score Exercise
#users put the numbers ,we found the highest number
#we don't use min or max ,we use for and if

# First write type
student_heights = input("Input a list of student heights:").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
max_num=0
for x in student_heights:
    if x>max_num:
        max_num=x
print(max_num)        
print(student_heights.index(max_num))   
        

# Second write type
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest score in the class is: {highest_score}")

#For Loop and Range()

# range(start, stop, step)
total=0
for number in range(1,101):
    total +=number
print(total)

# -Code Challange-

#Adding Evens Exercise
#task:I want you to calculate the sum of all the even numbers from 1 to 100,
#task:including 1 and 100.

total=0
for number in range(2,101,2):
    total +=number
    print(total)

# -Code Challange-
#The FizzBuzz Job Interview Question

"""
The first kid says 1, the second kid says 2.
But then when a kid encounters a number that's fully divisible by three,
then instead of saying that number, he's going to say Fizz.
And when the number is divisible by five,
instead of saying the number, they should say Buzz.
And if the number is divisible by both three and five, for example, 15,
then they should say Fizzbuzz.
"""
# First write type

for number in range (1,100):   
    if  number%3==0 and number%15!=0:
        print("Fizz")
    elif number%5==0 and number%15!=0:
        print("Buzz")
    elif number%15==0:
        print("FizzBuzz")
    else:
        print(number)

# Second write type
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

# -Code Challange-
#task:we made PyPassword Generator!
#task: we ask "how many letters would you like in your password?"
#task: we ask "How many symbols would you like"
#task:we ask"how many numbers would you like?
#and here is your password:
#there are two level esay or hard level 
#easy level 'letters'+'numbers'+'symbols'
#hard level random ('letters'+'numbers'+'symbols')
    
#Password Generator Project

# first write type-for hard level

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

new_letters=random.sample(letters,nr_letters)
new_symbols=random.sample(symbols,nr_symbols)
new_numbers=random.sample(numbers,nr_numbers)

new_letters.extend(new_symbols)
new_letters.extend(new_numbers)
random.shuffle(new_letters)

password = ""
for char in new_letters:
  password += char

print(f"Your password is: {password}")

# Second write type-for hard level

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list=[]

for char in range(1,nr_letters+1):
    password_list.append(random.choice(letters))
for char in range(1,nr_symbols+1):
    password_list.append(random.choice(symbols))
for char in range(1,nr_numbers+1):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password=""
for char in password_list:
    password +=char
print(f"your password is{password}")    

# Third write type-for esay level

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list=[]

for char in range(1,nr_letters+1):
    password_list.append(random.choice(letters))
for char in range(1,nr_symbols+1):
    password_list.append(random.choice(symbols))
for char in range(1,nr_numbers+1):
    password_list.append(random.choice(numbers))

print(password)


