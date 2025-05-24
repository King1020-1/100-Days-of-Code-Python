import random
from art import logo

def conditional_input(prompt: str,
                   condition:callable = lambda text:True,
                   error_message: str | None = "Invalid input"
                      ):
    """
    :param prompt: The prompt which should be displayed to the user.
    :param condition: A function which returns a condition on the inputted data
    :param error_message: The message displayed to user if condition is not satisfied
    :return: It returns the same thing as an input function
    """
    inputted_data = input(prompt)
    while not condition(inputted_data):
        print(error_message)
        inputted_data = input(prompt)
    return inputted_data

def integer_input(prompt: str ,error_message: str | None = "Invalid input,Input must be an Integer."):
    while True:
        try:
            inputted_data = int(input(prompt))
            break
        except ValueError:
            print(error_message)
    return inputted_data

difficulty_guesses = {"easy":10,"hard":5}

secretNumber = random.randint(1, 100)
game_win = False
print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
difficulty = conditional_input("Choose a difficulty. Type easy or hard: ",
                            lambda text:text.lower() in ["easy","hard"]).lower()

for attempts in range(difficulty_guesses[difficulty], 0, -1):
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = integer_input("Make a guess: ")
    if guess < secretNumber:
        print("Too low.")
        print("Guess again.")
    elif guess > secretNumber:
        print("Too high.")
        print("Guess again.")
    else:
        game_win = True
        break

if game_win:
    print(f"You got it! You win!")
else:
    print(f"You've run out of guesses, You lose.")
print(f"The answer was {secretNumber}.")


