import csv
import json
import unicodedata
import pandas as pd

def csvToJson(csv_filename, json_filename):
    # Carrega o CSV, remove acentos, converte para minúsculas e remove espaços
    df = pd.read_csv(csv_filename, header=None)
    print(df)
    df[0] = df[0].str.normalize('NFD').str.encode('ascii', 'ignore').str.decode('utf-8').str.lower().str.strip()
    df.to_json(json_filename, orient='records', lines=True)


def readJson(filename):
    # Lê o JSON e retorna a coluna de palavras como lista
    df = pd.read_json(filename, orient='records', lines=True)
    return df[0].tolist()