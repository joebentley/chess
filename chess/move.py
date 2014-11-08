
def check_move(board, from_pos, to_pos):
    """Check whether the move from (from_pos) to (to_pos) would be
       a valid move in chess. That is, are there pieces in the way?
       Can the piece move like this?

       Returns True if the piece can make that move, else False.

       Keyword arguments:
       board    (Board) -- current game board
       from_pos (Point) -- position containing piece that wants to move
       to_pos   (Point) -- position the piece wants to move to"""

    # Get piece from position
    piece = board.getsquare(from_pos)

    # Check if piece could move there on an _empty_ board or trying to move offscreen
    if not piece.valid_move(board, to_pos) or not board.point_on_board(to_pos):
        return False
    # Check if another piece at destination and it's the same colour, the move is invalid
    if board.piece_at(to_pos) and board.getsquare(to_pos).color == piece.color:
        return False

    return True
