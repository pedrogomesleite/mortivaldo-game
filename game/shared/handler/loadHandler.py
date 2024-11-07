import os

import pygame.mixer
from pygame import image, font, Surface, color

from game.shared.settings import SETTINGS

pygame.font.init()


def loadSpriteSheet(file_name: str, unit_size, tiles: list[int] = [1, 1], color_key: color.Color = (255, 255, 255, 255),
                    folder_name=""):
    """
	Carrega sprites diferentes de um mesmo arquivo.
	Todas são quadradas e têm o mesmo comprimento.

    Argumentos:
    ---
	- flie_name: nome do arquivo;
	- tiles: nº de linhas e nº de colunas, respect.;
	- color_key: cor do fundo;
	- folder_name: nome da pasta do arquivo.
    """

    original = image.load(os.path.join(SETTINGS["SOURCE_DIR"], "graphics", folder_name, file_name)).convert()
    sprites = []
    sprite_index = 0

    for i in range(tiles[0]):
        for j in range(tiles[1]):
            sprites.append(Surface((unit_size, unit_size)))
            sprites[sprite_index].blit(original, (0, 0), (j * unit_size, i * unit_size, unit_size, unit_size))
            sprites[sprite_index].set_colorkey(color_key)
            sprites[sprite_index].convert()
            sprite_index += 1

    return sprites


def loadAllSpritesFromDirectory(directory: str, color_key: tuple = (255, 255, 255)):
    """
    Carrega todas as imagens de um diretório e as retorna em uma lista.

    Argumentos:
    directory : str
        O diretório onde as imagens estão localizadas.
    color_key : tuple
        A cor do fundo a ser removida das imagens (transparência).

    Retorna:
    list
        Uma lista contendo as superfícies (sprites) carregadas de todas as imagens.
    """
    sprites = []

    if not os.path.isdir(directory):
        raise ValueError(f"O diretório {directory} não existe.")

    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            file_path = os.path.join(directory, filename)

            img = image.load(file_path).convert_alpha()
            img.set_colorkey(color_key)
            sprites.append(img)

    return sprites


def loadSprite(file_name, color_key: color.Color = (255, 255, 255, 255), folder_name=""):
    """
	Carrega uma única sprite.

    Argumentos:
    ---
	- flie_name: nome do arquivo;
	- color_key: cor do fundo;
	- folder_name: nome da pasta do arquivo.
	"""

    surface = image.load(os.path.join(SETTINGS["SOURCE_DIR"], "sprite", folder_name, file_name)).convert_alpha()
    if color_key != ():
        surface.set_colorkey(color_key)
    return surface


def loadFont(fontName: "", size):
    """
	Carrega as fontes requeridas.

    Argumentos:
    ---
	- `*requests`: fontes a carregar; cada request é no formato [<nome do arquivo>:str, <tamanho da fonte>:int].
    """

    fonts = font.Font(os.path.join(SETTINGS["SOURCE_DIR"], "fonts", fontName), size)
    return fonts


# TODO: Função que manipula o objeto de animação

def loadMusic(file_name, volume, folder_name=""):
    pygame.mixer.music.load(os.path.join(SETTINGS["SOURCE_DIR"], "audio", folder_name, file_name))


def loadAudio(file_name, volume=0.3, folder_name=""):
    """
    Carrega um arquivo de áudio.

    Argumentos:
    - file_name: nome do arquivo;
    - volume: volume do áudio.
    - folder_name: nome da pasta específica do arquivo;
    """
    audio = pygame.mixer.Sound(os.path.join(SETTINGS["SOURCE_DIR"], "audio", folder_name, file_name))
    audio.set_volume(volume)

    return audio
