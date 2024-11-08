from os import path

from game.shared.handler.baseAsset import BaseAsset
from game.shared.handler.loadHandler import loadAllSpritesFromDirectoryScale
from game.shared.settings import SETTINGS


class RunasObj(BaseAsset):
    def __init__(self, factor=0.15):
        super().__init__()
        self.loadAnimation(path.join(path.join(SETTINGS["SOURCE_DIR"], "sprite", "runas")), factor)
        lin = [600, 700, 800, 900, 1000, 450]
        col = [700, 816, 1032, 1150, 924, 650, 1200]
        self.spritesPos = {
            "alma": [(col[0], lin[0]), self.sprites[0]],
            "comeco": [(col[1], lin[0]), self.sprites[1]],
            "magia": [(col[2], lin[0]), self.sprites[2]],
            "veneno": [(col[3], lin[0]), self.sprites[3]],
            "doenca": [(col[0], lin[1]), self.sprites[4]],
            "fraqueza": [(col[1], lin[1]), self.sprites[5]],
            "maldicao": [(col[2], lin[1]), self.sprites[6]],
            "poder": [(col[3], lin[1]), self.sprites[7]],
            "ressureicao": [(col[0], lin[2]), self.sprites[8]],
            "vida": [(col[1], lin[2]), self.sprites[9]],
            "desespero": [(col[2], lin[2]), self.sprites[10]],
            "desgraca": [(col[3], lin[2]), self.sprites[11]],
            "eternidade": [(col[0], lin[3]), self.sprites[12]],
            "humano": [(col[1], lin[3]), self.sprites[13]],
            "praga": [(col[2], lin[3]), self.sprites[14]],
            "ruina": [(col[3], lin[3]), self.sprites[15]],
            "sangue": [(col[4], lin[1]), self.sprites[16]],
            "trevas": [(col[4], lin[2]), self.sprites[17]],
            "acao": [(col[5], lin[5]), self.sprites[18]],
            "negacao": [(col[6], lin[5]), self.sprites[19]],
        }

    def drawSelf(self, screen):

        for key, value in self.spritesPos.items():
            position = value[0]
            sprite = value[1]
            screen.blit(sprite, position)

    def loadAnimation(self, folder="", factor=0.15):
        self.sprites = loadAllSpritesFromDirectoryScale(folder, scale_factor=factor)

    def setSpritePos(self, positions: []):
        for i, (key, _) in enumerate(self.spritesPos.items()):
            self.spritesPos[key][0] = positions[i]

    def changePos(self, key, pos):
        if key in self.spritesPos:
            self.spritesPos[key] = pos
