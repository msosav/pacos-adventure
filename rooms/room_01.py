from utils import Room


class Room01(Room):
    """
    Room01 represents the cavern room in the game.

    This class inherits from the Room class and initializes the cavern room
    with a name, description, exits to the south and east, and a map item.
    """

    def __init__(self):
        """
        Initializes the Room01 instance.

        Sets the room name to "Cavern" and the description to "You find yourself in a large, echoing cavern."
        Adds an exit to the south leading to the "Entrance" and an exit to the east leading to the "Tunnel".
        Adds a "map" item to the room.
        """
        super().__init__("Cavern", "You find yourself in a large, echoing cavern.")
        self.add_exit("south", "Entrance")
        self.add_exit("east", "Tunnel")
        self.add_item("map")
