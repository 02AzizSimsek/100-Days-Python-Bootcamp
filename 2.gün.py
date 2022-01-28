# what we will be make by the end of the day
print(len(12345))# it gives error like this
print(len('124569'))#this way it tells us that there are 6 of them
#len does not work int types


#  DATA TYPES 

#  String => we use for character, we use "" with quotation mark
print("Hello"[0])#=>output:H
print("Hello"[2])#=>output:l
#"123"#=>the computer does not understand that it is a number
print("123"+"456")#=>output:123456
print("hello"+"world")#=>output:helloworld

#  Integer=>if the data is of number type, integer type
print(123+456)#output:579
#123_456_789 => actually the computer removes the underscores and reads it as 123456789, the underscore makes it easier for us to read

#  Float=>called floating point and caters to dotted numbers
#3.14159

#  Boolean=>Approximates True or False, no need for quotation marks 
#It is used as a test method to check what we wrote.

num_char=len(input("what is your name? "))
#print("Your name has "+num_char+" characters")#wrong type
print(type(num_char))#type gives to blok type(int,str,float....),type check
new_num_char=str(num_char)#transformation data type 
print("Your name has "+new_num_char+" characters")#no wrong type 

print ("your name has "+str(num_char)+" characters")#different write ,no transformation type

print(20+float(100.70))
print(str(70)+str(100))

# -Code Challange-Data Types-
#task:if useres write 39,code output must be 12
#tast:if useres write 26,code output must be 8

# First write type
a=input("a:")
b=input("b:")
print(str(a)+str(b))
print(int(a)+int(b))

# Second write type
two_digit_number=input("number:")
print(int(two_digit_number[0])+int(two_digit_number[1]))

# Third write type
two_digit_number=input("number:")
first_digit=two_digit_number[0]
second_digit=two_digit_number[1]
result=int(first_digit)+int(second_digit)
print(result)

#    Mathematical Operation Python
#When you divide number,output type will be float
#PEMDAS,parentheses(),Exponents**,Multiplication*,Division/,Addition+,Subtraction-

# -Code Challange-BMI Calculator Exercise

#First write type 
a=float(input("height(m):"))
b=int(input("weight(kg):"))
print("your BMI:"+str(int(int(b)/float(a**2))))
#print(f"your BMI:",int(int(b)/float(a**2)))#we use f-string ,but we will learn later.

#Second write type
height=input("enter your height(m):")
weight=input("enter your weight(kg):")
bmi=int(weight)/float(height)**2
bmi_as_int=int(bmi)
print(bmi_as_int)

#Third write type
height=input("enter your height(m):")
weight=input("enter your weight(kg):")
bmi=int(int(weight)/float(height)**2)
print(bmi)


#Number Manipulation and F strings in python

print(8/3)
print(round(8/3))#rounding process
print(round(2.66666,2))#rounding 2.67
print(8//5)#direct rounding 1, actually (8/5)output:1.6 ,round(8/5) output:2

# f-string=>all these different data types can be combined into a string using an F in it.
score=0
height=1.8
isWinning=True
print(f"your score is {score},your height is {height},you are winning is {isWinning}")

# -Code Challange-Life in weeks 

#task:if we were lucky enough to live until 90 years old. The code is going to ask you for your current age
#task:to tell us how many days, weeks and months we actually have left

#task information=>1 year=365 days,1 year=52 weeks,1 year=12 months

age=input("What is your current age?:")

a=int(90)-int(age)

days=a*365
weeks=a*52
month=a*12
print(f"you have {days} days,weeks {weeks},month {month}")

# Tip Calculator 

#task:it'll ask you, what percentage tip would you like to give?,then finally it asks how many people are splitting this bill?
#examples=>bill total:124$,percentage:12,people split:7 ,should pay:19.93$

#First write type

bill=float(input("bill total:"))
percentage=float(input("percentage:"))
bill_percentage=(bill)*(percentage)/int(100)
bill_per_person=int(input("people:"))
pay=(bill_percentage)/(bill_per_person)+bill/bill_per_person
new_pay=round(pay,2)
new_pay="{:.2f}".format(pay)
print(f"you should pay:",new_pay)

#Second write type

print("welcome to the tip calculator!")
bill=float(input("What was the total bill?$:"))
tip=int(input("How much tip would you like to give? 10,12 or 15?:"))
people=int(input("How many people to split the bill?:"))
tip_as_percent=tip/100
total_tip_amount=bill*tip_as_percent
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)
final_amount="{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")

