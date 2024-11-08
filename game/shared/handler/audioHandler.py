import pygame

from game.shared.handler.loadHandler import loadAudio, loadMusic


class AudioHandler:
    def __init__(self):
        self.music = {
            "music 0" : ["music 0.mp3", 0.3],
            "music 1" : ["music 1.mp3", 0.3],
            "music 2" : ["music 2.mp3", 0.3],
            "music 3" : ["music 3.mp3", 0.3],
            "music 4" : ["music 4.mp3", 0.3],
            "music 5" : ["music 5.mp3", 0.3],
        }
        sound_effects = {
            "click" : ["Click.mp3", 0.3, ""],
            "negativo": ["NEGATIVO.mp3", 0.3, ""],
            "positivo": ["POSITIVO.mp3", 0.3, ""],
            "aparece runa": ["APARECE RUNA.mp3", 0.3, ""],
            "giz 1": ["Giz 1.mp3", 0.3, ""],
            "giz 2": ["Giz 2.mp3", 0.3, ""],
            "giz 3": ["Giz 3.mp3", 0.3, ""],
            "apagar": ["Apagar Giz.mp3", 0.3, ""],
            "pegar pedra": ["Pegar Pedra.mp3", 0.3, ""],
            "pedras batendo": ["Pedras Batendo.mp3", 0.3, ""],
            "selecionar runa": ["Selecionar Runa Fase FINAL.mp3", 0.3, ""],
            "fogo derrota": ["Fogo da Derrota.mp3", 0.3, ""],
            "fogo vitoria": ["Fogo da Vitória.mp3", 0.3, ""],
            "A": ["Diálogo A.mp3", 0.3, "dialogo"],
            "E": ["Diálogo E.mp3", 0.3, "dialogo"],
            "I": ["Diálogo I.mp3", 0.3, "dialogo"],
            "U": ["Diálogo U.mp3", 0.3, "dialogo"],
        }
        self.sound_effects = dict()

        for key, value in sound_effects.items():
            self.sound_effects[key] = loadAudio(value[0], value[1], value[2])

    def playMusic(self, name):
        loadMusic(name, "music")
        pygame.mixer.music.set_volume(0.3)
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
