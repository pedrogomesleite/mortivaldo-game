import pygame
import sys
from os import path
from screeninfo import get_monitors

from pygame import display

from game.scenes.dialogo.DialogoSceneHandler import DialogoSceneHandler
from scenes.forca.ForcaSceneHandler import ForcaSceneHandler
from shared.handler import render
from shared.settings import SETTINGS
from shared.handler.audioHandler import AudioHandler
from shared.handler.loadHandler import loadSprite
from shared.handler.GameHandler import GameHandler

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

gameHandler = GameHandler(ForcaSceneHandler(), dialogoHandler)
# scenesHandlers = [ForcaSceneHandler(), dialogoHandler]
audioHandler = AudioHandler()
current_state = None

pygame.mouse.set_visible(False)


def main():
    # TODO: iniciar o menu
    sendDialogo("11111111111 222222222 3333333333 4444444 55555555 6666666666 77777777 88888888")
    sendDialogo("tsete2")
    sendDialogo("tsete3")

    while True:

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameHandler.sceneHandlers[0].scene.startForca()

        SCREEN.fill((0, 0, 0))

        for handler in gameHandler.sceneHandlers:
            handler.runState(events)
            render.renderScene(SCREEN, handler)

        display.update()

        clock.tick(SETTINGS["FPS"])


if __name__ == "__main__":
    main()
