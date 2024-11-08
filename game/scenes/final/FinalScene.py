from os import path

from game.shared.handler.baseScene import BaseScene
from game.shared.obj.BackgroundAnimatedObj import BackgroundAnimatedObj
from game.shared.obj.BackgroundObj import BackgroundObj
from game.shared.settings import SETTINGS


class FinalScene(BaseScene):
    def __init__(self):
        super().__init__()

        self.gameBack = BackgroundObj("FASE FINALL Com Enter.png", "endgame")
        self.animation = BackgroundAnimatedObj(path.join(SETTINGS["SOURCE_DIR"], "sprite", "background endgame"))

        self.layers = [[self.animation, self.gameBack]]
