import math

class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceTo(self, point):
        return math.sqrt(math.pow(self.x - point.x, 2) + math.pow(self.y - point.y, 2))

    def add(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def from_letters(coords, board):
        """Generate a Cartesian coordinate point from letter + number representation.

           Keyword arguments:
           coords -- string of form 'A1', 'G5', etc.
           board  -- current game board
        """

        # Check that string is uppercase
        if coords[0].islower():
            raise IndexError('Lower-case character out of range, use upper-case only')

        # String representation is 1-indexed and reversed (8 is at top)
        return Point(ord(coords[0]) - 64 - 1, board.height - int(coords[1]))

    def to_letters(self, board):
        """Convert coordinate to letter + number representation.

           For example:
           (3, 5) -> C5
           (6, 2) -> F2

           Keyword arguments:
           board -- current game board
        """

        # String representation is reversed (8 is at top)
        return str(chr(self.x + 97)).upper() + str(board.height - self.y)

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
