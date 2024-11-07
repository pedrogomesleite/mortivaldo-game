from game.scenes.dialogo.DialogoSceneHandler import DialogoSceneHandler
from game.shared.handler.loadHandler import loadFont

dialogoHandler = DialogoSceneHandler()


def sendDialogo(mensagem=""):
    dialogoHandler.setText(loadFont("TruetypewriterPolyglott.ttf", 50), mensagem)
