from game.shared.handler.baseAsset import BaseAsset


class TextObj(BaseAsset):
    def __init__(self, text, font, line):
        super().__init__()
        self.spacing = 50
        self.x = 250
        self.y = 720 + line * self.spacing
        self.vel = 2
        self.stopFlag = False
        self.fragText(text, font)

    def drawSelf(self, screen):
        self.animationOnce(screen)

    def fragText(self, text, font):
        for i in range(len(text)):
            sub = text[:i + 1]
            frag = font.render(sub, True, (255, 255, 255))
            self.sprites.append(frag)
