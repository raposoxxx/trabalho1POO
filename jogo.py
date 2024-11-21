import random
from dados import readJson

class Jogo:

    def __init__(self) -> None:
        self.palavras = readJson('db/palavras.json')


    def escolherPalavra(self) -> str:
        palavraEscolhida = random.choice(self.palavras)
        return palavraEscolhida           