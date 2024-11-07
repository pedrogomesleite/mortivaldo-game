from os import path

from game.shared.obj.BackgroundObj import BackgroundObj
from game.shared.obj.MouseObj import MouseObj
from game.shared.handler.baseScene import BaseScene
from game.shared.settings import SETTINGS


class ForcaScene(BaseScene):
    def __init__(self):
        super().__init__()
        mouseobj = MouseObj(path.join(path.join(SETTINGS["SOURCE_DIR"], "sprite"), "cursor-crianca"))
        self.defoultBack = BackgroundObj("cripta.png", "background")
        self.gameBack = BackgroundObj("parede.png", "wordle")
        self.backgroundlayer = [self.defoultBack]
        sceneobjs = [mouseobj]

        # TODO: preencher com objetos do wordle
        self.game = []

        self.gameShow = []
        self.layers = [self.backgroundlayer, self.gameShow, sceneobjs]

    def switchBack(self):
        if self.backgroundlayer[0] == self.defoultBack:
            self.backgroundlayer[0] = self.gameBack
            self.gameShow = self.game
        else:
            self.backgroundlayer[0] = self.defoultBack
            self.gameShow = []

