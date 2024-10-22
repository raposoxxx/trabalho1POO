import pygame
from telajogo import TelaJogo

tela = TelaJogo()
timer = pygame.time.Clock()
fps = 60

class Sistema:
    
    def run(self) -> None:
        running = True
        while running:
            
            if tela.letters == 5:
                turnActive = False
            if tela.letters < 5:
                turnActive = True

            timer.tick(fps)
            tela.produzirTela()
            tela.produzirMatriz()            
            tela.checarPalavra()
            tela.preencherMatriz()
 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE and tela.letters > 0:
                        tela.board[tela.turn][tela.letters - 1] = ' '
                        tela.letters -= 1
                    if event.key == pygame.K_TAB:
                        
                        tela.turn += 1
                        tela.letters = 0
                        turnActive = True
                if event.type == pygame.TEXTINPUT and turnActive:
                    entry = event.__getattribute__('text')
                    tela.board[tela.turn][tela.letters] = entry.upper()
                    tela.letters += 1
                




            pygame.display.flip()

        pygame.quit()