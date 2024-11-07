from game.scenes.dialogo.DialogoSceneHandler import DialogoSceneHandler

dialogoHandler = DialogoSceneHandler()


def sendDialogo(mensagem=""):
    dialogoHandler.setText(mensagem)
