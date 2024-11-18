from dados import atualizar_vitorias
from dados import podio


def Teste() -> None:
    #csvToJson('palavras.csv', 'palavras.json')
    nome = input("Digite seu nome: ")

    atualizar_vitorias('jogadores.json', nome)

    print(podio('jogadores.json'))

Teste()    


