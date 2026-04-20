# Aula 13 - Treinando sua própria IA (PyTorch)

Nesta aula, mergulhamos no mundo do Deep Learning para entender como as redes neurais "aprendem". Construímos um classificador de sentimentos real para comentários do YouTube, saindo da teoria e indo para a prática com PyTorch.

## 🛠️ Requisitos e Instalação

Para acompanhar esta aula e rodar os scripts, você precisa instalar as bibliotecas **PyTorch** e **Pandas**. 

Abra o terminal e execute:

```bash
pip install torch pandas
```

> [!NOTE]
> Se você estiver usando Mac (M1/M2/M3), o PyTorch detectará automaticamente o chip para aceleração. Nesta aula, configuramos o código para rodar em **CPU** por padrão para garantir compatibilidade total.

## 📂 Arquivos da Aula

1. `1_tensores_basico.py`: O que são Tensores (Escalares, Vetores, Matrizes e Cubos) e como a matemática da IA funciona.
2. `2_preparacao_dados.py`: Como carregar o CSV e preparar o texto para a rede neural.
3. `3_modelo_e_treino.py`: Onde criamos a arquitetura da rede e realizamos o treinamento.
4. `4_testar_ia.py`: Script para você testar a sua IA treinada com novas frases.
5. `comentarios_videos.csv`: Nosso dataset real de treinamento.

## 🎯 O que aprendemos:

1. **Estrutura de Tensores**: A base numérica de toda Inteligência Artificial.
2. **Matemática da IA**: O conceito intuitivo de Pesos (Weights), Vieses (Bias) e Ativação.
3. **Pipeline de Dados**: Transformando texto em números através do "Bag of Words".
4. **Treinamento**: O loop de ajuste onde a IA aprende com seus próprios erros (Loss e Optimization).

## 🚀 Desafio Prático

Tente abrir o arquivo `comentarios_videos.csv` e adicionar mais 10 frases (5 positivas e 5 negativas). Depois, rode o script `3_modelo_e_treino.py` novamente e veja se a precisão da sua IA no script `4_testar_ia.py` melhorou!

---

_Curso PythonIA do Zero - Professor Renato Aloi_
