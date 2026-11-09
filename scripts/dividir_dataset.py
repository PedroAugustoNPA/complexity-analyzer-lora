
import json
import random
from pathlib import Path

random.seed(42)

BASE = Path(__file__).resolve().parents[1]
ORIGEM = BASE / "data" / "complexity.jsonl"

with ORIGEM.open("r", encoding="utf-8") as arquivo:
    dados = [
        json.loads(linha)
        for linha in arquivo
        if linha.strip()
    ]

if len(dados) != 197:
    raise ValueError(
        f"Esperados 197 exemplos, encontrados {len(dados)}."
    )

random.shuffle(dados)

# Divisão: 157 treinamento, 20 validação e 20 teste
treino = dados[:157]
validacao = dados[157:177]
teste = dados[177:197]

conjuntos = {
    "train.jsonl": treino,
    "validation.jsonl": validacao,
    "test.jsonl": teste,
}

for nome, exemplos in conjuntos.items():
    destino = BASE / "data" / nome

    with destino.open("w", encoding="utf-8") as arquivo:
        for exemplo in exemplos:
            arquivo.write(
                json.dumps(exemplo, ensure_ascii=False) + "\n"
            )

    print(f"{nome}: {len(exemplos)} exemplos")

print("\nDivisão concluída!")
