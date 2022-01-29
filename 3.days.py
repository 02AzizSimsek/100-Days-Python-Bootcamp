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



























      