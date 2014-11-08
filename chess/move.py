
def check_move(board, from_pos, to_pos):
    """Check whether the piece at from_pos can move from move to to_pos
       without colliding with another piece or going off the board etc.

       Keyword arguments:
       board    (Board) -- current game board
       from_pos (Point) -- position containing piece that wants to move
       to_pos   (Point) -- position the piece wants to move to"""

    # Get piece from position
    piece = board.getsquare(from_pos)

    # Check if piece could move there on an _empty_ board or trying to move offscreen
    if not piece.valid_move(to_pos) or not board.point_on_board(to_pos):
        return False
    # Check if another piece at destination and it's the same colour, the move is invalid
    if board.piece_at(to_pos) and board.getPiece(to_pos).color == piece.color:
        return False
    # Check if there are any pieces in the path of our piece
    if piece.is_path_clear(board, to_pos):
        return True
