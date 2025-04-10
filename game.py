'''
Adventure Game
Author: Alec Berlin
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''

# TODO: Create a class called Player to represent the player in the game
class Player:
    # TODO: Inside the Player class, define an __init__ method that:
    #       - Takes a name parameter
    #       - Initializes these attributes:
    #           - self.name (string)
    #           - self.inventory (empty list)
    #           - self.health (set to 100)
    #           - self.has_map (set to False)
    #           - self.has_lantern (set to False)
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.has_map = False
        self.has_lantern = False

# TODO: Define a function called welcome_player() that:
#       - Prints a welcome message
#       - Asks the user for their name using input()
#       - Welcomes the user using an f-string
#       - Returns the Player object
def welcome_player():
    print("Welcome to the Adventure Game!")
    print('Your journey begins here... ')
    player_name = input("What is your name, adventurer? ")
    player = Player(player_name)
    print(f"Welcome, {player.name}! Your journey begins now.")
    return player

def describe_area():
    starting_area = """
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deeper into the
unknown...
"""
    print(starting_area)

# TODO: Update add_to_inventory() so it:
#       - Accepts a Player object as a parameter
#       - Appends the item to player.inventory
#       - Prints a message confirming the item was picked up
def add_to_inventory(player, item):
    player.inventory.append(item)
    print(f"You picked up a {item}!")

# TODO: Replace the global variable player_name with a Player object
#       Example: player = Player("Scott")
# TODO: Update your welcome_player() function to return a Player object
#       Instead of returning just a name, create and return the Player
player = welcome_player()

describe_area()

# Start the game Loop
while True:
    print("\nYou see two paths ahead:")
    print("\t1. Take the left path into the dark woods.")
    print("\t2. Take the right path toward the mountain pass.")
    print("\t3. Stay where you are.")
    print("\tI. Check Inventory")

    decision = input("What will you do (1, 2, 3, or I): ").lower()

    if decision == "1":
        print(f"{player.name}, you step into the dark woods. The trees whisper as you walk deeper.")
        add_to_inventory(player, "lantern")
        # TODO: In path 1, after picking up the lantern:
        #       - Set player.has_lantern = True
        player.has_lantern = True
    elif decision == "2":
        print(f"{player.name}, you make your way towards the mountain pass, feeling the cold wind against your face.")
        add_to_inventory(player, "map")
        # TODO: In path 2, after picking up the map:
        #       - Set player.has_map = True
        player.has_map = True
    elif decision == "3":
        print("You stay still, listening to the distant sounds of the forest")
    elif decision == "i":
        if player.inventory:
            print("Inventory:", ", ".join(player.inventory))
        else:
            print("Your inventory is empty.")
    else:
        print("Invalid choice. Please choose 1, 2, 3, or I.")

    # TODO: (Optional Stretch) Add a check before certain choices
    #       - Example: If player.has_lantern is False, prevent entering a cave
    #       - Print a message like “It’s too dark to continue without a lantern.”
    if decision == "1" and not player.has_lantern:
        print("It's too dark to continue without a lantern.")

    # Ask if they want to continue
    play_again = input("Do you want to continue exploring? (yes or no): ").lower()
    if play_again != "yes":
        print(f"Thanks for playing, {player.name}! See you next time.")
        break  # Exit the loop and end the game