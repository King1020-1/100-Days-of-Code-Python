import random
import turtle as t
from turtle import Turtle,Screen
t.colormode(255)

def colour_line(size: int,spacing: int,number:int):
    for _ in range(number):
        timmy.pendown()
        timmy.dot(size,random.choice(colour_list))
        timmy.penup()
        timmy.forward(spacing)
    timmy.backward(spacing*number)

def colour_square(size: int,spacing: int,number:int):
    for _ in range(number):
        colour_line(size,spacing,number)
        timmy.setheading(90)
        timmy.forward(spacing)
        timmy.setheading(0)

colour_list = [(5, 12, 35),
               (40, 21, 16), (130, 89, 54), (202, 137, 119), (235, 211, 82), (188, 137, 161),
               (216, 83, 67), (80, 6, 20), (33, 139, 65), (147, 86, 105), (193, 77, 101),
               (29, 87, 29), (220, 176, 210), (74, 107, 141), (152, 136, 65), (20, 207, 180),
               (12, 72, 28), (132, 158, 180), (7, 62, 139), (114, 188, 158), (86, 133, 173),
               (125, 8, 28), (18, 204, 220), (242, 204, 6), (236, 172, 164), (133, 223, 208)]

timmy = Turtle()
timmy.speed("fastest")
timmy.hideturtle()
timmy.teleport(-350,-300)
colour_square(20,50,10)
screen = Screen()
screen.exitonclick()

