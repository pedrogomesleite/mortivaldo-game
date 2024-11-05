from pygame import display, transform, draw


def renderScene(screen, handler):
    layers = handler.scene.layers
    for layer in layers:
        for obj in layer:
            obj.drawSelf(screen)

    display.update()
