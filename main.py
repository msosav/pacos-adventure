import sys

from colorama import Fore, Style, init
from termcolor import colored

from rooms.room_00 import Room00
from rooms.room_01 import Room01
from rooms.room_02 import Room02
from utils import Game

init(autoreset=True)

if __name__ == "__main__":
    game = Game()

    # Create rooms
    entrance = Room00()
    cavern = Room01()
    tunnel = Room02()

    # Add rooms to the game
    game.add_room(entrance)
    game.add_room(cavern)
    game.add_room(tunnel)

    # Set starting room
    game.set_current_room("Entrance")

    print(Fore.CYAN + Style.BRIGHT + "Welcome to Paco's Adventures!" + Style.RESET_ALL)
    print(colored("Type 'help' for a list of commands.", "yellow"))
    game.look()

    while True:
        command = input(Fore.GREEN + "\n> " + Fore.RESET).lower().split()
        if not command:
            continue

        action = command[0]
        if action == "quit":
            print(colored("Thanks for playing!", "cyan"))
            sys.exit()
        elif action == "help":
            print(Fore.YELLOW + "Available commands:")
            print("  look - Look around the current room")
            print("  go [direction] - Move in a direction (north, south, east, west)")
            print("  take [item] - Pick up an item")
            print("  inventory - Check your inventory")
            print("  quit - Exit the game")
        elif action == "look":
            game.look()
        elif action == "go":
            if len(command) > 1:
                game.move(command[1])
            else:
                print(colored("Go where?", "red"))
        elif action == "take":
            if len(command) > 1:
                game.take(command[1])
            else:
                print(colored("Take what?", "red"))
        elif action == "inventory":
            game.inventory_check()
        else:
            print(colored("I don't understand that command.", "red"))
