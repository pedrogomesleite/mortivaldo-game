from game.shared.handler.loadHandler import loadFonts

class BaseSceneHandler:
    """
    Administra as cenas do jogo. Responsável por
    alternar as cenas, chamar as funções de cada
    cena e também a função de checagem de eventos
    relacionados aos elementos de UI.
    """

    def __init__(self):
        # TODO: iniciar as variaveis de cena
        self.fonts = None
        self.scene = None
        self.current_state = None
        self.run = True
        self.loadFonts()
        self.setScene()

    def loadFonts(self):
        # TODO: fontes especias do game padrão em todas
        # Load fonts
        self.fonts = loadFonts(
            [

            ]
        )

    def runState(self, events):
        """
        Chama a função da cena atual.

        Argumentos:
        ---
        - events: eventos do pygame;
        """

        if self.current_state is False:
            self.scene.resetScene()
            return

        # TODO: tratar eventos com heranca usand o baseActionHandler

    def clearScreen(self, scene):
        """
        Limpa todas as camadas de renderização.
        """

        self.scene.layers.clear()
        self.scene.layers.append([])
        self.scene.layers.append([])

# TODO: transições
