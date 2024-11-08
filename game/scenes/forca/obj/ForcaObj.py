from game.shared.handler.baseAsset import BaseAsset
from game.shared.handler.loadHandler import loadSprite


class ForcaObj(BaseAsset):
    def __init__(self, x, y):
        self.guess = None
        self.x = x
        self.y = y

        self.sprites = {
            "blank" : [loadSprite("linha.png", folder_name="wordle"), x, y],
            "guess" : [],
            "hint" : []
        }


    def setLetter(self, font, size, guess):
        self.guess = guess
        self.sprites["guess"] = [font.render(guess, size)]

        self.sprites["guess"][1] = self.x + (self.sprites["blank"][0].get_size()[0] - self.sprites["guess"][0].get_size()[0]) / 2
        self.sprites["guess"][2] = self.y + self.sprites["guess"][0].get_size()[1] + 20

    def setHint(self, font, size, hint):
        self.sprites["hint"] = [font.render(hint, size)]

        self.sprites["hint"][1] = self.x + (self.sprites["blank"][0].get_size()[0] - self.sprites["hint"][0].get_size()[0]) / 2
        self.sprites["hint"][2] = self.y + self.sprites["guess"][2] + 10



    def drawSelf(self, screen):
        for i in self.sprites.values():
            screen.blit(i[0], (i[1], i[2]))