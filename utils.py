import csv
import json
import unicodedata
import pandas as pd

def csvToJson(csv_filename, json_filename):
    
    df = pd.read_csv(csv_filename, header=None)

    # Remove acentos, converte para minúsculas e remove espaços
    df[0] = (
        df[0]
        .apply(lambda x: unicodedata.normalize('NFD', x).encode('ascii', 'ignore').decode('utf-8'))
        .str.lower()
        .str.strip()
    )

    # Salva o DataFrame no formato JSON
    df.to_json(json_filename, orient='records', lines=True)


def readJson(filename):
    # Lê o JSON e retorna a coluna de palavras como lista
    df = pd.read_json(filename, orient='records', lines=True)
    return df[0].tolist()