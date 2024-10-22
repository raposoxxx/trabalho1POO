import random
import pygame
from utils import readCSV

class Jogo:

    def __init__(self):
        self.palavras = readCSV('palavras.csv')


    def escolherPalavra(self) -> str:
        palavraEscolhida = random.choice(self.palavras)
        return palavraEscolhida           