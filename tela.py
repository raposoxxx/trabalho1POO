import pygame

pygame.init()

white = (255, 255, 255)
gray = (48, 48, 48)
green = (19, 122, 53)
yellow = (220, 176, 53)
    
fps = 60
timer = pygame.time.Clock()
titleFont = pygame.font.Font('freesansbold.ttf', 56)
turnActive = True

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
        
        self.turn = 0
        self.letters = 0
        

    def produzirTela(self): # aparece tela
        self.screen.fill(white)

    def produzirMatriz(self): # cria a matriz das palavras
        for col in range(0, 5):
            for row in range(0, 6):
                pygame.draw.rect(self.screen, gray, [col * 100 + 12, row * 100 + 12, 75, 75], 3, 5)
                pieceText = titleFont.render(self.board[row][col], True, gray)
                self.screen.blit(pieceText, (col * 100 + 30, row * 100 + 25))

    def checarPalavra(self):
        global palavra
        for col in range(0, 5):
            for row in range(0, 6):
                if palavra[col] == self.board[row][col] and self.turn > row:
                    pygame.draw.rect(self.screen, green, [col * 100 + 12, row * 100 + 12, 75, 75], 0, 5)
                elif self.board[row][col] in palavra and self.turn > row:
                    pygame.draw.rect(self.screen, yellow, [col * 100 + 12, row * 100 + 12, 75, 75], 0, 5)



tela = Tela()


running = True
while running:
    timer.tick(fps)
    tela.produzirTela()
    tela.produzirMatriz()
    tela.checarPalavra()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and tela.letters > 0:
                tela.board[tela.turn][tela.letters] = ' '
                tela.letters -= 1
            if event.key == pygame.K_SPACE:
                tela.turn += 1
                tela.letters = 0
        if event.type == pygame.TEXTINPUT:
            entry = event.__getattribute__('text')
            tela.board[tela.turn][tela.letters] = entry.upper()
            tela.letters += 1
        

    if tela.letters == 5:
        turnActive = False
    if tela.letters < 5:
        turnActive = True


    pygame.display.flip()

pygame.quit()




