import random
import os
from art import logo,vs
from game_data import data

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def play_game():
    
    random.shuffle(data)
    account1 = data.pop()
    print(logo)
    current_score = 0

    while True:
        if len(data) != 0:
            account2 = data.pop()
        else:
            print("You guessed everything correctly you're the ultimate winner!")
            break
        if account1["follower_count"] > account2["follower_count"]:
            correct_answer = "A"
        else:
            correct_answer = "B"
        print(f"Compare A: {account1["name"]}, a {account1["description"]}, from {account1["country"]}.")
        print(vs)
        print(f"Against B: {account2["name"]}, a {account2["description"]}, from {account2["country"]}.")
        while True:
            try:
                player_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
                if not player_choice in ["A","B"]:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input")
        if player_choice == correct_answer:
            current_score += 1
            cls()
            print(logo)
            print(f"You're right! Current score: {current_score}")
            account1 = account2
        else:
            cls()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {current_score}")
            break

while True:
    play_game()
    play_again = ""
    while play_again not in ["yes","no"]:
        play_again = input("Do you want to try again?\n").lower()
        print("Please type yes or no")
    if play_again == "no":
        break
    