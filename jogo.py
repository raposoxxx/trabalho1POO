import random
from utils import readCSV

filename = 'palavras.csv'

class Jogo:
    def __init__(self, filename):
        self.palavras = readCSV(filename)
        self.palavraEscolhida = random.choice(self.palavras)
        self.tentativas = 0
        self.maxTentativas = 5
        self.tamanhoPalavra = 5


    def checkTentativa(self, tentativa):
        

        if len(tentativa) != self.tamanhoPalavra:
            raise ValueError('A palavra deve ter', self.tamanhoPalavra, 'letras') 
        

        return self.feedback(tentativa)
    
    def feedback(self, tentativa):
        self.tentativas += 1
        feedback = ['-'] * 5
        for i, letra in enumerate(tentativa):
            if letra == self.palavraEscolhida[i]:
                feedback[i] = 'C'
            elif letra in self.palavraEscolhida:
                feedback[i] = 'E'
            else:
                feedback[i] = 'X'
        return ''.join(feedback)
    
    def jogar(self):
        print('Bem-vindo ao jogo Termo! Adivinhe a palavra de ', self.tamanhoPalavra, 'letras')
        print('Você tem ', self.maxTentativas, 'tentativas')
        print('-----------------------------------')
        print('C = Letra correta no lugar certo')
        print('E = Letra correta no lugar errado')
        print('X = Letra errada')
        
        while True:
            tentativa = input('Digite sua tentativa: ')
            try:
                feedback = self.checkTentativa(tentativa)
                print(feedback)

                if feedback == 'C' * self.tamanhoPalavra:
                    print('Parabéns! Você acertou a palavra!')
                    break

            except ValueError as e:
                print(e)
                

            if self.tentativas == self.maxTentativas:
                print('Você perdeu! A palavra era', self.palavraEscolhida)
                break







if __name__ == "__main__":
    jogo = Jogo('palavras.csv')
    jogo.jogar()