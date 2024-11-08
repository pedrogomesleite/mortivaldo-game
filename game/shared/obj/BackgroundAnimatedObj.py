from game.shared.handler.baseAsset import BaseAsset


class BackgroundAnimatedObj(BaseAsset):
    def __init__(self, folder):
        super().__init__()
        self.loadAnimation(folder)

    def drawSelf(self, screen):
        self.animation(screen)
