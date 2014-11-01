
from curses import wrapper
from chess.board import Board

class CursesGame:
    def __init__(self):
        # Setup position on screen
        self.offsetX = 0
        self.offsetY = 0

        # Initialize a new board
        self.board = Board.init_board()

    def draw(self, stdscr):
        """Draw the board onto stdscr."""
        for y, row in enumerate(self.board.board):
            for x, piece in enumerate(row):
                # Draw letters for each column
                if y == 0:
                    # Convert x-coordinate to lower case letter in alphabet
                    char = chr(x + 97)
                    stdscr.addch(self.offsetY, x + self.offsetX + 2, char)

                    # Draw horizontal rule
                    stdscr.addch(self.offsetY + 1, x + self.offsetX + 2, '-')
                # Draw numbers for each row
                if x == 0:
                    # Convert y-coordinate to number in sequence [8..1]
                    num = str(8 - y)
                    stdscr.addch(y + self.offsetY + 2, self.offsetX, num)

                    # Draw vertical rule
                    stdscr.addch(y + self.offsetY + 2, self.offsetX + 1, '|')

                # Draw the character at given point onto screen at offset (offsetX, offsetY)
                stdscr.addch(y + self.offsetY + 2, x + self.offsetX + 2,
                        ord(piece.render()))

    def update(self, stdscr):
        """Main game loop, responsible for drawing and input."""
        while True:
            # Clear the screen
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


    def run(self):
        """Launch main game loop."""
        # Setup curses and launch main game update loop
        wrapper(self.update)
