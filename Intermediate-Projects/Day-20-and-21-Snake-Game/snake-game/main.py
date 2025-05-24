import time
from turtle import Screen
import os
from snake import Snake,Scoreboard,Food

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

def play_game():

    screen = Screen()
    screen.tracer(0)
    screen.colormode(255)
    screen.setup(width=640,height=720)
    screen.title("Snake Game")
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()


    while food.position() in [segment.position() for segment in snake.segments]:
        food.refresh()

    screen.listen()
    directions = ["Up","Down","Right","Left"]
    for direction in directions:
        screen.onkey(snake.change_direction(direction),direction)

    while True:
        time.sleep(0.15)
        
        screen.update()
        snake.move()
        
        wall_collision_conditions =  [round(snake.head.xcor(),2) > 280,
                                round(snake.head.xcor(),2) < -280,
                                round(snake.head.ycor(),2) > 280,
                                round(snake.head.ycor(),2) < -280,
        ]
                                
        body_collision_conditions = [(round(snake.head.xcor() - segment.xcor(),2) , round(snake.head.ycor() - segment.ycor(),2))
                                    for segment in snake.segments[1:]]
        # I'm checking if difference of x,y btw snake head and any other segment is (0,0)

        
        if snake.head.distance(food) < 10 :
            while any([segment.distance(food) < 10 for segment in snake.segments]):
                food.refresh()
            snake.extend()
            scoreboard.increase_score()
            time.sleep(0.075)
            screen.update()

        if any(wall_collision_conditions):
            scoreboard.game_over()
            break

        if (0,0) in body_collision_conditions:
            scoreboard.game_over()
            break
    screen.exitonclick()

play_game()
while True:
    want_to_play =input("do you want to play again? (yes/no) \n").lower()
    while want_to_play not in ["yes","no"]:
        print("Invalid input.")
        want_to_play = input("do you want to play? (yes/no) \n").lower()
    if want_to_play == "yes":
        play_game()
    elif want_to_play == "no":
        break

