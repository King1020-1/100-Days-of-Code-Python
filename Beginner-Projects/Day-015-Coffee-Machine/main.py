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

def is_resource_sufficient(ingredients):
    for item1 in ingredients:
        if MENU[choice]["ingredients"][item1] > resources[item1]:
            print(f"Sorry there is not enough {item1}.")
            return False
    return True

def is_payment_sufficient(drink):
    total_payment = 0
    print("Please insert coins.")
    for coin,value in coin_values.items():
        total_payment += integer_input(f"how many {coin}?: ")*value
    extra_money_paid = total_payment - MENU[drink]["cost"]
    if extra_money_paid > 0:
        print(f"Here is ${extra_money_paid:.2f} in change.")
        return True
    if extra_money_paid < 0:
        print(f"Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink):
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
        resources["money"] += MENU[drink]["cost"]
    print(f"Here is your {drink} ☕️. Enjoy!")

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {"water": 300,"milk": 200,"coffee": 100,"money":0}
coin_values = {"quarter":0.25,"dime":0.10,"nickle":0.05,"penny":0.01}

while True:
    choice = conditional_input("What would you like? (espresso/latte/cappuccino): ",
                               lambda text:text.lower() in ["espresso","latte","cappuccino","report","add","off"]).lower()
    if choice in ["espresso", "latte", "cappuccino"]:
        if not (is_resource_sufficient(MENU[choice]["ingredients"]) and is_payment_sufficient(choice)):
            continue
        make_coffee(choice)

    elif choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${resources["money"]}")

    elif choice == "add":
        for item in resources:
            if item != "money":
                resources[item] += integer_input(f"How much {item} do you want to add?: ")

    elif choice == "off":
        break