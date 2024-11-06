import pygame
import sys

from game.scenes.dialogo.DialogoSceneHandler import DialogoSceneHandler
from scenes.forca.ForcaSceneHandler import ForcaSceneHandler
from shared.handler import render
from shared.settings import SETTINGS
from shared.handler.audioHandler import AudioHandler

# Pygame setup
pygame.init()

# TODO: fullscreen, adaptabilidade ao moniotr?

SCREEN = pygame.display.set_mode(SETTINGS["SCREEN_SIZE"])
pygame.display.set_caption("Mortivaldo game")
# pygame.display.set_icon()
clock = pygame.time.Clock()

# TODO: importar esse vetor em todos os handlers e na iniciação
# TODO: [forca, juntar, livro, final, dialogo]
scenesHandlers = [ForcaSceneHandler(), DialogoSceneHandler()]
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

        for handler in scenesHandlers:
            handler.runState(events)
            render.renderScene(SCREEN, handler)

        clock.tick(SETTINGS["FPS"])


if __name__ == "__main__":
    main()
