
from curses import wrapper
from chess.board import Board

class CursesGame:
    def __init__(self):
        # Setup position on screen
        self.offsetX = 2
        self.offsetY = 2

        # Initialize a new board
        self.board = Board.initBoard()

    # Draw board onto the screen
    def draw(self, stdscr):
        for y in range(len(self.board.board)):
            for x in range(len(self.board.board[y])):
                # Draw the character at given point onto screen at offset (offsetX, offsetY)
                stdscr.addch(y + self.offsetY, x + self.offsetX,
                        ord(self.board.board[y][x].render()))

    # Main game loop, responsible for input and drawing
    def update(self, stdscr):
        while True:
            stdscr.clear()

            # Draw the board
            self.draw(stdscr)

            # Get key input
            key = stdscr.getkey()

            # Quit if q pressed
            if key == 'q':
                return

            # Refresh the window
            stdscr.refresh()



    # Launch main game update loop
    def run(self):
        # Setup curses and launch main game update loop
        wrapper(self.update)
