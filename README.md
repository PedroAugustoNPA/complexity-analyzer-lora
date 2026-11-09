# Complexity Analyzer — LoRA

Projeto experimental de fine-tuning utilizando LoRA para adaptar um modelo de linguagem à análise de complexidade de algoritmos em C.

## Modelo

- Modelo base: Qwen3-0.6B
- Técnica: LoRA
- Frameworks: Transformers e PEFT
- Hardware de treinamento: NVIDIA Tesla T4 (Google Colab)

## Dataset

197 exemplos válidos, divididos em:

- Treinamento: 157
- Validação: 20
- Teste: 20

## Resultados

| Época | Training Loss | Validation Loss |
|---|---:|---:|
| 1 | 1.0929 | 0.8807 |
| 2 | 0.7437 | 0.7356 |
| 3 | 0.5822 | 0.6989 |
| 4 | 0.5023 | 0.6917 |
| 5 | 0.4397 | 0.6898 |

## Objetivo

Estudar o processo de fine-tuning de modelos de linguagem com LoRA e avaliar sua capacidade de identificar complexidades temporais e espaciais.

**Status:** experimento inicial para fins de aprendizado.