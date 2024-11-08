from os import path

from game.scenes.livro.obj.RunasSomaObj import RunasSomaObj
from game.shared.handler.baseScene import BaseScene
from game.shared.obj.BackgroundObj import BackgroundObj
from game.shared.obj.MouseObj import MouseObj
from game.shared.obj.RunasObj import RunasObj
from game.shared.settings import SETTINGS


class LivroScene(BaseScene):
    def __init__(self):
        super().__init__()
        mouseobj = MouseObj(path.join(path.join(SETTINGS["SOURCE_DIR"], "sprite"), "cursor-esqueleto"))
        self.defoultBack = BackgroundObj("sala de estudo.png", "background")
        self.gameBack = BackgroundObj("papel.png", "livro")
        self.backgroundlayer = [self.defoultBack]

        self.runa = RunasObj()
        self.runasPos = self.runa.spritesPos
        self.runaCentro = RunasSomaObj()
        self.keyList = self.runaCentro.keyList
        self.game = [self.runa, self.runaCentro]

        self.gameShow = []
        self.layers = [self.backgroundlayer, self.gameShow, [mouseobj]]

    def switchBack(self):
        if self.backgroundlayer[0] == self.defoultBack:
            self.backgroundlayer[0] = self.gameBack
            for item in self.game:
                self.gameShow.append(item)
        else:
            self.backgroundlayer[0] = self.defoultBack
            self.gameShow.clear()
