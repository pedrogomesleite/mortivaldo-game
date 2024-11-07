import pygame, sys

from game.shared.handler.baseScene import BaseScene

class MenuScene(BaseScene):
    def __init__(self):
        super().__init__()

    def startGame(self):
        self.run = False

    def ExitGame(self):
        pygame.quit()
        sys.exit()