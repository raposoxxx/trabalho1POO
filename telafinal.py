import pygame
from tela import Tela
from utils import carregarPodio

pygame.init()

class TelaFinal(Tela):
    
    def __init__(self) -> None:
        super().__init__()

    def produzirTela(self) -> None:
        self.screen.blit(self.finalbgimage, (0, 0))

    def exibirPodio(self) -> None:

        # Carrega e ordena os jogadores
        podio_df = carregarPodio('db/jogadores.json')

        # Loop de exibição do pódio
        running = True
        while running:
            self.produzirTela()

            # Exibe o título
            title_surface = self.titleFont.render("ranking: ", True, self.gray)
            self.screen.blit(title_surface, (110, 20))

            # Exibe os primeiros colocados
            for i, row in podio_df.iterrows():
                if i >= 5:  # Mostra apenas o top 5
                    break
                text = f"{i + 1}º - {row['nome']}: ({row['vitorias']})"
                text_surface = self.regularFont.render(text, True, self.gray)
                self.screen.blit(text_surface, (130, 120 + i * 70))

            # Event loop para fechar o pódio
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()

        pygame.quit()
        