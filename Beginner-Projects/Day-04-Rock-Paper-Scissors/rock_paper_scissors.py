import random
import sys

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

player_wins = 0
computer_wins = 0

rps_choices = ["rock", "paper", "scissors"]
rps_art = [rock,paper,scissors]
win_list = [(0,1),(1,2),(2,0)]
loss_list = [(1,0),(2,1),(0,2)]

while player_wins < 5 and computer_wins < 5:
    print("\n--- New Round ---")
    print("")

    while True:
        try:
            player_input = (input("Type Rock,Paper,Scissors or end to close:\n")).lower()
            if player_input == "end":
                sys.exit()
            player_index = rps_choices.index(player_input)
            break

        except ValueError:
            print("Invalid input. Please enter Rock,Paper or Scissors.")

    computer_input = random.choice(rps_choices)
    computer_index = rps_choices.index(computer_input)

    print(f"\nYou chose: \n{rps_art[player_index]}")
    print(f"Computer chose: \n{rps_art[computer_index]}")

    if (computer_index,player_index) in loss_list:
        print("Computer wins this round!")
        computer_wins +=1
    elif (computer_index,player_index) in win_list:
        print("You win this round!")
        player_wins +=1
    elif player_index == computer_index:
        print("It's a tie!")

    print(f"\nScore: You {player_wins} - Computer {computer_wins}")



print("\n--- Game Over ---")
if player_wins > computer_wins:
    print("Congratulations! You won the game!")
else:
    print("The computer won the game.")

print(f"Final Score: You {player_wins} - Computer {computer_wins}")
