import pygame

from game.scenes.forca.ForcaScene import ForcaScene
from game.shared.handler.baseSceneHandler import BaseSceneHandler
from game.shared.settings import SETTINGS


class ForcaSceneHandler(BaseSceneHandler):
    def __init__(self):
        super().__init__()
        self.scene = ForcaScene()
        self.square_center = (SETTINGS["SCREEN_SIZE"][0] // 2, SETTINGS["SCREEN_SIZE"][1] // 2)
        self.square_up = 100, 100
        self.isGame = False
        self.run = False

    def runState(self, events):
        super().runState(events)
        for event in events:
            # TODO: eventos do wordle

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not self.isGame:
                    self.clickSwitchBack(event, (self.square_center, 400))
                elif self.isGame:
                    self.clickSwitchBack(event, (self.square_up, 100))

    def clickSwitchBack(self, event, quadrado):
        square_center = quadrado[0]
        square_size = quadrado[1]
        mouse_x, mouse_y = event.pos
        square_left = square_center[0] - square_size // 2
        square_top = square_center[1] - square_size // 2
        square_right = square_left + square_size
        square_bottom = square_top + square_size
        if square_left <= mouse_x <= square_right and square_top <= mouse_y <= square_bottom:
            self.scene.switchBack()
            self.isGame = not self.isGame
