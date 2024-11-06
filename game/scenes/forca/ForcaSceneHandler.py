from game.scenes.forca.ForcaScene import ForcaScene
from game.shared.handler.baseSceneHandler import BaseSceneHandler


class ForcaSceneHandler(BaseSceneHandler):
    def __init__(self):
        super().__init__()
        self.scene = ForcaScene()
        self.fonts = None
