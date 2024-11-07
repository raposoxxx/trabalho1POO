import pygame
from tela import Tela

pygame.init()

class TelaFinal(Tela):
    
    def __init__(self) -> None:
        super().__init__()

    def produzirTela(self) -> None:
        self.screen.blit(self.finalbgimage, (0, 0))

    def mostrarResultado(self) -> None:
        self.screen.blit(self.title, (100, 50))
        