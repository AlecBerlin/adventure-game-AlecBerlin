'''
Adventure Game
Author: Alec Berlin
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''

# TODO: Create an empty list called `inventory` at the top of your code.
inventory = []

# TODO: Define a function called welcome_player() that:
#       - Prints a welcome message
#       - Asks the user for their name using input()
#       - Welcomes the user using an f-string
#       - Returns the player's name
def welcome_player():
    print("Welcome to the Adventure Game!")
    print('Your journey begins here... ')
    player_name = input("What is your name, adventurer? ")
    print(f"Welcome, {player_name}! Your journey begins now.")
    return player_name

# TODO: Define a function called describe_area() that:
#       - Prints a multi-line string describing the starting location of the game
def describe_area():
    starting_area = """
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deeper into the
unknown...
"""
    print(starting_area)

# TODO: Define a function called add_to_inventory(item) that:
#       - Takes an item (string) as a parameter
#       - Adds the item to the inventory list
#       - Prints a message saying the item was picked up
def add_to_inventory(item):
    inventory.append(item)
    print(f"You picked up a {item}!")

# TODO: Call welcome_player() and store the result in a variable called player_name
player_name = welcome_player()

# TODO: Call describe_area() to print the scene before the game loop starts
describe_area()

# Start the game Loop
while True:
    print("\nYou see two paths ahead:")
    print("\t1. Take the left path into the dark woods.")
    print("\t2. Take the right path toward the mountain pass.")
    print("\t3. Stay where you are.")
    print("\tI. Check Inventory")

    decision = input("What will you do (1, 2, 3, or I): ").lower()

    # TODO: Inside the game loop:
    #       - If the user types "i", print the contents of the inventory
    #       - If the user chooses option 1, call add_to_inventory("lantern")
    #       - If the user chooses option 2, call add_to_inventory("map")

    if decision == "1":
        print(f"{player_name}, you step into the dark woods. The trees whisper as you walk deeper.")
        add_to_inventory("lantern")
    elif decision == "2":
        print(f"{player_name}, you make your way towards the mountain pass, feeling the cold wind against your face.")
        add_to_inventory("map")
    elif decision == "3":
        print("You stay still, listening to the distant sounds of the forest")
    elif decision == "i":
        if inventory:
            print("Inventory:", ", ".join(inventory))
        else:
            print("Your inventory is empty.")
    else:
        print("Invalid choice. Please choose 1, 2, 3, or I.")

    # Ask if they want to continue
    play_again = input("Do you want to continue exploring? (yes or no): ").lower()
    if play_again != "yes":
        print(f"Thanks for playing, {player_name}! See you next time.")
        break  # Exit the loop and end the game