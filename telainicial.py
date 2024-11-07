import pygame
from tela import Tela

tela = Tela()

pygame.init()

class TelaInicial(Tela):
    def __init__(self) -> None:
        super().__init__()
    
    def produzirTela(self) -> None:
        self.screen.blit(self.bgImage, (0, 0))

    def produzirInicio(self) -> None:
        text1 = self.regularFont.render("BEM VINDO AO", True, self.black)
        text2 = self.titleFont.render("PALAVREADO", True, self.black)
        text3 = self.regularFont.render("Aperte qualquer tecla", True, self.black)
        self.screen.blit(text1, (130, 125))
        self.screen.blit(text2, (30, 170))
        self.screen.blit(text3, (50, 600))