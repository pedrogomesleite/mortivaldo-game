import pygame

from game.shared.handler.loadHandler import loadAudio, loadMusic

class AudioHandler:
    def __init__(self):
        self.music = None
        self.sound_effects = None

    def setupScene(self, folder_name, music:list, sound_effects:dict=dict()):
        """
        Função que prepara todos os sons da cena.

        Argumentos:
        - music: lista no formato [<nome do arquivo>, <volume>];
        - sound_effects: dicionário no formato {<nome do som> : [<nome do arquivo>, <volume>]}
        """
        # self.music = loadAudio(music[0], music[1], folder_name)
        loadMusic(music[0], music[1], folder_name)
        for key, value in sound_effects.items():
            self.sound_effects[key] = loadAudio(value[0], value[1], folder_name)
        return

    def playSceneMusic(self):
        pygame.mixer.music.play(-1)

    def playSoundEffect(self, code):
        return

    def interruptAllSound(self):
        pygame.mixer.stop()
        return
