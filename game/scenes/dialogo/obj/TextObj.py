from game.shared.handler.baseAsset import BaseAsset


class TextObj(BaseAsset):
    def __init__(self, textSurface):
        super().__init__()
        self.x = 250
        self.y = 720
        self.sprite = textSurface

    def drawSelf(self, screen):
        self.static(screen)
