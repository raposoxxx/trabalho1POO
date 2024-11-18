import pygame
import pandas as pd
from telafinal import TelaFinal
from dados import salvar_vencedor

# Função para exibir a tela do vencedor
def tela_vencedor(json_filename):
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Você Venceu!")

    font = pygame.font.Font(None, 36)
    input_font = pygame.font.Font(None, 32)

    background_color = (0, 128, 0)  # Verde
    text_color = (255, 255, 255)

    input_box = pygame.Rect(150, 200, 300, 40)
    color_active = (255, 255, 255)
    color_inactive = (100, 100, 100)
    color = color_active  # Já ativa por padrão
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
                        salvar_vencedor(json_filename, text.strip())
                        running = False
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        # Renderiza a tela
        screen.fill(background_color)

        # Exibe a mensagem de vitória
        title_surface = font.render("Parabéns! Você venceu!", True, text_color)
        screen.blit(title_surface, (150, 100))

        # Exibe a instrução
        instruction_surface = font.render("Digite seu nome e pressione Enter:", True, text_color)
        screen.blit(instruction_surface, (120, 160))

        # Desenha a caixa de entrada e o texto digitado
        pygame.draw.rect(screen, color, input_box, 2)
        text_surface = input_font.render(text, True, text_color)
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

        pygame.display.flip()

    TelaFinal.exibir_podio("jogadores.json")
