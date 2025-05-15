import os
from art import logo

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return n1/n2
def take_number(string1):
    while True:
        try:
            return float(input(string1))
        except ValueError:
            print("Invalid input.")

operations = {"+":add,
              "-":subtract,
              "*":multiply,
              "/":divide,
}


print(logo)
number1 = take_number("What's the first number?: ")
while True:
    while True:
        try:
            for symbol in operations:
                print(symbol)
            operation_symbol = input("Pick an operation: ")
            if operation_symbol not in operations:
                raise ValueError
            break
        except ValueError:
            print("Invalid input.")
    number2 = take_number("What's the next number?: ")
    result = operations[operation_symbol](number1, number2)
    print(f"{number1} {operation_symbol} {number2} = {result}")
    choice = input(f"Type 'y' to continue calculating with {result}\n"
          "Type 'n' to start a new calculation\n"
          "Type anything else to stop the calculator.\n").lower()
    if choice == "y":
        number1 = result
    elif choice == "n":
        os.system("cls")
        print(logo)
        number1 = take_number("What's the first number?: ")
    else:
        break

