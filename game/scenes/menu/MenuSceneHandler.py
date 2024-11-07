import pygame

from game.scenes.menu.MenuScene import MenuScene
from game.shared.handler.baseSceneHandler import BaseSceneHandler
from game.shared.settings import SETTINGS


class MenuSceneHandler(BaseSceneHandler):
    def __init__(self):
        super().__init__()
        self.scene = MenuScene()

    def runState(self, events):
        super().runState(events)

        # for event in events:
