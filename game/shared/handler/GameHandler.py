class GameHandler:
    def __init__(self, audioHandler, *sceneHandlers):
        self.sceneHandlers = sceneHandlers
        self.scene = "menu"
        self.audioHandler = audioHandler

    # def run(self):


    def setupMenu(self):
        self.scene = "menu"

        self.audioHandler.setupScene("menu", ["Menu.mp3", 0.3], {"click" : ["Click.mp3", 0.3]})
        self.audioHandler.playSceneMusic()

    def setupLevel1(self):
        self.scene = "level1"

        self.audioHandler.setupScene("level1", ["Ambiente 1.mp3", 0.3], {
            "click" : ["Click.mp3", 0.3], "apagar" : ["Apagar Giz.mp3", 0.3], "aparece runa" : ["APARECE RUNA.mp3", 0.3],
            "dialogo A" : ["Diálogo A.mp3", 0.3], "dialogo E" : ["Diálogo E.mp3", 0.3], "dialogo I" : ["Diálogo I.mp3", 0.3],
            "dialogo U" : ["Diálogo U.mp3", 0.3], "giz 1" : ["Giz 1.mp3", 0.3], "giz 2" : ["Giz 2.mp3", 0.3],
            "giz 3" : ["Giz 3.mp3", 0.3], "negativo" : ["NEGATIVO.mp3", 0.3], "positivo" : ["POSITIVO.mp3", 0.3]
        })
        self.audioHandler.playSceneMusic()

    def setupLevel2(self):
        self.scene = "level2"

        self.audioHandler.setupScene("level2", ["Ambiente 2.mp3", 0.3], {
            "click" : ["Click.mp3", 0.3], "aparece runa" : ["APARECE RUNA.mp3", 0.3], "dialogo A" : ["Diálogo A.mp3", 0.3],
            "dialogo E": ["Diálogo E.mp3", 0.3], "dialogo I": ["Diálogo I.mp3", 0.3], "dialogo U": ["Diálogo U.mp3", 0.3],
            "negativo": ["NEGATIVO.mp3", 0.3], "pedras batendo" : ["Pedras Batendo.mp3", 0.3],
            "pegar pedra" : ["Pegar Pedra.mp3", 0.3], "positivo": ["POSITIVO.mp3", 0.3]
        })
        self.audioHandler.playSceneMusic()


    def setupLevel3(self):
        self.scene = "level3"

        self.audioHandler.setupScene("level3", ["Ambiente 3.mp3", 0.3], {
            "click" : ["Click.mp3", 0.3], "aparece runa" : ["APARECE RUNA.mp3", 0.3], "dialogo A" : ["Diálogo A.mp3", 0.3],
            "dialogo E": ["Diálogo E.mp3", 0.3], "dialogo I": ["Diálogo I.mp3", 0.3], "dialogo U": ["Diálogo U.mp3", 0.3],
            "giz 1": ["Giz 1.mp3", 0.3], "negativo" : ["NEGATIVO.mp3", 0.3], "positivo" : ["POSITIVO.mp3", 0.3]
        })
        self.audioHandler.playSceneMusic()

    def setupEndgame(self):
        self.scene = "endgame"

        self.audioHandler.setupScene("endgame", ["Ambiência Final.mp3", 0.3], {
            "click" : ["Click.mp3", 0.3], "aparece runa" : ["APARECE RUNA.mp3", 0.3], "dialogo A" : ["Diálogo A.mp3", 0.3],
            "dialogo E": ["Diálogo E.mp3", 0.3], "dialogo I": ["Diálogo I.mp3", 0.3], "dialogo U": ["Diálogo U.mp3", 0.3],
            "fogo derrota" : ["Fogo da Derrota.mp3", 0.3], "fogo vitoria" : ["Fogo da Vitória.mp3", 0.3],
            "selecionar runa" : ["Selecionar Runa Fase FINAL.mp3", 0.3], "negativo" : ["NEGATIVO.mp3", 0.3]
        })
        self.audioHandler.playSceneMusic()

    def setupCredits(self):
        self.scene = "credits"

        self.audioHandler.setupScene("credits", ["Créditos.mp3", 0.3])
        self.audioHandler.playSceneMusic()

    def nextScene(self):
        return
