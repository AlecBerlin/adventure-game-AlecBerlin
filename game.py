'''
Adventure Game
Author: Alec Berlin
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.has_map = False
        self.has_lantern = False

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

def add_to_inventory(player, item):
    player.inventory.append(item)
    print(f"You picked up a {item}!")

player = welcome_player()

describe_area()

while True:
    print("\nYou see several options ahead:")
    print("\t1. Take the left path into the dark woods.")
    print("\t2. Take the right path toward the mountain pass.")
    print("\t3. Stay where you are.")
    # TODO: Add a new menu option for "Explore a nearby cave"
    print("\t4. Explore a nearby cave.")
    # TODO: Add a new menu option for "Search for a hidden valley"
    print("\t5. Search for a hidden valley.")
    print("\tI. Check Inventory")

    decision = input("What will you do (1, 2, 3, 4, 5 or I): ").lower()

    if decision == "1":
        print(f"{player.name}, you step into the dark woods. The trees whisper as you walk deeper.")
        add_to_inventory(player, "lantern")
        player.has_lantern = True
    elif decision == "2":
        print(f"{player.name}, you make your way towards the mountain pass, feeling the cold wind against your face.")
        add_to_inventory(player, "map")
        player.has_map = True
    elif decision == "3":
        print("You stay still, listening to the distant sounds of the forest")
    # TODO: In the cave choice:
    #       - If player.has_lantern is True: allow entry and add "treasure" to inventory
    #       - Else: display a message that it’s too dark
    elif decision == "4":
        if player.has_lantern:
            print(f"{player.name}, you enter the cave, your lantern lighting the way.")
            add_to_inventory(player, "treasure")
        else:
            print("It's too dark to continue without a lantern.")
    # TODO: In the valley choice:
    #       - If player.has_map is True: allow entry and add "rare herbs" to inventory
    #       - Else: display a message that you can’t find the valley
    elif decision == "5":
        if player.has_map:
            print(f"{player.name}, you use your map to find a hidden valley.")
            add_to_inventory(player, "rare herbs")
        else:
            print("You can't find the hidden valley without a map.")
    elif decision == "i":
        if player.inventory:
            print("Inventory:", ", ".join(player.inventory))
        else:
            print("Your inventory is empty.")
    else:
        print("Invalid choice. Please choose 1, 2, 3, 4, 5, or I.")

    # TODO: After picking up new items, confirm to the player they got it.
    # The add_to_inventory() function already prints a confirmation message.

    if decision == "1" and not player.has_lantern:
        print("It's too dark to continue without a lantern.")

    play_again = input("Do you want to continue exploring? (yes or no): ").lower()
    if play_again != "yes":
        print(f"Thanks for playing, {player.name}! See you next time.")
        break