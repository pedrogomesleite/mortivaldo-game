from game.scenes.dialogo.obj.DialogoObj import DialogoObj
from game.shared.handler.baseScene import BaseScene


class DialogoScene(BaseScene):
    def __init__(self):
        super().__init__()
        sceneobjs = [DialogoObj()]
        self.textLayer = []
        self.layers = [sceneobjs, self.textLayer]

    def loadText(self, text):
        self.textLayer.append(text)

    def nextText(self, text):
        if len(self.textLayer) > 0:
            self.textLayer.pop(0)
        self.loadText(text)
