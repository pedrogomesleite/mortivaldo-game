import pygame

from game.shared.handler.loadHandler import loadAudio, loadMusic


class AudioHandler:
    def __init__(self):
        self.music = None
        self.sound_effects = None

    def setupScene(self, folder_name, music: list = None, sound_effects: dict = None):
        """
        Função que prepara todos os sons da cena.

        Argumentos:
        - music: lista no formato [<nome do arquivo>, <volume>];
        - sound_effects: dicionário no formato {<nome do som> : [<nome do arquivo>, <volume>]}
        """
        # self.music = loadAudio(music[0], music[1], folder_name)
        if music:
            loadMusic(music[0], music[1], folder_name)
        if sound_effects:
            self.sound_effects = dict()
            for key, value in sound_effects.items():
                self.sound_effects[key] = loadAudio(value[0], value[1], folder_name)

    def playSceneMusic(self):
        pygame.mixer.music.play(-1)

    def playSoundEffect(self, name):
        self.sound_effects[name].play()

    def stopMusic(self):
        pygame.mixer.music.stop()

    def stopSoundEffects(self):
        pygame.mixer.stop()

    def stopAllSound(self):
        # pygame.mixer.stop()
        self.stopMusic()
        self.stopSoundEffects()
