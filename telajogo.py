import pygame
from jogo import Jogo
from tela import Tela

pygame.init()

tela = Tela()
jogo = Jogo()

class TelaJogo(Tela):

    def __init__(self) -> None:
        super().__init__()
        self.board = [[" ", " ", " ", " ", " "] for _ in range(6)]
        self.colors = [["lightgray" for _ in range(5)] for _ in range(6)]  # Matriz para armazenar cores de cada quadrado
        self.turn = 0
        self.letters = 0
        self.palavra = jogo.escolherPalavra().upper()

    def produzirTela(self) -> None: # produz tela do jogo
        self.screen.fill(self.gray)

    def produzirMatriz(self) -> None:
        # Usa a matriz de cores para desenhar cada quadrado na cor correta
        for col in range(5):
            for row in range(6):
                color = getattr(tela, self.colors[row][col])  # Acessa a cor pela string na matriz de cores
                pygame.draw.rect(self.screen, color, [col * 100 + 12, row * 100 + 12, 75, 75], 0, 5)

    def preencherMatriz(self) -> None: # permite que letras sejam colocadas nos quadradinhos
        for col in range(5):
            for row in range(6):
                pieceText = self.gameFont.render(self.board[row][col], True, tela.white)
                self.screen.blit(pieceText, (col * 100 + 30, row * 100 + 25))

    def checarPalavra(self) -> None:
        palavra_restante = list(self.palavra)  # Copia da palavra para modificar conforme checamos
        
        # Primeiro, para letras no lugar correto
        for col in range(5):
            if self.palavra[col] == self.board[self.turn][col]:
                self.colors[self.turn][col] = "green"  # Armazena a cor
                palavra_restante[col] = None  # Marca como usada

        # Depois, para letras corretas no lugar errado
        for col in range(5):
            if self.palavra[col] != self.board[self.turn][col] and self.board[self.turn][col] in palavra_restante:
                self.colors[self.turn][col] = "yellow"  # Armazena a cor
                palavra_restante[palavra_restante.index(self.board[self.turn][col])] = None  # Marca como usada

    def jogarTurno(self) -> None:
        # Adiciona letra ao tabuleiro e incrementa contador de letras
        if self.letters < 5:
            self.preencherMatriz()
            self.letters += 1

        # Verifica a palavra quando a linha atual está completa
        if self.letters == 5:
            self.checarPalavra()  # Dá feedback após tentativa completa
            self.turn += 1        # Passa para o próximo turno
            self.letters = 0      # Reseta o contador de letras




