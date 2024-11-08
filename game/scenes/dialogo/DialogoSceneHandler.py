import pygame

from game.scenes.dialogo.DialogoScene import DialogoScene
from game.scenes.dialogo.obj.TextObj import TextObj
from game.shared.handler.baseSceneHandler import BaseSceneHandler


class DialogoSceneHandler(BaseSceneHandler):
    def __init__(self):
        super().__init__()
        self.scene = DialogoScene()
        self.texts = []

    def runState(self, events):
        # TODO: manipular evento de enter
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(self.texts) > 1:
                        self.scene.nextText(self.texts.pop(1))
                    else:
                        self.texts = []
                        self.run = False
        super().runState(events)

    def setText(self, text=""):
        textobgj = TextObj(text, self.fonts)
        self.texts.append(textobgj)
        if len(self.scene.textLayer) == 0:
            self.scene.loadText(textobgj)
            self.run = True
