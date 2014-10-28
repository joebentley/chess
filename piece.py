from point import Point
from enum import Enum

class Color(Enum):
    white = 0
    black = 1
    neither = 2

class Piece:
    color = Color.white
    position = Point(0, 0)

    def __init__(self, position, color):
        self.position = position
        self.color = color

    # Check if move 
    def validMove(self, position):
        return True


class Pawn(Piece):
    
    def validMove(self, position):
        # If positive, move up, else move down
        moveDir = 1

        # White moves up, black moves down
        if self.color == Color.black:
            moveDir = -1

        if position.x == self.x and position.y == self.y + moveDir:
            return True

