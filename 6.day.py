# while something_is_true =>do something repeatedly

#for item in lists_of_items:
    #do something to each item
    
#for number in range (a,b):
    #print(number)    


 #   Reeborg's World Codes   

      # Hurdle-2

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    jump()

# ----------------------------------
      # Hurdle-3

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
-------------------------------------
      # Hurdle-4

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
#--------------------------------
      #  Maze

First Spelling

note: works but not efficient,there is a endless loop

def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if right_is_clear():
       turn_right()
       move()
    elif front_is_clear():
        move()
    else:
        turn_left()

Second Spelling

def turn_right():
    turn_left()
    turn_left()
    turn_left()
while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
       turn_right()
       move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
     
    

       
     
    

