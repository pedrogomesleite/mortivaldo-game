from game.scenes.dialogo.obj.DialogoObj import DialogoObj
from game.shared.handler.baseScene import BaseScene


class DialogoScene(BaseScene):
    def __init__(self):
        super().__init__()
        sceneobjs = [DialogoObj()]
        self.layers.append(sceneobjs)
