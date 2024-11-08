from os import path

from game.shared.obj.BackgroundObj import BackgroundObj
from game.shared.obj.MouseObj import MouseObj
from game.shared.handler.baseScene import BaseScene
from game.shared.settings import SETTINGS
from game.scenes.forca.obj.ForcaObj import ForcaObj

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

        # TODO: os objetos do gameShow só renderizam quando a caixa de diálogo ainda não saiu
        #       quando a caixa sai, eles não renderizam
        self.gameShow = []
        self.layers = [self.backgroundlayer, self.gameShow, sceneobjs]


        self.passwords = ["Alma", "Começo", "Veneno"]
        self.spacing = 40


    def switchBack(self):
        if self.backgroundlayer[0] == self.defoultBack:
            self.backgroundlayer[0] = self.gameBack
            self.gameShow = self.game
        else:
            self.backgroundlayer[0] = self.defoultBack
            self.gameShow = []

    def startForca(self):
        # TODO: chamar a troca de background
        self.progress = 0
        self.word = self.passwords[self.progress]

        for i in range(len(self.passwords[self.progress])):
            self.game.append(ForcaObj(
                SETTINGS["SCREEN_SIZE"][0] + (len(self.word) / 2) * self.spacing,
                SETTINGS["SCREEN_SIZE"][1] - 30
            ))

            self.gameShow = self.game[:]


    def nextWord(self):
        self.progress += 1
