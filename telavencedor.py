import pygame
import pandas as pd
from tela import Tela
from telafinal import TelaFinal

telafinal = TelaFinal()

class TelaVencedor(Tela):
    def __init__(self) -> None:
        super().__init__()
        
    def produzirTela(self) -> None:
        self.screen.fill(self.gray)

# Função para salvar o nome do jogador e adicionar ao ranking
    def salvarVencedor(self, json_filename, nome_jogador) -> None:
        try:
            # Carrega o JSON se ele existir
            df = pd.read_json(json_filename, lines=True)
        except (ValueError, FileNotFoundError):
            # Inicializa um DataFrame vazio se o arquivo estiver vazio ou não existir
            df = pd.DataFrame(columns=["nome", "vitorias"])
        
        # Verifica se o jogador já está no ranking
        if nome_jogador in df["nome"].values:
            # Incrementa as vitórias do jogador existente
            df.loc[df["nome"] == nome_jogador, "vitorias"] += 1
        else:
            # Adiciona o jogador com 1 vitória
            novo_jogador = pd.DataFrame([{"nome": nome_jogador, "vitorias": 1}])
            df = pd.concat([df, novo_jogador], ignore_index=True)
        
        # Salva o DataFrame atualizado no JSON
        df.to_json(json_filename, orient="records", lines=True)

    # Função para exibir a tela do vencedor
    def telaVencedor(self, json_filename) -> None:
        pygame.init()
        pygame.display.set_caption("Você Venceu!")

        input_box = pygame.Rect(100, 180, 300, 40)
        text = ""

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    # Verifica entrada de texto
                    if event.key == pygame.K_RETURN:  # Pressiona Enter para salvar
                        if text.strip():  # Salva apenas se o nome não estiver vazio
                            self.salvarVencedor(json_filename, text.strip())
                            running = False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

            self.produzirTela()

            # Exibe a mensagem de vitória
            title_surface = self.smallGameFont.render("Parabéns! Você venceu!", True, self.white)
            self.screen.blit(title_surface, (100, 100))

            # Exibe a instrução
            instruction_surface = self.smallGameFont.render("Digite seu nome e pressione Enter:", True, self.white)
            self.screen.blit(instruction_surface, (40, 130))

            # Desenha a caixa de entrada e o texto digitado
            pygame.draw.rect(self.screen, self.lightgray, input_box, 0, 5)
            text_surface = self.smallGameFont.render(text, True, self.white)
            self.screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

            pygame.display.flip()

        telafinal.exibirPodio()
