from game.shared.handler.mensageHandler import dialogoHandler


def nextScene(scenes, toShowList):
    for scene in scenes:
        if scene != dialogoHandler:
            scene.run = toShowList[scene.me]
