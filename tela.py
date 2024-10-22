import pygame

pygame.init()

white = (255, 255, 255)
gray = (48, 48, 48)
green = (19, 122, 53)
    
fps = 60
timer = pygame.time.Clock()
titleFont = pygame.font.Font('freesansbold.ttf', 56)

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
                pygame.draw.rect(self.screen, gray, [col * 100 + 12, row * 100 + 12, 75, 75], 3, 5)
                pieceText = titleFont.render(self.board[row][col], True, gray)
                self.screen.blit(pieceText, (col * 100 + 35, row * 100 + 25))


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




