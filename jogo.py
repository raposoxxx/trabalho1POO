import random
from utils import readCSV

filename = 'palavras.csv'

class Jogo:

    def __init__(self):
        self.palavras = readCSV('palavras.csv')
        self.tentativas = 0
        self.maxTentativas = 5
        self.tamanhoPalavra = 5


    def escolherPalavra(self):
        palavraEscolhida = random.choice(self.palavras)
        return palavraEscolhida        


    def checkTentativa(self, tentativa):
        

        if len(tentativa) != self.tamanhoPalavra or not tentativa.isalpha():  #Checa se a tentativa tem o tamanho correto e se é uma palavra
            raise ValueError(f"A palavra deve ter {self.tamanhoPalavra} letras") 
        

        return self.feedback(tentativa)
    
    def feedback(self, tentativa):
        self.tentativas += 1
        feedback = ['X'] * self.tamanhoPalavra

        palavraRestante = list(self.palavraEscolhida)

        for i, letra in enumerate(tentativa):
            if letra == self.palavraEscolhida[i]:
                feedback[i] = 'O'
                palavraRestante[i] = None

        for i, letra in enumerate(tentativa):          
            if feedback[i] == 'O':
                continue
            if letra in palavraRestante:
                feedback[i] = '/'
                palavraRestante[palavraRestante.index(letra)] = None

        return ''.join(feedback)
    

    def jogar(self):
        print('Bem-vindo ao jogo Termo! Adivinhe a palavra de ', self.tamanhoPalavra, 'letras')
        print('Você tem ', self.maxTentativas, 'tentativas')
        print('-----------------------------------')
        print('O = Letra correta no lugar certo')
        print('/ = Letra correta no lugar errado')
        print('X = Letra errada')
        
        while True:
            tentativa = input('Digite sua tentativa: ')
            try:
                feedback = self.checkTentativa(tentativa)
                print(feedback)

                if feedback == 'O' * self.tamanhoPalavra:
                    print('Parabéns! Você acertou a palavra!')
                    break

            except ValueError as e:
                print(e)
                

            if self.tentativas == self.maxTentativas:
                print('Você perdeu! A palavra era', self.palavraEscolhida)
                break



if __name__ == "__main__":


    jogo = Jogo()
    jogo.jogar()