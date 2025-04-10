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
        # TODO: Add a health attribute to the Player class (start at 100)
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

def explore_dark_woods(player):
    print(f"{player.name}, you step into the dark woods. The trees whisper as you walk deeper.")
    if not player.has_lantern:
        add_to_inventory(player, "lantern")
        player.has_lantern = True

def explore_mountain_pass(player):
    print(f"{player.name}, you make your way towards the mountain pass, feeling the cold wind against your face.")
    if not player.has_map:
        add_to_inventory(player, "map")
        player.has_map = True

# TODO: Modify explore_cave(player)
#       - If player does not have lantern, subtract 10 health
def explore_cave(player):
    if player.has_lantern:
        print(f"{player.name}, you enter the cave, your lantern lighting the way.")
        add_to_inventory(player, "treasure")
    else:
        player.health -= 10
        print("It's too dark to continue without a lantern. You take damage trying to navigate.")

# TODO: Modify explore_hidden_valley(player)
#       - If player does not have map, subtract 10 health
def explore_hidden_valley(player):
    if player.has_map:
        print(f"{player.name}, you use your map to find a hidden valley.")
        add_to_inventory(player, "rare herbs")
    else:
        player.health -= 10
        print("You can't find the hidden valley without a map. You get lost and take damage.")

# TODO: Create a function stay_still(player)
#       - Subtract 10 health when the player stays still
def stay_still(player):
    player.health -= 10
    print("You stay still, but the forest's stillness drains your energy.")

# TODO: Create a function check_win(player)
#       - If "treasure" and "rare herbs" are both in inventory, print win message and exit
def check_win(player):
    if "treasure" in player.inventory and "rare herbs" in player.inventory:
        print(f"Congratulations, {player.name}! You've found the treasure and rare herbs! You win!")
        exit()

# TODO: Create a function check_lose(player)
#       - If health is 0 or lower, print lose message and exit
def check_lose(player):
    if player.health <= 0:
        print(f"Game over, {player.name}. You have died.")
        exit()

player = welcome_player()

describe_area()

while True:
    print("\nYou see several options ahead:")
    print("\t1. Take the left path into the dark woods.")
    print("\t2. Take the right path toward the mountain pass.")
    print("\t3. Stay where you are.")
    print("\t4. Explore a nearby cave.")
    print("\t5. Search for a hidden valley.")
    print("\tI. Check Inventory")

    decision = input("What will you do (1, 2, 3, 4, 5 or I): ").lower()

    if decision == "1":
        explore_dark_woods(player)
    elif decision == "2":
        explore_mountain_pass(player)
    elif decision == "3":
        stay_still(player)
    elif decision == "4":
        explore_cave(player)
    elif decision == "5":
        explore_hidden_valley(player)
    elif decision == "i":
        if player.inventory:
            print("Inventory:", ", ".join(player.inventory))
        else:
            print("Your inventory is empty.")
    else:
        print("Invalid choice. Please choose 1, 2, 3, 4, 5, or I.")

    # TODO: Show the player's current health after every action
    print(f"{player.name}'s current health: {player.health}")

    check_win(player)
    check_lose(player)

    play_again = input("Do you want to continue exploring? (yes or no): ").lower()
    if play_again != "yes":
        print(f"Thanks for playing, {player.name}! See you next time.")
        break