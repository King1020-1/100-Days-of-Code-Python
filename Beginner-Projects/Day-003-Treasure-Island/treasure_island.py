print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''',end = "")
play = True
while play:
    print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
    print("THE SIGN BOARD SAYS\nWhether you choose left or right you'll always be right.")
    # The interpretation according to me is if you chose right it is the path named right
    # while if you chose left it means it's the correct path for treasure
    direction = input('choose "left" or "right"\n').lower()
    if direction == "left":
        print("You've came to a lake. This is an island in the middle of the lake")
        action = input('Type "wait" to wait for a boat or type "swim" to swim across.\n').lower()
        if action == "wait":
            print("You arrive at the island unharmed. There is a house with 3 chests and 1 Key.")
            print("You can only open 1 Chest after that key will be stuck in that Chest.")
            print("Rule:- Statement on at least 1 Chest is True and at least 1 Chest is False.")
            print("Red Chest: The treasure is in the Yellow Chest")
            print("Yellow Chest: Every Chest with word 'Yellow' is True.")
            print("Blue Chest: The Yellow Chest is True.")
            # Logic is if Yellow was True then all statements must be True which violates the Rules
            # hence Yellow must be False which makes Blue False and Makes Red True
            colour = input("red,yellow or blue,Which chest will you open?\n").lower()
            if colour == "yellow":
                print("You found the treasure! You Win!")
            else:
                print("The key is stuck in the chest You chose Wrong, Game Over!")
        else:
            print("You arrive at the island poisoned by one of the fish and died, Game Over! ")
    else:
        print("You were on the right path but nothing was left, Game Over!")
    play = False
    try_again = input("Do you want to try again? Yes or No\n").lower()
    if try_again == "yes":
        play = True
        print()