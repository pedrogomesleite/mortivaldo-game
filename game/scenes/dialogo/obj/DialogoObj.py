from game.shared.handler.baseAsset import BaseAsset
from os import path

from game.shared.settings import SETTINGS


class DialogoObj(BaseAsset):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 550
        self.loadStatic("caixa-dialogo.png", path.join(SETTINGS["SOURCE_DIR"], "sprite"))

    def drawSelf(self, screen):
        self.static(screen)
