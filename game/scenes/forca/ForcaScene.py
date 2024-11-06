from os import path

from game.scenes.forca.Obj.MouseObj import MouseObj
from game.shared.handler.baseScene import BaseScene
from game.shared.settings import SETTINGS


class ForcaScene(BaseScene):
    def __init__(self):
        super().__init__()
        mouseobj = MouseObj(path.join(path.join(SETTINGS["SOURCE_DIR"], "sprite"), "cursor-crianca"))
        sceneobjs = [mouseobj]
        self.layers.append(sceneobjs)
