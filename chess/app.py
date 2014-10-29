

from chess.cursesgame import CursesGame
from chess.game import Game

class App:
    def __init__(self, curses = True):
        if curses:
            self.game = CursesGame()
        else:
            self.game = Game()

        self.game.run()

