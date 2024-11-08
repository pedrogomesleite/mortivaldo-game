from game.scenes.final.FinalScene import FinalScene
from game.shared.handler.baseSceneHandler import BaseSceneHandler


class FinalSceneHandler(BaseSceneHandler):
    def __init__(self, sceneAtual, index):
        super().__init__(sceneAtual, index)
        self.scene = FinalScene()


