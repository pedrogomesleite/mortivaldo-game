import pygame

from game.shared.handler.baseSceneHandler import BaseSceneHandler


def renderScene(screen, handler: BaseSceneHandler):
    if handler.run is False:
        return

    layers = handler.scene.layers
    for layer in layers:
        for obj in layer:
            obj.drawSelf(screen)

    # retangulo_cor = (255, 0, 0)  # Cor vermelha para o retângulo
    # retangulo_pos = (800, 500)  # Posição do canto superior esquerdo
    # retangulo_tamanho = (300, 100)  # Largura e altura do retângulo
    #
    # pygame.draw.rect(screen, retangulo_cor, pygame.Rect(retangulo_pos, retangulo_tamanho))
