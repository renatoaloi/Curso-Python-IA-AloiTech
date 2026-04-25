# Aula 14 - Classificador de Sentimentos NLP com PyTorch

Construindo o nosso próprio Classificador de Sentimentos usando Processamento de Linguagem Natural (NLP) com PyTorch.

## 🛠️ Requisitos e Instalação

Recomendamos o uso de um ambiente virtual (venv) para isolar as dependências do projeto.

1. Crie o ambiente virtual:
```bash
python -m venv venv
```

2. Ative o ambiente virtual:
- No Windows:
```bash
venv\Scripts\activate
```
- No Linux/Mac:
```bash
source venv/bin/activate
```

3. Instale as bibliotecas necessárias:
```bash
pip install torch pandas
```

## 📂 Arquivos da Aula

* `1_preparacao_dados.py`: Carregando um CSV e transformando texto em números.
* `2_modelo_e_treino.py`: Construção e treinamento da rede neural.
* `3_testar_ia.py`: Testando a inteligência artificial com novas frases.
* `comentarios_videos.csv`: Arquivo CSV de exemplo com comentários.

## 🎯 O que aprendemos:

* Preparar dados textuais usando técnicas de NLP (Bag of Words).
* Criar tensores a partir de texto.
* Construir uma arquitetura de rede neural no PyTorch focada em classificação binária.
* Realizar inferência com o modelo treinado em dados inéditos.

## 🚀 Desafio Prático

Após treinar o modelo com o dataset fornecido, tente adicionar novas frases ao `comentarios_videos.csv` e veja como a precisão da sua IA melhora!

---

_Curso PythonIA do Zero - Professor Renato Aloi_
