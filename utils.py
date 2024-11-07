import csv
import json
import unicodedata
import pandas as pd

def csvToJson(csv_filename, json_filename) -> None:
    
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


def readJson(filename) -> None:
    # Lê o JSON e retorna a coluna de palavras como lista
    df = pd.read_json(filename, orient='records', lines=True)
    return df[0].tolist()


import pandas as pd

import pandas as pd

def atualizar_vitorias(json_filename, nome_jogador):
    try:
        # Tenta carregar o JSON como DataFrame
        df = pd.read_json(json_filename, lines=True)
    except (ValueError, FileNotFoundError):
        # Inicializa um DataFrame vazio se o arquivo estiver vazio ou não existir
        df = pd.DataFrame(columns=["nome", "vitorias"])

    # Verifica se o DataFrame está vazio (arquivo JSON estava vazio)
    if df.empty:
        # Adiciona o primeiro jogador com 1 vitória
        df = pd.DataFrame([{"nome": nome_jogador, "vitorias": 1}])
    elif nome_jogador in df["nome"].values:
        # Incrementa o contador de vitórias para o jogador existente
        df.loc[df["nome"] == nome_jogador, "vitorias"] += 1
    else:
        # Adiciona o jogador com 1 vitória se ele ainda não estiver no DataFrame
        novo_jogador = pd.DataFrame([{"nome": nome_jogador, "vitorias": 1}])
        df = pd.concat([df, novo_jogador], ignore_index=True)

    # Salva o DataFrame atualizado de volta no JSON
    df.to_json(json_filename, orient='records', lines=True)


def podio(json_filename):
    # Lê o JSON e retorna o DataFrame
    df = pd.read_json(json_filename, lines=True)

    # Ordena o DataFrame por número de vitórias em ordem decrescente
    df = df.sort_values(by="vitorias", ascending=False)

    # Retorna as 3 primeiras linhas do DataFrame
    return df.head(5)



