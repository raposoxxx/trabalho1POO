import pygame
from tela import Tela
from telajogo import TelaJogo
from utils import csvToJson 

tela = Tela()
telajogo = TelaJogo()
timer = pygame.time.Clock()
fps = 60

class Sistema:
    
    def run(self) -> None:
        
        running = True
        while running:
            
            if telajogo.letters == 5:
                turnActive = False
            if telajogo.letters < 5:
                turnActive = True

            timer.tick(fps)
            tela.produzirTela()
            telajogo.produzirMatriz()            
            telajogo.checarPalavra()
            telajogo.preencherMatriz()
 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE and tela.letters > 0:
                        telajogo.board[telajogo.turn][telajogo.letters - 1] = ' '
                        telajogo.letters -= 1
                    if event.key == pygame.K_TAB:
                        telajogo.turn += 1
                        telajogo.letters = 0
                        turnActive = True
                if event.type == pygame.TEXTINPUT and turnActive:
                    entry = event.__getattribute__('text')
                    telajogo.board[telajogo.turn][telajogo.letters] = entry.upper()
                    telajogo.letters += 1
                

            pygame.display.flip()

        pygame.quit()