import pygame
from abc import ABC, abstractmethod

class Tela(ABC):

    def __init__(self) -> None:
        self.gameFont = pygame.font.Font('freesansbold.ttf', 56)
        self.regularFont = pygame.font.Font('fonts/outwrite.ttf', 30)
        self.titleFont = pygame.font.Font('fonts/comicate.ttf', 76)
        self.bgImage = pygame.image.load('images/fundocaderno.jpg')
        self.gray = (48, 48, 48)
        self.white = (255, 255, 255)
        self.lightgray = (104, 104, 104)
        self.green = (19, 122, 53)
        self.yellow = (220, 176, 53)
        self.WIDTH = 500
        self.HEIGHT = 700
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])  # a tela é definida aqui
        pygame.display.set_caption("Palavreado")

    @abstractmethod
    def produzirTela(self) -> None: # aparece tela
        pass