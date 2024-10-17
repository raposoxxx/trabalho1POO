import csv

def readCSV(filename):
    palavras = []
    with open(filename, newline='') as csvfile:
        leitor = csv.reader(csvfile)
        for linha in leitor:
            palavras.append(linha[0].lower().strip())
    return palavras
        

