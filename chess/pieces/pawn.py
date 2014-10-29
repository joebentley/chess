from chess.pieces.color import Color
from chess.pieces.piece import Piece

class Pawn(Piece):
    def render(self):
        if self.color == Color.white:
            return 'P'
        else:
            return 'p'

    def validMove(self, position):
        # If positive, move down the board, else move up
        moveDir = -1
        # White moves up, black moves down
        if self.color == Color.black:
            moveDir = 1

        if position.x == self.x and position.y == self.y + moveDir:
            return True
        return False

