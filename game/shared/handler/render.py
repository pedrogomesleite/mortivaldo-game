from pygame import display, transform, draw

from game.shared.handler.baseSceneHandler import BaseSceneHandler


def renderScene(screen, handler: BaseSceneHandler):
    layers = handler.scene.layers
    for layer in layers:
        for obj in layer:
            obj.drawSelf(screen)

    display.update()
