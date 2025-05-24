raise Exception("The code will not work by running it in python Please go to reeborgs world to test out the code")
# Do Not Copy This Line Only Copy The Solution Below


# Solution
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

