from utils import readJson
from utils import csvToJson
import random
from utils import atualizar_vitorias
from utils import podio


def Teste() -> None:
    #csvToJson('palavras.csv', 'palavras.json')
    nome = input("Digite seu nome: ")

    atualizar_vitorias('jogadores.json', nome)

    print(podio('jogadores.json'))

Teste()    


