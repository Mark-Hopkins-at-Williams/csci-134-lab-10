"""
Here are some maze layouts you can use for testing your code!

"""

MAZE0 = [["ES", "WSE", "WS"],
         ["NSE", "WNE", "WN"],
         ["NE", "WE", "W"]]

MAZE1 = [["E", "WS", "S"],
         ["ES", "NWE", "NWS"],
         ["NE", "WE", "NW"]]

MAZE2 = [["E", "WS", "S"],
         ["ES", "NW", "NS"],
         ["NE", "WE", "NW"]]

MAZE3 = [["SE"] + ["WSE"]*6 + ["WS"],
         ["NSE"] + ["NWE"]*6 + ["NW"],
         ["NE"] + ["WE"]*6 + ["W"]]

MAZE4 = [["ES", "ESW", "SW"],
         ["ENS", "ENW", "NW"],
         ["EN", "WE", "W"]]

MAZE5 = [["E"] + ["WSE"]*6 + ["WS"],
         ["E"] + ["WNE"]*6 + ["WN"]]

MAZE6 = [["E", "WSE", "WS"],
         ["ES", "NSW", "N"],
         ["NE", "NWE", "W"]]

MAZE7 = [["ES", "WE", "W"],
         ["NES", "WE", "W"],
         ["NE", "WE", "W"]]

MAZE8 = [["E", "WSE", "W"],
         ["ES", "NWE", "WS"],
         ["NE", "WE", "NW"]]



def next_room(room, direction):
    """ Replace this with your code for Question One ("Maze"). """


class Maze:
    """
    IMPORTANT: Read, understand, but do NOT modify this class!!!!

    """
    def __init__(self, exits):
        self.num_visits = 0
        self.exits = exits

    def visit(self, room):
        self.num_visits += 1
        row, col = room[0], room[1]
        result = []
        for direction in self.exits[row][col]:
            destination = next_room(room, direction)
            if destination != None:
                result += [(direction, destination)]
        return sorted(result)

    def get_num_visits(self):
        return self.num_visits

    def get_room_string(self, room):
        return "O"

    def __str__(self):
        def erase_unless(condition, string):
            if condition:
                return string
            else:
                return " "
        result = ""
        for row in range(len(self.exits)):
            for col in range(len(self.exits[row])):
                result += " "
                result += erase_unless("N" in self.exits[row][col], "|")
                result += " "
            result += "\n"
            for col in range(len(self.exits[row])):
                result += erase_unless("W" in self.exits[row][col], "-")
                result += self.get_room_string((row, col))
                result += erase_unless("E" in self.exits[row][col], "-")
            result += "\n"
            for col in range(len(self.exits[row])):
                result += " "
                result += erase_unless("S" in self.exits[row][col], "|")
                result += " "
            result += "\n"
        return result

    __repr__ = __str__

