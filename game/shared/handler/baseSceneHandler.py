from game.shared.handler.loadHandler import loadFont
from game.shared.settings import SETTINGS


class BaseSceneHandler:
    """
    Administra as cenas do jogo. Responsável por
    alternar as cenas, chamar as funções de cada
    cena e também a função de checagem de eventos
    relacionados aos elementos de UI.
    """

    def __init__(self, sceneAtual, index):
        # TODO: iniciar as variaveis de cena
        self.fonts = None
        self.scene = None
        self.me = index
        self.run = sceneAtual[index]
        self.sceneAtual = sceneAtual
        self.loadFont()
        self.isPlayng = True

    def loadFont(self):
        # TODO: fontes especias do game padrão em todas
        # Load fonts
        self.fonts = loadFont("TruetypewriterPolyglott.ttf", SETTINGS["TEXT_SIZES"][2])

    def runState(self, events):
        """
        Chama a função da cena atual.

        Argumentos:
        ---
        - events: eventos do pygame;
        """

        self.scene.gameLoop()

        if self.run is False:
            self.scene.resetScene()
            return

        # TODO: tratar eventos com heranca usando o baseActionHandler

    def clearScreen(self):
        """
        Limpa todas as camadas de renderização.
        """

        self.scene.layers.clear()
        self.scene.layers.append([])
        self.scene.layers.append([])

    def transicao(self, index):
        self.run = False
        self.sceneAtual[self.me] = False
        self.sceneAtual[index] = True

    def playMusci(self):
        pass

# TODO: transições
