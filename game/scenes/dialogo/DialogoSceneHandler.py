from game.scenes.dialogo.DialogoScene import DialogoScene
from game.shared.handler.baseSceneHandler import BaseSceneHandler
from game.shared.handler.loadHandler import loadFonts


class DialogoSceneHandler(BaseSceneHandler):
    def __init__(self):
        super().__init__()
        self.scene = DialogoScene()
