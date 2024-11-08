from game.shared.obj.RunasObj import RunasObj


class RunasSomaObj(RunasObj):
    def __init__(self):
        super().__init__(None, 0.5)
        pos = (840, 240)
        newPos = []
        for i in range(len(self.sprites)):
            newPos.append(pos)
        self.setSpritePos(newPos)
        self.negacao = "negacao"
        self.acao = "acao"
        self.center = None
        self.keyList = []

    def drawSelf(self, screen):
        for i, key in enumerate(self.keyList):
            runa = self.spritesPos[key][0]
            screen.blit(self.spritesPos[key][1], runa)
