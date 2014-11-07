from chess.pieces.color import Color
from chess.pieces.piece import Piece

class Knight(Piece):
    def render(self):
        if self.color == Color.white:
            return 'N'
        else:
            return 'n'

    def valid_move(self, position):
        # If the move is in an L shape, there are two cases,
        # - the difference in x is 1 and the difference in y is 2, like a normal L
        # - the difference in x is 2 and the difference in y is 1, an L on its side
        if ((abs(position.x - self.position.x) == 1 and abs(position.y - self.position.y) == 2) or
            (abs(position.x - self.position.x) == 2 and abs(position.y - self.position.y) == 1)):

            return True

        # Movement not in an L shape
        return False

    def is_path_clear(self, board, to_pos):
        # Path always clear for knight
        return True
