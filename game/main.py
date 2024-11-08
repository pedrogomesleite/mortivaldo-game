import pygame
import sys
from os import path
from screeninfo import get_monitors

from pygame import display

from game.scenes.dialogo.DialogoSceneHandler import DialogoSceneHandler
from game.scenes.livro.LivroSceneHandler import LivroSceneHandler
from scenes.forca.ForcaSceneHandler import ForcaSceneHandler
from shared.handler import render
from shared.settings import SETTINGS
from shared.handler.audioHandler import AudioHandler
from shared.handler.loadHandler import loadSprite

# Obtém a resolução do monitor (qualquer monitor)
monitor = get_monitors()[0]
screen_size = (monitor.width, monitor.height)

SETTINGS["SCREEN_SIZE"] = screen_size

# Pygame setup
pygame.init()

# TODO: fullscreen, adaptabilidade ao moniotr?


SCREEN = pygame.display.set_mode(SETTINGS["SCREEN_SIZE"], pygame.FULLSCREEN)
pygame.display.set_caption("Mortivaldo game")
pygame.display.set_icon(loadSprite("3 Eternidade.png", folder_name="runas"))
clock = pygame.time.Clock()

# TODO: importar esse vetor em todos os handlers e na iniciação
# TODO: [forca, juntar, livro, final, dialogo]

# IMPORTANT: deixa esse import aqui sem ele NÃO VAI FUNCIONAR
from game.shared.handler.mensageHandler import sendDialogo, dialogoHandler

scenesHandlers = [ForcaSceneHandler(), LivroSceneHandler(), dialogoHandler]
audioHandler = AudioHandler()
current_state = None

pygame.mouse.set_visible(False)


def main():
    # TODO: iniciar o menu
    while True:
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill((0, 0, 0))

        for handler in scenesHandlers:
            handler.runState(events)
            render.renderScene(SCREEN, handler)

        display.update()

        clock.tick(SETTINGS["FPS"])


if __name__ == "__main__":
    main()
