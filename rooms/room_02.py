from utils import Room

class Room02(Room):
    """
    Room02 represents the tunnel room in the game.

    This class inherits from the Room class and initializes the tunnel room
    with a name, description, an exit to the west, and a key item.
    """

    def __init__(self):
        """
        Initializes the Room02 instance.

        Sets the room name to "Tunnel" and the description to "You're in a narrow, winding tunnel."
        Adds an exit to the west leading to the "Cavern" and adds a "key" item to the room.
        """
        super().__init__("Tunnel", "You're in a narrow, winding tunnel.")
        self.add_exit("west", "Cavern")
        self.add_item("key")
