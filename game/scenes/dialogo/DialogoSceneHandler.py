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

    def setText(self, font, text="", box_size=1200):
        if font.size(text)[0] < box_size:
            return text

        lines = []

        j = 0
        for i in range(len(text.split())):
            if font.size(" ".join(text.split()[j:i + 1]))[0] >= box_size:
                # TODO: separar o texto em linhas. o font.render n considera quebras de linha

                print(text.split()[j:i])

                lines.append(" ".join(text.split()[j:i]))
                j = i
        lines.append(" ".join(text.split()[j:]))

        for i in range(len(lines)):
            textObj = TextObj(lines[i], self.fonts, i)
            self.texts.append(textObj)

            # NOTE: se pá tem q devolver essa linha pro código
            # if len(self.scene.textLayer) == 0:
            self.scene.loadText(textObj)
            self.run = True
