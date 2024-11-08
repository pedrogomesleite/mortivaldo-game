from game.shared.handler.baseAsset import BaseAsset


class TextObj(BaseAsset):
    def __init__(self, text, font):
        super().__init__()
        self.x = 250
        self.y = 720
        self.vel = 2
        self.stopFlag = False
        self.formtText(text)
        self.fragText(text, font)

    def drawSelf(self, screen):
        self.animationOnce(screen)

    def fragText(self, text, font, max_width=50, max_height=200):
        current_line = ""
        current_height = 0

        # Loop para processar o texto caractere por caractere
        for i in range(len(text)):
            sub = text[:i + 1]  # Substring com os caracteres até o índice atual
            frag = font.render(sub, True, (255, 255, 255))

            # Verifique a largura da superfície (frag) e o total de altura
            if frag.get_width() > max_width or current_height + frag.get_height() > max_height:
                # Se ultrapassar o limite, adicione a linha anterior como um fragmento
                if current_line:
                    line_surface = font.render(current_line, True, (255, 255, 255))
                    self.sprites.append(line_surface)  # Adiciona à lista de sprites
                    current_line = ""  # Reseta a linha atual
                    current_height = 0  # Reseta a altura da linha

                # Adiciona o fragmento atual como uma nova linha
                self.sprites.append(frag)
                current_height = frag.get_height()  # Atualiza a altura da nova linha
            else:
                # Caso contrário, adicione o caractere à linha atual
                current_line += text[i]

        # Após o loop, verifique se há alguma linha restante para adicionar
        if current_line:
            line_surface = font.render(current_line, True, (255, 255, 255))
            self.sprites.append(line_surface)

    def formtText(self, text):
        # TODO: formamtar o texto com as quebras de linhas
        return
