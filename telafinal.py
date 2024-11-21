import pygame
from tela import Tela
from utils import carregarPodio

pygame.init()

class TelaFinal(Tela):
    
    def __init__(self) -> None:
        super().__init__()

    def produzirTela(self) -> None:
        self.screen.blit(self.finalbgimage, (0, 0))

    def exibirPodio(json_filename):
        pygame.init()
        screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("Pódio")

        # Carrega e ordena os jogadores
        podio_df = carregarPodio(json_filename)

        # Fontes e cores
        font = pygame.font.Font(None, 36)
        background_color = (30, 30, 30)
        text_color = (255, 255, 255)

        # Loop de exibição do pódio
        running = True
        while running:
            screen.fill(background_color)

            # Exibe o título
            title_surface = font.render("Pódio dos Jogadores", True, text_color)
            screen.blit(title_surface, (200, 50))

            # Exibe os primeiros colocados
            for i, row in podio_df.iterrows():
                if i >= 5:  # Mostra apenas o top 5
                    break
                text = f"{i + 1}º - {row['nome']}: {row['vitorias']} vitórias"
                text_surface = font.render(text, True, text_color)
                screen.blit(text_surface, (100, 100 + i * 40))

            # Event loop para fechar o pódio
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()

        pygame.quit()
        