from game.shared.handler.baseAsset import BaseAsset


class TextObj(BaseAsset):
    def __init__(self, text, font):
        super().__init__()
        self.x = 250
        self.y = 720
        self.vel = 2
        self.stopFlag = False
        self.formtText(text)
        self.fragText(text, font)

    def drawSelf(self, screen):
        self.animationOnce(screen)

    def fragText(self, text, font):
        for i in range(len(text)):
            sub = text[-i - 1:]
            frag = font.render(sub, True, (255, 255, 255))
            self.sprites.append(frag)

    def formtText(self, text):
        # TODO: formamtar o texto com as quebras de linhas
        return
