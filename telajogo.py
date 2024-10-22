import pygame
from jogo import Jogo
from tela import Tela

pygame.init()

jogo = Jogo()

white = (255, 255, 255)
gray = (48, 48, 48)
green = (19, 122, 53)
yellow = (220, 176, 53)
    
titleFont = pygame.font.Font('freesansbold.ttf', 56)
turnActive = True


class TelaJogo(Tela):

    def __init__(self):
        super().__init__(white, gray, green, yellow)
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])  # a tela é definida aqui
        pygame.display.set_caption("Palavreado")

        self.board = [[" ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " "]]
        
        self.turn = 0
        self.letters = 0
        self.palavra = jogo.escolherPalavra().upper()

    def produzirMatriz(self): # cria a matriz das palavras
        for col in range(0, 5):
            for row in range(0, 6):
                pygame.draw.rect(self.screen, white, [col * 100 + 12, row * 100 + 12, 75, 75], 0, 5)


    def preencherMatriz(self): # permite que letras sejam colocadas nos quadradinhos
        for col in range(0, 5):
            for row in range(0, 6):
                pieceText = titleFont.render(self.board[row][col], True, gray)
                self.screen.blit(pieceText, (col * 100 + 30, row * 100 + 25))        

    def checarPalavra(self):
        for col in range(0, 5):
            for row in range(0, 6):
                if self.palavra[col] == self.board[row][col]:
                    pygame.draw.rect(self.screen, green, [col * 100 + 12, row * 100 + 12, 75, 75], 0, 5)
                elif self.board[row][col] in self.palavra:
                    pygame.draw.rect(self.screen, yellow, [col * 100 + 12, row * 100 + 12, 75, 75], 0, 5)
            





