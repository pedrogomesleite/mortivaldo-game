from game.scenes.forca.MouseObj import MouseObj
from game.shared.handler.baseScene import BaseScene


class ForcaScene(BaseScene):
    def __init__(self):
        super().__init__()
        sceneobjs = [MouseObj()]
        self.layers.append(sceneobjs)
