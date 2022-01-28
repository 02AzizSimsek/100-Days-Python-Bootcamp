print("hello world!")
#""ifadesi kullanıldıgı zaman içindeki kısım kod degildir anlamındadır 
print("hello"+" "+"aziz")

#-----------------

#1.Missing double quotes before the word Day.
#   print("Day 1-String Manipulation
#2.Outer double quotes changed to single quotes.
#   print('String Concatenation is done with the "+" sign.')
#3.Extra indentation removed 
#   print('e.g. print("Hello"+"world")') 
#4.Extra (in print function removed.)
#   print("New lines can be created with a backslash and n.")   

#--------------------

#input() will get user input in console
#Then print() will print the word "Hello" and the uset input 

a=input("what is your name: ")
print(a)

print("hello " + input("What is your name?"))

#--------------------

#sorunun çözümünde ise google araması olarak bakabiliriz =how to get the length of a string in python stack overflow
 
a=input("What is your name? ")
print(a)
len(a)

print(len(input("what is your name? ")))

s='please answer my question'
len(s)

#---------------------

name="jack"
print(name)

name="maximus"
print(name)

name=input("whats is your name?")
length=len(name)
print(length)

#---------------------

a=int(input("number a:"))
b=int(input("number b: "))
a*b

#-----------------------

#Band name Generator
 
print("welcome to the band name generator.")

city=input("which city did you grew up in?\n")

pet=input("what is your pet name?\n")

print(input("your name?\n")+" "+ city +" "+ pet )







