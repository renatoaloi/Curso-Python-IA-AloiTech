# Aula 13 - Treinando sua própria IA (PyTorch)

Eu sei que você já assistiu dezenas de vídeos ensinando como funcionam as Redes Neurais Artificiais (RNA's), mostrando aqueles desenhos de neurônios com setinhas pra lá e pra cá, mas hoje vamos colocar a mão na massa e vou mostrar para vocês, através de gráficos cuidadosamente elaborados, o que está acontecendo dentro de uma rede neural enquanto ela funciona. Vamos levantar o capô e ver a mágica acontecendo!

Então nessa aula vamos mergulhar no mundo do Deep Learning para entender como as redes neurais realmente "aprendem". Vou apresentar para vocês o "Dilema do Caixeiro Viajante" e como podemos resolver isso com IA.

Vem comigo e vamos aprender juntos como funcionam as caraminholas dentro da cabeça da IA!

## 🛠️ Requisitos e Instalação

Para acompanhar esta aula e rodar os scripts, você precisa instalar a biblioteca **PyTorch**.

Abra o terminal e execute:

```bash
# 1. Criar o ambiente virtual
python -m venv venv

# 2. Ativar o ambiente virtual no Windows
.\venv\Scripts\activate

# (Ou no Linux/macOS)
source venv/bin/activate

# 3. Instalar as bibliotecas requeridas
pip install torch
```

> [!NOTE]
> Se você estiver usando Mac (M1/M2/M3), o PyTorch detectará automaticamente o chip para aceleração. Nesta aula, configuramos o código para rodar em **CPU** por padrão para garantir compatibilidade total.

## 📂 Arquivos da Aula

O aprendizado é progressivo, siga a ordem dos scripts:

1. `1_tensores_basico.py`: O que são Tensores (Átomos da IA) e como a matemática fundamental funciona.
2. `2_hello_world_ia.py`: O "Nascimento" do neurônio. Ensinamos a lógica OR para entender o loop de treinamento.
3. `3_problema_XOR.py`: O desafio clássico. Como camadas ocultas permitem que a IA aprenda problemas não-lineares.
4. `4_caixeiro_viajante.py`: Projeto Final. Usamos Latitude e Longitude para criar um classificador de área de atendimento de delivery.

## 🎯 O que aprendemos:

1. **Estrutura de Tensores**: Escalares, Vetores, Matrizes e a eficiência computacional.
2. **Matemática da IA**: O segredo da fórmula $y = wx + b$.
3. **Camadas Ocultas**: Por que redes profundas são necessárias para a complexidade do mundo real.
4. **Treinamento Geográfico**: Como preparar coordenadas (Lat/Long) para que a IA aprenda a decidir territórios.

## 🚀 Desafio Prático

No script `4_caixeiro_viajante.py`, tente adicionar novas coordenadas de treinamento no Tensor `X` e suas respectivas respostas no Tensor `y`. Treine novamente a rede e veja se ela se torna mais precisa ao testar novos pontos na cidade!

---

_Curso PythonIA do Zero - Professor Renato Aloi_
