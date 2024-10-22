import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
    
fps = 60
timer = pygame.time.Clock()

class Tela():

    def __init__(self):
        self.WIDTH = 500
        self.HEIGHT = 700
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])  # A tela é definida aqui
        pygame.display.set_caption("Palavreado")
        self.board = [[" ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " "]]
        

    def produzirTela(self): # aparece tela
        self.screen.fill(white)

    def produzirMatriz(self): # cria a matriz das palavras
        for col in range(0, 5):
            for row in range(0, 6):
                pygame.draw.rect(self.screen, black, [col * 100, row * 100, 75, 75], 3, 5)


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




