#conditional
#if-else

#      -Code Challange-
#rollercoaster height measurment 
#task:if you body height 120cm or higer than 120cm,you can pass.If your body height under 120cm,you can't pass
print("welcome to the rollercoaster!")
height=int(input("what is your height in cm:"))

if height > 120:
    print("you can play in rollercoaster")
elif height==120:#or we don't write this,if block change:(if height >=120) shaped 
    print("you can ride the rollercoaster")
else:
    print("Sorry,you can't play in rollercoaster")

#comparison Operations
# ">" Greater than,"<" Less than,">="Greater than or equal to,"<="Less than or equal to
# "=" value assignment,"==" is it equal,"!=" it is not equal.


#     -Code Challange- 
#Odd or Even Exercise
#task:number calculator(even or odd)

#modulo=>"%"=gives the remainder,6/2=3,6%2=0

number =int(input("Which number do you want to change:"))

if  (number%2) == 0 :
    print("your number is even ")
else:
    print("your number is odd")    


# Nested if statements and elif statements

#     -Code Challange-
#rollercoaster height measurment and ticket price calculator
#task:if height=120 or height>120 ,and you 18 or under 18 you must be pay 7$ .if you older than 18 you must be pay 12$
#task:if height<120,you can't ride rollercoaster
#we use nested if/else,

# First write type 

height=int(input("your body height:"))
age=int(input("your age:"))

if height>=120:
    if age<=18:
        print("your ticket price:7$")
    else:
        print("your ticket price:12$ ")
else:
  print("you can't ride rollarcoaster")        
# Second write type

print ("welcome to rollarcoaster!")
height=int(input("your body height:"))
if height>=120:
    print("you can ride the rollarcoaster")
    age=int(input("what is your age?:"))
    if age<=18:
        print("please pay $7")
    else:
        print("please pay $12")
else:
   print("you can't ride rollarcoaster")        
       
#task new plugin:age<12 price 5$,age 12-18 price 7$,age>18 price 12$

print("welcome to the rollarcoaster")
height=int(input("what is your height in cm?:"))
 
if height>=120:
    print("you can ride the rollarcoaster")
    age=int(input("what is your age?: "))
    if age<12:
        print("please pay $5")
    elif age<=18:
        print("please pay $7")
    else:
        print("please pay $12")
else:
    print("Sorry,you have to grow taller before you can ride.")
    
#we can use as many elif conditions between the if and else as we

# -Code Challange-
#BMI 2.0
#task:BMI callculator and calculator say BMI values

print("welcome to the BMI")

height=float(input("enter your height(m):"))
weight=float(input("enter your weight(kg):"))

bmi=round(weight/(height**2))

if bmi<18.5:
    print(f"your BMI is {bmi},you are underweight")
elif bmi<25:
    print(f"your BMI is {bmi},you have a normal weight")
elif bmi<30:
    print(f"your BMI is {bmi},you are overweight")
elif bmi<35:
    print(f"your BMI is {bmi},you are obese") 
else:
    print(f"your BMI is {bmi},you are clinically obese")    


#  -Code Challange-
#task: leap year calculator
#task:1 year 365 days,leap year's february has 1 more day

year=int(input("Which year do you want to check?:"))

if year % 4==0:
    if year % 100 !=0:
        print(f"{year},year is leap")
    elif year % 100 ==0:
        if year %400!=0:
            print(f"{year},year is not leap")
        elif year % 400 ==0:
            print(f"{year},year is leap ")
else:
    print(f"{year},year is not leap")

# Multiple If Statements in Succession

# -Code Challange-
#task:Rollercoaster height measurment+ticket price(age filter for price)+(new)if take picture add cost your ticket price
#task:if height=120 or height>120 ,age<12 price 5$,age 12-18 price 7$,age>18 price 12$
#task:if height<120,you can't ride rollercoaster
#example:120cm,12 age and picture($3)=>7+3=$10

# First write type

print("welcome to the rollercoaster")

height=int(input("what is your height in cm?:"))

if height>=120:
    print("welcome to the rollercoaster")
    age=int(input("what is your age?:"))
    if age<12:
        print("would you like the photo")
        picture=str(input("y/n:"))
        if str(picture)=="y":
            print("please pay $8")
        if str(picture)=="n":
            print("please pay $5")
    if age<18:
        print("would you like the photo")
        picture=str(input("y/n:"))
        if str(picture)=="y":
            print("please pay $10")
        if str(picture)=="n":
            print("please pay $7")
    if age>=18:
        print("would you like the photo")
        picture=str(input("y/n:"))
        if str(picture)=="y":
            print("please pay $15")
        if str(picture)=="n":
            print("please pay $12")  
else:
   print("you can't ride the rollarcoaster")            
            
# Second write type

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")    


#   -Code Challange-
#task:Pizza order bill calculator
#task:Pizza size+pepperoni+extra chesse
#task information:
#  Small Pizza: $15-Medium Pizza: $20-Large Pizza: $25
#  Pepperoni for Small Pizza: +$2 -Pepperoni for Medium or Large Pizza: +$3
#  Extra cheese for any size pizza: + $1

# first write type

print("welcome to Python Pizza Delivers!")
size=input("what size pizza do you want? S-M-L:")
add_pepperoni=input("do you want pepperoni? Y-N:")
bill=0
if size=="S":
   bill +=15
   if add_pepperoni=="Y":
     bill += 2         
if size=="M":
   bill +=20
   if add_pepperoni=="Y":
     bill += 3          
if size=="L":
   bill +=25
   if add_pepperoni=="Y":
     bill += 3    
extra_cheese=input ("do you want extra cheese?Y-N:")
if extra_cheese=="Y":
   bill +=1
print(f"you pay:{bill}")     

# Second write type
print("welcome to Python Pizza Delivers!")
size=input("what size pizza do you want? S-M-L:")
add_pepperoni=input("do you want pepperoni? Y-N:")
extra_cheese=input ("do you want extra cheese?Y-N:")
bill=0
if size=="S":
   bill +=15
elif size=="M":
    bill +=20
else:
    bill +=25    
    
if add_pepperoni=="Y":
   if size=="S":
       bill +=2
   else:
       bill +=3
if extra_cheese=="Y":
   bill +=1
print(f"you pay:{bill}")       


#Logical Operations
# and-or-not

# -Code Challange-
#task:Rollercoaster height measurment+ticket price(age filter for price)+(new)if take picture add cost your ticket price
#task:if height=120 or height>120 ,age<12 price 5$,age 12-18 price 7$,age>18 price 12$
#task:if height<120,you can't ride rollercoaster
#new task:if age 45-55 price is free 
#example:120cm,12 age and picture($3)=>7+3=$10

# First write type

print("welcome to the rollercoaster")

height=int(input("what is your height in cm?:"))

if height>=120:
    print("welcome to the rollercoaster")
    age=int(input("what is your age?:"))
    if age<12:
        print("would you like the photo")
        picture=str(input("y/n:"))
        if str(picture)=="y":
            print("please pay $8")
        if str(picture)=="n":
            print("please pay $5")
    if age<18:
        print("would you like the photo")
        picture=str(input("y/n:"))
        if str(picture)=="y":
            print("please pay $10")
        if str(picture)=="n":
            print("please pay $7")
    if age>=18 and age<45:
        print("would you like the photo")
        picture=str(input("y/n:"))
        if str(picture)=="y":
            print("please pay $15")
        if str(picture)=="n":
            print("please pay $12")  
    if age>=45 and age<=55:
        print("you can ride free")
else:
   print("you can't ride the rollarcoaster")            
           
# second write type

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age>=45 and age<=55 :
    print("Everthing is going to be ok.have a ride on us!")  
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3  
  print(f"Your final bill is ${bill}")
else:
  print("Sorry, you have to grow taller before you can ride.")    

# -Code Challange-Difficult
#task:love calculator

#Task Information: Take both people's names and check for the number of times the 
#letters in the word TRUE occurs. Then check for the number of 
#times the letters in the word LOVE occurs.
#Then combine these numbers to make a 2 digit number.

#we use 
#lower_name="Aziz".lower()
#lower_name.count("z")

# First write type

name1=input("what is your name:")
name2=input("what is your lover name:")

low1=name1.lower()
low2=name2.lower()

t=int(low1.count("t")+low2.count("t"))
r=int(low1.count("r")+low2.count("r"))
u=int(low1.count("u")+low2.count("u"))
e=int(low1.count("e")+low2.count("e"))

true=(t+r+u+e)

l=int(low1.count("l") + low2.count("l"))
o=int(low1.count("o")+low2.count("l"))
v=int(low1.count("v")+low2.count("v"))
e1=int(low1.count("e")+low2.count("e"))

love=(l+o+v+e1)
score=int(str(true)+str(love))

if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score<=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

# Second write type

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")


#    -CODE Challange-
#task:make choises story for users

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
# First Write Type

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

episode1=input("you are at a crossroad.Where do you want to go? Type l-R:")
if episode1=="R" or episode1=="r":
      episode2=input("You\'ve come to a lake. There is an island in the middle of the lake. Type wait to wait for a boat. Type swim to swim across:S-W:")
      if episode2=="S":
           episode3=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?:R-Y-B:")
           if episode3=="Y":
               print("***You found the treasure! You Win!***")
           elif episode3=="R":
               print("It's a room full of fire. Game Over!!.")
           else:
               print("You enter a room of beasts. Game Over!!.")
      else:
          print("You get attacked by an angry trout. Game Over!!.")
else:
 print("You fell into a hole. Game Over!!.")        


# Second Write Type

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")

      
