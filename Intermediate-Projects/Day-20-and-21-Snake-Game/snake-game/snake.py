import random
from turtle import Turtle,Screen
from pathlib import Path
import itertools
import time

IMAGE_DIRECTORY = Path(__file__).resolve().parent.parent / "images"

SIZE_OF_GRID = 20
image_list = {"body_upper_left" : str(IMAGE_DIRECTORY / "snake_body_upper_left.gif"),
              "body_horizontal" : str(IMAGE_DIRECTORY / "snake_body_horizontal.gif"),
              "body_upper_right": str(IMAGE_DIRECTORY / "snake_body_upper_right.gif"),
              "head_up" :str(IMAGE_DIRECTORY / "snake_head_up.gif"),
              "head_right" :str(IMAGE_DIRECTORY / "snake_head_right.gif"),
              "body_lower_right" : str(IMAGE_DIRECTORY / "snake_body_lower_right.gif"),
              "body_vertical" : str(IMAGE_DIRECTORY / "snake_body_vertical.gif"),
              "head_left" : str(IMAGE_DIRECTORY / "snake_head_left.gif"),
              "head_down" : str(IMAGE_DIRECTORY / "snake_head_down.gif"),
              "body_lower_left" : str(IMAGE_DIRECTORY / "snake_body_lower_left.gif"),
              "tail_down" : str(IMAGE_DIRECTORY / "snake_tail_down.gif"),
              "tail_left" : str(IMAGE_DIRECTORY / "snake_tail_left.gif"),
              "fruit" : str(IMAGE_DIRECTORY / "fruit.gif"),
              "tail_right" :str(IMAGE_DIRECTORY / "snake_tail_right.gif"),
              "tail_up" : str(IMAGE_DIRECTORY / "snake_tail_up.gif")
}

directions = {"up" : 90,
              "down" : 270,
              "left" : 180,
              "right" : 0
}
SIZE_OF_GRID = 20

grid_tiles = {"up" : (0,SIZE_OF_GRID),
                "down" : (0,-SIZE_OF_GRID),
                "left" : (-SIZE_OF_GRID,0),
                "right" : (+SIZE_OF_GRID,0)
} # Basically this dict refers to the immediate left right up down of a particular tile


screen = Screen()
for value in image_list.values():
    screen.addshape(str(IMAGE_DIRECTORY / value))

class Snake:
    def __init__(self):
        self.segments : list[Turtle] = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]
        self.visualize()

    def create_snake(self):
        for i in range(3):
            self.add_segment((-SIZE_OF_GRID*i,0))

    def add_segment(self,position):
        new_segment = Turtle(shape = "square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def extend(self):
        self.tail.shape("square")
        # self.correct_heading()
        for direction in directions:
            if self.tail.heading() == directions[direction]:
                new_tail_position = self.segments[-1].position() - grid_tiles[direction]
                self.add_segment((round(new_tail_position[0],2),round(new_tail_position[1],2)))
            # I'm subtracting the direction because if tail faces right then the new tail must be on the left side
            # and If you see me rounding it's because of floating point problems the positions are sometimes 19.999999 
        self.correct_heading()
        self.tail = self.segments[-1]
        self.visualize()


    def move(self):
        
        self.head.forward(SIZE_OF_GRID)
        self.correct_heading()
        for segment in self.segments[1:]:
            segment.forward(SIZE_OF_GRID)
        self.correct_heading()
        self.visualize()

    def change_direction(self,direction):
        direction_change_time = 0
        def up():
            if self.head.heading() != directions["down"]:
                self.head.setheading(directions["up"])
        def down():
            if self.head.heading() != directions["up"]:
                self.head.setheading(directions["down"])
        def left():
            if self.head.heading() != directions["right"]:
                self.head.setheading(directions["left"])
        def right():
            if self.head.heading() != directions["left"]:
                self.head.setheading(directions["right"])
        def do_nothing():
            pass

        if direction == "Up":
            return up
        elif direction == "Down":
            return down
        elif direction == "Left":
            return left
        elif direction == "Right":
            return right
        else:
            return do_nothing
    
    def correct_heading(self):
        for seg_num in range((len(self.segments) - 1), 0, -1):
            if seg_num != 0:
                x_diff = -round(self.segments[seg_num].xcor() - self.segments[seg_num - 1].xcor(),1)
                y_diff = -round(self.segments[seg_num].ycor() - self.segments[seg_num - 1].ycor(),1)
                # It is negative because if the 2nd segment is at right side of first segment,
                # the 2nd segment should have heading towards first segment
                tile_diff = (x_diff,y_diff)
                for direction in directions:
                    if tile_diff == grid_tiles[direction]:
                        self.segments[seg_num].setheading(directions[direction])
                
    def visualize(self):
        if self.head.heading() == directions["up"]:
            self.head.shape(image_list["head_up"])
        elif self.head.heading() == directions["down"]:
            self.head.shape(image_list["head_down"])
        elif self.head.heading() == directions["left"]:
            self.head.shape(image_list["head_left"])
        elif self.head.heading() == directions["right"]:
            self.head.shape(image_list["head_right"])

        if self.tail.heading() == directions["up"]:
            self.tail.shape(image_list["tail_down"])
        elif self.tail.heading() == directions["down"]:
            self.tail.shape(image_list["tail_up"])
        elif self.tail.heading() == directions["left"]:
            self.tail.shape(image_list["tail_right"])
        elif self.tail.heading() == directions["right"]:
            self.tail.shape(image_list["tail_left"])

        for current_segment,next_segment in itertools.pairwise(self.segments[1:]):
            #FIXME: MAKE A DICTIONARY OF THIS DATA
            if (current_segment.heading(),next_segment.heading()) == (directions["up"],directions["up"]):
                current_segment.shape(image_list["body_vertical"])
            elif (current_segment.heading(),next_segment.heading()) == (directions["down"],directions["down"]):
                current_segment.shape(image_list["body_vertical"])
            elif (current_segment.heading(),next_segment.heading()) == (directions["left"],directions["left"]):
                current_segment.shape(image_list["body_horizontal"])
            elif (current_segment.heading(),next_segment.heading()) == (directions["right"],directions["right"]):
                current_segment.shape(image_list["body_horizontal"])
            elif (current_segment.heading(),next_segment.heading()) == (directions["up"],directions["right"]):
                current_segment.shape(image_list["body_lower_right"])
            elif (current_segment.heading(),next_segment.heading()) == (directions["down"],directions["right"]):
                current_segment.shape(image_list["body_upper_right"])
            elif (current_segment.heading(),next_segment.heading()) == (directions["up"],directions["left"]):
                current_segment.shape(image_list["body_lower_left"])
            elif (current_segment.heading(),next_segment.heading()) == (directions["down"],directions["left"]):
                current_segment.shape(image_list["body_upper_left"])
            elif (current_segment.heading(),next_segment.heading()) == (directions["right"],directions["up"]):
                current_segment.shape(image_list["body_upper_left"])
            elif (current_segment.heading(),next_segment.heading()) == (directions["right"],directions["down"]):
                current_segment.shape(image_list["body_lower_left"])
            elif (current_segment.heading(),next_segment.heading()) == (directions["left"],directions["up"]):
                current_segment.shape(image_list["body_upper_right"])
            elif (current_segment.heading(),next_segment.heading()) == (directions["left"],directions["down"]):
                current_segment.shape(image_list["body_lower_right"])
            else:
                current_segment.shape("square")
        
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.set_border()
        self.penup()
        self.goto(0,280)
        self.score = 0
        self.color("white")
        self.write(f"Score: {self.score}", align = "center",font = ("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align = "center",font = ("Courier", 20, "normal"))

    def increase_score(self):
        self.clear()
        self.set_border()
        self.penup()
        self.goto(0,280)
        self.score += 1
        self.write(f"Score: {self.score}", align = "center",font = ("Courier", 20, "normal"))

    def set_border(self):
        self.pendown()
        self.color("white")
        self.hideturtle()
        self.teleport(290,290)
        self.goto(290,-290)
        self.goto(-290,-290)
        self.goto(-290,290)
        self.goto(290,290)
        self.goto(290,320)
        self.goto(-290,320)
        self.goto(-290,290)
        self.goto(290,290)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5,stretch_wid = 0.5)
        self.color("orange")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        rand_x,rand_y = 20*random.randint(-12,12),20*random.randint(-12,12)
        self.goto(rand_x,rand_y)


        