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
                    self.run = False
        super().runState(events)

    def setText(self, text=""):
        self.texts.append(text)
        textobgj = TextObj(self.fonts.render(text, True, (255, 255, 255)))
        self.scene.loadText(textobgj)
        self.run = True
