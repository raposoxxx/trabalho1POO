import random
import pygame
from utils import readJson

class Jogo:

    def __init__(self):
        self.palavras = readJson('palavras.json')


    def escolherPalavra(self) -> str:
        palavraEscolhida = random.choice(self.palavras)
        return palavraEscolhida           