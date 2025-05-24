import sys
import random
from turtle import Turtle,Screen

screen = Screen()
screen.setup(width = 500,height = 400)
is_race_on = False
colors = ["red","orange","yellow","green","blue","purple"]

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win?")
if user_bet: 
    user_bet = user_bet.lower() 

turtle_list = []

if user_bet:
    is_race_on = True
    for index,color in enumerate(colors):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.speed(2)
        new_turtle.color(color)
        new_turtle.goto(x=-230, y=-100 + 40 * index)
        turtle_list.append(new_turtle)
else:
    sys.exit() 
winning_color = "_" # Put this cuz pycharm was giving warning about being variable can be undefined,
                    # and _ specifically  because if I inputted an empty string, it gives the winning message


while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            continue
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

if winning_color == user_bet:
    print(f"You've won! The {winning_color} turtle is the winner!")
else:
    print(f"You've lost. The {winning_color} turtle is the winner!")

screen.exitonclick()