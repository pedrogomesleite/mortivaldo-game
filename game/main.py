import pygame
import sys

from game.shared.handler import render
from game.shared.settings import SETTINGS

# Pygame setup
pygame.init()

SCREEN = pygame.display.set_mode(SETTINGS["SCREEN_SIZE"], )
pygame.display.set_caption("Jogo da Cobrinha")
clock = pygame.time.Clock()

# TODO: importar esse vetor em todos os handlers e na iniciação
# TODO: [forca, juntar, livro, final, dialogo]
scenesHandlers = []
current_state = None

pygame.mouse.set_visible(False)
pygame.mouse.set

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
