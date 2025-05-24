import json
import random
import os
import sys

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def repeated_input(prompt: str,
                   condition:callable = lambda text:True,
                   error_message: str | None = "Invalid input",
                   integer: bool = False,
                   floating_point: bool = False):
    """
    :param prompt: The prompt which should be displayed to the user.
    :param condition: A function which returns a condition on the inputted data
    :param error_message: The message displayed to user if condition is not satisfied
    :param integer: True if you want to return an integer
    :param floating_point: True if you want to return a float ,
                  will return float if both integer and float are True
    :return: It returns the same thing as an input function
    """
    while True:
        try:
            inputted_data = input(prompt)
            if integer:
                inputted_data = int(inputted_data)
            if floating_point:
                inputted_data = float(inputted_data)
            if not condition(inputted_data):
                raise ValueError
            return inputted_data
        except ValueError:
            print(error_message)

def initial_grid(n: int)->list[list[int]]:
    """initializes a grid of n*n elements with all zeros"""
    return [[0]*n for _ in range(n)]

def rand_2_on_grid(grid: list[list[int]])-> list:
    """changes a random 0 into a 2 in the grid"""
    rand_list = list(range(len(grid)**2))
    random.shuffle(rand_list)
    global game_lost
    for i in rand_list:
        row,element = divmod(i,len(grid))
        if grid[row][element] == 0:
            grid[row][element] = 2
            break
    else:
        game_lost = True
    return grid

def slide(row: list[int])-> list:
    """a function which turns [0,2,4,2,0,2] --> [2,4,4,0,0,0]"""
    length1 = len(row)
    cleaned_list = [element for element in row if element]
    length2 = len(cleaned_list)
    for i in range(length2 - 1):
        if cleaned_list[i] == cleaned_list[i+1]:
            cleaned_list.pop(i+1)
            cleaned_list[i] *= 2
            cleaned_list.append(0)
    return cleaned_list + [0]*(length1-length2)

def rotate(grid: list[list[int]],n: int)->list[list[int]]:
    for _ in range(n):
        grid = [[element[i] for element in grid] for i in range(len(grid))]
        grid.reverse()
    # n = 1 for anti-clockwise , # n = 2 for "180 degree" rotation and n = 3 for clockwise rotation
    return grid

def slide_all(grid: list[list[int]],direction: str)->list[list[int]]:
    dict1 = {"up":(1,3),"left":(0,0),"down":(3,1),"right":(2,2)}
    # Basically the function shifts left
    # for shifting up is rotating anticlockwise then shifting left then rotating clockwise
    for i in dict1:
        if direction == i:
            grid = rotate(grid,dict1[i][0])
            for index, element in enumerate(grid):
                grid[index] = slide(element)
            grid = rotate(grid, dict1[i][1])
    return grid

username = input("Please type your username:\n").lower()

game_inputs = {"W":"up","A":"left","S":"down","D":"right"}
high_score_dict = {}

while True:
    try:
        with open("high_scores.json","r") as fp:
            high_score_dict = json.load(fp)
        high_score = high_score_dict.get(username, 0)
        break
    except (FileNotFoundError,json.decoder.JSONDecodeError) :
        with open("high_scores.json", "w") as fp:
            json.dump(high_score_dict, fp)

check_high_score = repeated_input("Type 0 to check high_score\n"
                                     "     1 to check high_score then play\n"
                                     "     2 to play\n",
                                  lambda number:(2 >= number >= 0),
                                  integer=True)

if check_high_score < 2:
    try:
        print(f"{username} has a high_score of {high_score_dict[username]}\n")
    except KeyError:
        print("You do not have a high_score saved.\n")
    if check_high_score == 0:
        sys.exit()
# The loop is for opening high_scores


while True:
    game_lost = False
    game_score = 2
    print("Welcome to 2048 Game")
          
    grid_size = 4

    print("Instructions:\n"
          "Press 'W' to move up\n"
          "Press 'A' to move left\n"
          "Press 'S' to move down\n"
          "Press 'D' to move right")

    play_grid = initial_grid(grid_size)
    play_grid = rand_2_on_grid(rand_2_on_grid(play_grid)) # adding 2s on 2 random positions
    # Initialization of game

    while not game_lost:
        max_row = [] #a list in which maximum values of all rows will be there
        for _row in play_grid:
            print(_row)
            max_row.append(max(_row))
        current_score = max(max_row)
        print(f"Your current score is {current_score}")

        play_direction = repeated_input("Which way do you want to move?(W/A/S/D)\n",
                                        lambda text:text in ["W","A","S","D"]).upper()
        play_grid = slide_all(play_grid,game_inputs[play_direction])
        play_grid = rand_2_on_grid(play_grid)
        if current_score > game_score:
            game_score = current_score
        cls()
    print(f"The game ended, You have a score of {game_score} in it.")
    play_again = repeated_input("Do you want to play again?(Yes/No):\n",
                                lambda text:text in ["yes","no"]).lower()
    if game_score > high_score:
        high_score = game_score
        high_score_dict[username] = high_score
    with open("high_scores.json","w") as fp:
        json.dump(high_score_dict, fp)

    if play_again == "no":
            break
