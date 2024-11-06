from os import path

from game.shared.obj.BackgroundObj import BackgroundObj
from game.shared.obj.MouseObj import MouseObj
from game.shared.handler.baseScene import BaseScene
from game.shared.settings import SETTINGS


class ForcaScene(BaseScene):
    def __init__(self):
        super().__init__()
        mouseobj = MouseObj(path.join(path.join(SETTINGS["SOURCE_DIR"], "sprite"), "cursor-esqueleto"))
        bckobj = BackgroundObj("cripta.png", "background")
        backgroundlayer = [bckobj]
        sceneobjs = [mouseobj]
        self.layers.append(backgroundlayer)
        self.layers.append(sceneobjs)
