import os
from art import logo
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


bids = {}

print(logo)

while True:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "yes":
        cls()
    else:
        break

winner = max(bids, key=bids.get)
print(f"The winner is {winner} with a bid of ${bids[winner]}.")
