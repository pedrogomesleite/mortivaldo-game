from pygame import mouse, MOUSEBUTTONDOWN, MOUSEBUTTONUP


class BaseActionHandler:

    def handleEvents(events, scene_manager, layers):

        """
        Função responsável por checar interaçẽos do
        jogador com a interface.

        Argumentos:
        ---
        - events: eventos do pygame;
        - scene_manager:

        """
        # TODO: arrumar o acesso ao scene_manager

        if not mouse.get_pressed()[0]:
            return

        mouse_pos = mouse.get_pos()

        for obj in layers[1]:
            # TODO: implementar herança com eventos de cada scene
            return
        return
