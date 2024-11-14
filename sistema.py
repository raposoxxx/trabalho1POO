import pygame
from telajogo import TelaJogo
from telainicial import TelaInicial
from utils import atualizar_vitorias
from telafinal import TelaFinal

telajogo = TelaJogo()
telainicial = TelaInicial()
timer = pygame.time.Clock()
fps = 60

class Sistema:
    
    def run(self) -> None:
        
        running = True
        turnActive = True
        exibirJogo = False

        while running:

            timer.tick(fps) # temporizador

            if not exibirJogo:
                # Exibe a tela inicial
                telainicial.produzirTela()
                telainicial.produzirInicio()

                # Verifica eventos
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        # Permite que a tela do jogo seja exibida
                        exibirJogo = True
                    
            else:
                # Exibe a tela do jogo
                telajogo.jogarTurno()
            
            # Verifica se a linha está completa e mostra o feedback
            if telajogo.turn >= 6:
                #telajogo.contador()
                TelaFinal.exibir_podio("jogadores.json")
            if telajogo.letters == 5:
                telajogo.checarPalavra()
                turnActive = False  # Desativa entradas até o próximo turno
            else:
                turnActive = True  # Permite entradas enquanto a palavra não está completa

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    # Apaga a última letra se houver letras
                    if event.key == pygame.K_BACKSPACE and telajogo.letters > 0:
                        telajogo.board[telajogo.turn][telajogo.letters - 1] = ' '
                        telajogo.letters -= 1
                    # Inicia o próximo turno ao pressionar TAB
                    if event.key == pygame.K_TAB and telajogo.letters == 5:
                        telajogo.turn += 1
                        telajogo.letters = 0
                        turnActive = True  # Reativa entradas para o novo turno
                # Recebe letras apenas se turnActive estiver True
                if event.type == pygame.TEXTINPUT and turnActive:
                    entry = event.__getattribute__('text')
                    if telajogo.letters < 5:  # Garante máximo de 5 letras por linha
                        telajogo.board[telajogo.turn][telajogo.letters] = entry.upper()
                        telajogo.letters += 1

                

            pygame.display.flip() # flip() abre uma nova janela com o que foi implementado

        pygame.quit()
