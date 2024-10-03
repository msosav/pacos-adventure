from utils import Room


class Room00(Room):
    """
    Room00 represents the entrance room in the game.

    This class inherits from the Room class and initializes the entrance room
    with a name, description, an exit to the north, and a lantern item.
    """

    def __init__(self):
        """
        Initializes the Room00 instance.

        Sets the room name to "Entrance" and the description to "You are at the entrance of a mysterious cave."
        Adds an exit to the north leading to the "Cavern" and adds a "lantern" item to the room.
        """
        super().__init__("Entrance", "You are at the entrance of a mysterious cave.")
        self.add_exit("north", "Cavern")
        self.add_item("lantern")
