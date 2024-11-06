from game.shared.handler.baseAsset import BaseAsset


class BackgroundObj(BaseAsset):
    def __init__(self, filename, folder):
        super().__init__()
        self.loadStatic(filename, folder)

    def drawSelf(self, screen):
        self.static(screen)
