
import json
from pathlib import Path
from collections import Counter

BASE = Path(__file__).resolve().parents[1]
ARQUIVO = BASE / "data" / "complexity.jsonl"

dados = []
erros = []
prompts = []

with ARQUIVO.open("r", encoding="utf-8") as arquivo:
    for numero, linha in enumerate(arquivo, start=1):
        if not linha.strip():
            continue

        try:
            exemplo = json.loads(linha)
        except json.JSONDecodeError as erro:
            erros.append(f"Linha {numero}: JSON inválido: {erro}")
            continue

        mensagens = exemplo.get("messages")

        if not isinstance(mensagens, list):
            erros.append(f"Linha {numero}: campo 'messages' ausente ou inválido.")
            continue

        usuarios = [
            m for m in mensagens
            if m.get("role") == "user"
        ]

        assistentes = [
            m for m in mensagens
            if m.get("role") == "assistant"
        ]

        if len(usuarios) != 1 or len(assistentes) != 1:
            erros.append(
                f"Linha {numero}: esperado exatamente "
                "uma mensagem user e uma assistant."
            )
            continue

        pergunta = usuarios[0].get("content", "").strip()
        resposta = assistentes[0].get("content", "").strip()

        if not pergunta or not resposta:
            erros.append(f"Linha {numero}: pergunta ou resposta vazia.")
            continue

        prompts.append(pergunta)
        dados.append(exemplo)

contagem = Counter(prompts)
duplicados = [
    pergunta for pergunta, quantidade in contagem.items()
    if quantidade > 1
]

print("=== RELATÓRIO DO DATASET ===")
print(f"Exemplos válidos: {len(dados)}")
print(f"Perguntas distintas: {len(contagem)}")
print(f"Perguntas duplicadas: {len(duplicados)}")
print(f"Erros encontrados: {len(erros)}")

if erros:
    print("\n=== ERROS ===")
    for erro in erros:
        print(erro)

if duplicados:
    print("\n=== PERGUNTAS DUPLICADAS ===")
    for pergunta in duplicados:
        print("-", pergunta[:150])

if not erros and not duplicados:
    print("\nDataset passou nas verificações básicas!")
