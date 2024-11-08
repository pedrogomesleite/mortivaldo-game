from os import path

from game.scenes.livro.obj.RunasSomaObj import RunasSomaObj
from game.shared.handler.baseScene import BaseScene
from game.shared.obj.BackgroundObj import BackgroundObj
from game.shared.obj.MouseObj import MouseObj
from game.shared.obj.RunasObj import RunasObj
from game.shared.settings import SETTINGS


class LivroScene(BaseScene):
    def __init__(self, font):
        super().__init__()
        mouseobj = MouseObj(path.join(path.join(SETTINGS["SOURCE_DIR"], "sprite"), "cursor-esqueleto"))
        self.defoultBack = BackgroundObj("sala de estudo.png", "background")
        self.gameBack = BackgroundObj("closeup jogo papel sem luz.png", "jogo estudo")
        self.luz = BackgroundObj("closeup jogo papel só luz.png", "jogo estudo")
        self.luzLayer = []
        self.backgroundlayer = [self.defoultBack]

        self.runa = RunasObj(font)
        self.runasPos = self.runa.spritesPos
        self.runaCentro = RunasSomaObj()
        self.keyList = self.runaCentro.keyList

        self.perguntas = [
            BackgroundObj("Pergunta 1.png", "jogo estudo"),
            BackgroundObj("Pergunta 2.png", "jogo estudo"),
            BackgroundObj("Pergunta 3.png", "jogo estudo"),
            BackgroundObj("Pergunta 4.png", "jogo estudo"),
            BackgroundObj("Pergunta 5.png", "jogo estudo")
        ]

        self.textAtual = self.perguntas[0]

        self.display = BackgroundObj("Caixinha Runas Certo.png", "jogo estudo")

        self.game = [self.display, self.runa, self.runaCentro, self.textAtual]

        self.gameShow = []
        self.layers = [self.backgroundlayer, self.gameShow, self.luzLayer, [mouseobj]]

    def switchBack(self):
        if self.backgroundlayer[0] == self.defoultBack:
            self.backgroundlayer[0] = self.gameBack
            self.luzLayer.append(self.luz)
            for item in self.game:
                self.gameShow.append(item)
        else:
            self.backgroundlayer[0] = self.defoultBack
            self.luzLayer.pop(0)
            self.gameShow.clear()

    def setPergunta(self, index):
        self.game.pop(3)
        self.game.append(self.perguntas[index])
        self.textAtual = self.perguntas[index]

        self.gameShow.clear()
        for item in self.game:
            self.gameShow.append(item)

