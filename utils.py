from colorama import Fore, Style
from termcolor import colored


class Room:
    """
    A class to represent a room in the adventure game.

    Attributes:
    ----------
    name : str
        The name of the room.
    description : str
        A description of the room.
    exits : dict
        A dictionary of exits from the room, with directions as keys and rooms as values.
    items : list
        A list of items present in the room.
    """

    def __init__(self, name, description):
        """
        Constructs all the necessary attributes for the room object.

        Parameters:
        ----------
        name : str
            The name of the room.
        description : str
            A description of the room.
        """
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

    def add_exit(self, direction, room):
        """
        Adds an exit to the room.

        Parameters:
        ----------
        direction : str
            The direction of the exit (e.g., 'north', 'south').
        room : Room
            The room that the exit leads to.
        """
        self.exits[direction] = room

    def add_item(self, item):
        """
        Adds an item to the room.

        Parameters:
        ----------
        item : object
            The item to be added to the room.
        """
        self.items.append(item)


class Game:
    """
    A class to represent the game state.

    Attributes
    ----------
    rooms : dict
        A dictionary to store the rooms in the game.
    current_room : Room
        The room the player is currently in.
    inventory : list
        A list to store the items the player has picked up.

    Methods
    -------
    add_room(room):
        Adds a room to the game.
    set_current_room(room_name):
        Sets the current room based on the room name.
    move(direction):
        Moves the player in the specified direction.
    look():
        Prints the description of the current room.
    take(item):
        Allows the player to take an item from the current room.
    inventory_check():
        Prints the items in the player's inventory.
    """

    def __init__(self):
        self.rooms = {}
        self.current_room = None
        self.inventory = []

    def add_room(self, room):
        """
        Adds a room to the game.

        Parameters
        ----------
        room : Room
            The room to be added to the game.
        """
        self.rooms[room.name] = room

    def set_current_room(self, room_name):
        """
        Sets the current room based on the room name.

        Parameters
        ----------
        room_name : str
            The name of the room to set as the current room.
        """
        self.current_room = self.rooms[room_name]

    def move(self, direction):
        """
        Moves the player in the specified direction.

        Parameters
        ----------
        direction : str
            The direction to move the player.
        """
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            self.look()
        else:
            print(colored(f"You can't go {direction}.", "red"))

    def look(self):
        """
        Prints the description of the current room.
        """
        print(f"\n{Fore.CYAN}{Style.BRIGHT}{self.current_room.name}{Style.RESET_ALL}")
        print(colored(self.current_room.description, "yellow"))
        if self.current_room.items:
            print(Fore.GREEN + "You see:", ", ".join(self.current_room.items))
        print(Fore.MAGENTA + "Exits:", ", ".join(self.current_room.exits.keys()))

    def take(self, item):
        """
        Allows the player to take an item from the current room.

        Parameters
        ----------
        item : str
            The item to be taken from the current room.
        """
        if item in self.current_room.items:
            self.current_room.items.remove(item)
            self.inventory.append(item)
            print(colored(f"You picked up the {item}.", "green"))
        else:
            print(colored(f"There's no {item} here.", "red"))

    def inventory_check(self):
        """
        Prints the items in the player's inventory.
        """
        if self.inventory:
            print(Fore.YELLOW + "You are carrying:", ", ".join(self.inventory))
        else:
            print(Fore.YELLOW + "Your inventory is empty.")
