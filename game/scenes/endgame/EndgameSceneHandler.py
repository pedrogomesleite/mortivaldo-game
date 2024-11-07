import pygame

from game.scenes.endgame.EndgameScene import EndgameScene
from game.shared.handler.baseSceneHandler import BaseSceneHandler
from game.shared.settings import SETTINGS


class ForcaSceneHandler(BaseSceneHandler):
    def __init__(self):
        super().__init__()
        self.scene = EndgameScene()

    def runState(self, events):
        super().runState(events)

        # for event in events: