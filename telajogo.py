import pygame
from jogo import Jogo
from tela import Tela

pygame.init()


tela = Tela()
jogo = Jogo()
    
titleFont = pygame.font.Font('freesansbold.ttf', 56)
turnActive = True


class TelaJogo(Tela):

    def __init__(self):
        super().__init__()
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
                pygame.draw.rect(self.screen, tela.lightgray, [col * 100 + 12, row * 100 + 12, 75, 75], 0, 5)


    def preencherMatriz(self): # permite que letras sejam colocadas nos quadradinhos
        for col in range(0, 5):
            for row in range(0, 6):
                pieceText = titleFont.render(self.board[row][col], True, tela.white)
                self.screen.blit(pieceText, (col * 100 + 30, row * 100 + 25))        

    def checarPalavra(self):
        for col in range(0, 5):
            for row in range(0, 6):
                if self.palavra[col] == self.board[row][col]:
                    pygame.draw.rect(tela.screen, tela.green, [col * 100 + 12, row * 100 + 12, 75, 75], 0, 5)
                elif self.board[row][col] in self.palavra:
                    pygame.draw.rect(tela.screen, tela.yellow, [col * 100 + 12, row * 100 + 12, 75, 75], 0, 5)
            





