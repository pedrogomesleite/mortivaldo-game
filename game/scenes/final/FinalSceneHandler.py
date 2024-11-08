from game.scenes.final.FinalScene import FinalScene
from game.shared.handler.audioHandler import AudioHandler
from game.shared.handler.baseSceneHandler import BaseSceneHandler


class FinalSceneHandler(BaseSceneHandler):
    def __init__(self, sceneAtual, index):
        super().__init__(sceneAtual, index)
        self.scene = FinalScene()
        self.audio = AudioHandler()
        self.audio.playMusic("music 4")

    def playMusci(self):
        self.audio.playMusic("music 4")
        self.isPlayng = False

