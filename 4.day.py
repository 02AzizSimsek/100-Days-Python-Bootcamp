#Random Module
#randomisation

import random

random_float=random.random()
print(random_float)

#0-5 float number 

randomFloat=random.random()*5
print(randomFloat)

love_score=random.randint(1, 100)
print(f"Your love score is {love_score}")

#  -Code Challange-

#Heads or Tails Exercise
#task:computer random number if number even=>head,number odd=>tail
 
# First write type

import random
score=random.randint(0,100)
print(score)

if score%2==0:
    print("head")
else:
  print("Tail")    

# Second write type
import random

random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")


#Understanding the Offset and Appending Items to Lists
#List Data Type 
#fruits=[item1,item2]=>fruits=["Cherry","Apple","Pear"]
#[-1]=>end of the list

states_of_america=["Delaware","Pennsylvania","New Jersey","Georgia"]
print(states_of_america[1])
print(states_of_america[-1])

states_of_america[1]="volcan" #change list data 
print(states_of_america)

states_of_america.append("logitech")#data add to list
print(states_of_america)

states_of_america.extend(["xry","door","clone"])
print(states_of_america)

"""
list.append =>add data to list
list.extend =>add another list's data to list

list.insert(i, x)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

list.clear()
Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]])
Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)
Return the number of times x appears in the list.

list.sort(*, key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Equivalent to a[:].
"""

# -Code Challange-

#Banker Roulette - Who will pay the bill?
#task:there are five person and random select one person
#we use str.split(',')=>"f,a,r" : output:['f','a','r']

# First write type

import random
print("welcome to the Python Restaurants")
names_string=input("Give me everbody's names,seperated by a comma.:")
names=names_string.split(",")
print(f"{random.choice(names)},is going to buy the meal today!")

# Second write type

import random
# Split string method
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

#Get the total number of items in list.
num_items = len(names)
#Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, num_items - 1)
#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")


# IndexErrors and Working with Nested Lists

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])



#   -Code Challange-
#treasure Map Exercise
#users write 31=>code write x on the row1 data 2=>"⬜️","⬜️","x"

# First write type

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
print("Where do you want to put the treasure? ")

a=int(input("first number(1,2,3):"))
b=int(input("second number(1,2,3):"))
print(str(a)+str(b))
map[b-1][a-1]="x"
                        
print(f"{row1}\n{row2}\n{row3}")     

# Second write type

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

#    -Code Challange-
#  Rock-Paper-Scissors Game
#Rock wins against scissors
#scissors  wins against Paper
#Paper wins against rock

#rock=0,paper=1,scissors=2.
import random
game=["rock","paper","scissors"]
hand=int(input("choise your hand model(0-1-2):"))
print(game[hand])

new_game=[0,1,2]
computer=random.choice(new_game)
if computer==0:
   print("rock")
elif computer==1:
   print("paper") 
else:
  print("scissors")   

if hand==0:
    if computer==0:     
     print("s")
    elif computer==1:       
     print("lose")
    else:       
     print("w")    
elif hand==1:
    if computer==1:   
     print("s")
    elif computer==2:   
     print("lose")
    else:
     print("w")
elif hand==2:
    if computer==2:   
     print("s")
    elif computer==0:
     print("lose")
    else:
     print("w")     

# Second write type

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0: 
    print("You typed an invalid number, you lose!") 
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")

##Debugging challenge:
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution:

