from utils import readJson
from utils import csvToJson
import random


def Teste():
    csvToJson('palavras.csv', 'palavras.json')
    palavras = readJson('palavras.json')
    palavras = random.choice(palavras)



Teste()    


