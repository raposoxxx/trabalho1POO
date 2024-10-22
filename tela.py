import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
    
fps = 60
timer = pygame.time.Clock()

class Tela():

    def produzirTela(): # aparece tela
        WIDTH = 500
        HEIGHT = 700
        screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption("Palavreado")

        screen.fill(white)

    def produzirMatriz(): # cria a matriz das palavras
        global screen
        turn = 0
        board = [[" ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " "],]
        
        for col in range(0, 5):
            for row in range(0, 6):
                pygame.draw.rect(screen, black, [col * 100, row * 100, 75, 75], 3, 5)


tela = Tela()

running = True
while running:
    timer.tick(fps)
    tela.produzirTela()
    tela.produzirMatriz()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()




