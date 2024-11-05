import interfaceHandler, loadManager


class BaseSceneHandler:
    """
    Administra as cenas do jogo. Responsável por
    alternar as cenas, chamar as funções de cada
    cena e também a função de checagem de eventos
    relacionados aos elementos de UI.
    """

    def __init__(self):
        self.current_state = None

        self.run = True
        self.loadFonts()

    def loadFonts(self):
        # TODO: fontes especias do game padrão em todas
        # Load fonts
        self.fonts = loadManager.loadFonts(
            [

            ]
        )

    def runState(self, events, layers):
        """
        Chama a função da cena atual.

        Argumentos:
        ---
        - events: eventos do pygame;
        - layers: camadas de renderização.
        """

        # TODO: tratar eventos

        interfaceHandler.handleInterface(events, self, layers)

    def setScene(self, layers):
        """

        Argumentos:
        ---
        - scene_index: índice da cena de destino.
        """

        # TODO: receber os handlers das cenas se desenhar '-'

        self.clearScreen(layers)

    def clearScreen(self, layers):
        """
        Limpa todas as camadas de renderização.
        """

        layers.clear()
        layers.append([])
        layers.append([])

# TODO: transições
