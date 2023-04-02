def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    turn_left()
    turn_left()
    

#fails for other cases------debbug!!
while at_goal()!= True:
     
    if front_is_clear() :
        move() 
    elif wall_on_right()==False:
        turn_right()
        move()  
    elif wall_on_right() and front_is_clear()==False:
        turn_left()
          
    elif wall_in_front():
        turn_left()
        move()
        