from game.shared.handler.baseAsset import BaseAsset


class TextObj(BaseAsset):
    def __init__(self, text, font):
        super().__init__()
        self.x = 250
        self.y = 720
        self.vel = 2
        self.stopFlag = False
        self.text = self.formtText(text, font)
        self.fragText(self.text, font)

    def drawSelf(self, screen):
        self.animationOnce(screen)

    def fragText(self, text, font):
        for i in range(len(text)):
            sub = text[:i + 1]
            frag = font.render(sub, True, (255, 255, 255))
            self.sprites.append(frag)

    def formtText(self, text, font):
        # TODO: formamtar o texto com as quebras de linhas
        if font.size(text)[0] < 1400:
            return text

        line_breaks = []

        j = 0
        for i in range(len(text.split())):
            if font.size(" ".join(text.split()[j:i + 1]))[0] >= 1400:
                # TODO: separar o texto em linhas. o font.render n considera quebras de linha
                line_breaks.append(i + 1)
                j = i + 1
                print("line break at", i)

        for i in range(len(line_breaks)):
            new_text = text.split()
            new_text.insert(line_breaks[i] + i, '\n')

        print(new_text, "EBA")

        return " ".join(new_text)

