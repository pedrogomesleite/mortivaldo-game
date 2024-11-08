import pygame

from game.scenes.livro.LivroScene import LivroScene
from game.shared.handler.baseSceneHandler import BaseSceneHandler
from game.shared.handler.loadHandler import loadFont
from game.shared.handler.nextSceneHandler import nextScene
from game.shared.settings import SETTINGS


def isInside(pos, posRuna, size):
    x1, y1 = pos
    x2, y2 = posRuna

    return x2 <= x1 <= x2 + size and y2 <= y1 <= y2 + size


def isInsideRet(pos, posRuna, largura, altura):
    x1, y1 = pos
    x2, y2 = posRuna

    return x2 <= x1 <= x2 + largura and y2 <= y1 <= y2 + altura


class LivroSceneHandler(BaseSceneHandler):
    def __init__(self, sceneAtual, index):
        super().__init__(sceneAtual, index)
        self.center = None
        self.negacao = "negacao"
        self.acao = "acao"
        self.scene = LivroScene(self.fonts)
        self.square_center = (SETTINGS["SCREEN_SIZE"][0] // 2, (SETTINGS["SCREEN_SIZE"][1] // 2 + 350))
        self.square_up = 100, 100
        self.isGame = False

        self.respostas = [
            ["comeco", "negacao"],
            ["vida", "negacao", "acao"],
            ["maldicao", "acao"],
            ["veneno", "negacao", "acao"],
            ["trevas", "negacao", "acao"]
        ]
        self.perguntaAtual = 0

    def loadFont(self):
        # TODO: fontes especias do game padrão em todas
        # Load fonts
        self.fonts = loadFont("TruetypewriterPolyglott.ttf", SETTINGS["TEXT_SIZES"][5])

    def runState(self, events):
        super().runState(events)
        for event in events:
            # TODO: eventos do wordle



            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.confirmar(event.pos)
                if not self.isGame:
                    self.clickSwitchBack(event, (self.square_center, 400))
                elif self.isGame:
                    self.clickSwitchBack(event, (self.square_up, 100))
                if self.isGame:
                    self.verify(event.pos)

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

    def verify(self, pos):
        spritesPos = self.scene.runasPos
        keyList = self.scene.keyList
        for item in spritesPos:
            runa = spritesPos[item]
            if isInside(pos, runa[0], runa[1].get_width()):
                if item != "acao" and item != "negacao":
                    if self.center in keyList:
                        keyList.remove(self.center)
                    self.center = item
                    keyList.append(self.center)

                if item == "acao":
                    if self.acao not in keyList:
                        keyList.append(self.acao)
                    elif self.acao in keyList:
                        keyList.remove(self.acao)

                if item == "negacao":
                    if self.negacao not in keyList:
                        keyList.append(self.negacao)
                    elif self.negacao in keyList:
                        keyList.remove(self.negacao)

    def confirmar(self, pos):
        if isInsideRet(pos, (800, 500), 300, 100):
            keyList = self.scene.keyList
            if len(keyList) == 0:
                return
            perguntaAtual = self.respostas[self.perguntaAtual]
            for item in keyList:
                if item not in perguntaAtual:
                    # TODO: som de fracasso
                    return
            self.perguntaAtual += 1
            print(self.perguntaAtual, len(self.respostas))
            if self.perguntaAtual == len(self.respostas):
                self.transicao(self.me + 1)
                return
            self.scene.setPergunta(self.perguntaAtual)
            # TODO: som de sucesso
