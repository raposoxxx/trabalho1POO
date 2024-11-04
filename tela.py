import pygame

class Tela:

    def __init__(self) -> None:
        self.gray = (48, 48, 48)
        self.white = (255, 255, 255)
        self.lightgray = (104, 104, 104)
        self.green = (19, 122, 53)
        self.yellow = (220, 176, 53)
        self.WIDTH = 500
        self.HEIGHT = 700
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])  # a tela é definida aqui
        pygame.display.set_caption("Palavreado")

    def produzirTela(self): # aparece tela
        self.screen.fill(self.gray)
    