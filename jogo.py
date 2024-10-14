import random
from utils import readCSV

filename = 'palavras.csv'

class Jogo:
    def __init__(self, filename):
        self.palavras = readCSV(filename)
        self.palavraEscolhida = random.choice(self.palavras)
        self.tentativas = 0


    def tentar(self, tentativa):
        

        if len(tentativa) != 5:
            raise ValueError('A palavra deve ter 5 letras') 
        

        return self.feedback(tentativa)
    
    def feedback(self, tentativa):
        self.tentativas += 1
        