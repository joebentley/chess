from chess.pieces.color import Color
from chess.pieces.piece import Piece

class King(Piece):
    def render(self):
        if self.color == Color.white:
            return 'K'
        else:
            return 'k'

    def valid_move(self, position):
        # Check for single diagonal movement
        if abs(position.x - self.position.x) == 1 and abs(position.y - self.position.y) == 1:
            return True

        # Check for single horizontal or vertical movement
        if ((abs(position.x - self.position.x) == 1 and abs(position.y - self.position.y) == 0) or
            (abs(position.y - self.position.y) == 1 and abs(position.x - self.position.x) == 0)):

            return True

        return False

    def is_path_clear(self, board, to_pos):
        return True

