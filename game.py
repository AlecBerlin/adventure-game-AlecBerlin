'''
Adventure Game
Author: Alec Berlin
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''

# Welcome message and introduction
print("Welcome to the Adventure Game!")  
print('Your journey begins here...')

# Ask for the player's name
player_name = input("what is your name, adventurer? ")

# Use an f-string to display the same message in a more readable way
print(f"Welcome, {player_name}! Your journey begins now.")

# Describe the starting area
starting_area = """
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deeper into the unknown...
"""
print(starting_area)

#Start the game loop
while True: 
    print("\nYou see two paths ahead: ")
    print("\t1. Take the left path into the dark woods. ")
    print("\t2. Take the right path toward the mountain pass." )
    print("\t3. Stay where you are. ")

    decision = input("What will you do (1,2,3)?: ")
    if decision == "1":
        print(f"{player_name}, You walk into the dark woods. The trees whisper as you walk deeper. ")
    elif decision == "2":
        print(f"{player_name}, You make your way towards the mountain pass, feeling the cold wind against your face. ")
    elif decision == "3":
        print(f"{player_name}, You stay still, listening to the distant sounds of the forest. ")
    else:
        print("Invalid choice. Please choose 1, 2, or 3. ")

