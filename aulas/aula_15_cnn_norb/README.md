# Aula 15 - Redes Neurais Convolucionais (CNNs) com o Dataset NORB

Nesta aula, expandimos nossos horizontes para a visão computacional usando Redes Neurais Convolucionais (CNNs). Construímos um classificador de imagens 3D com o clássico *Small NORB dataset* criado por Yann LeCun. Aprendemos como utilizar convoluções para extração de características e operações de pooling para redução dimensional.

## 🛠️ Requisitos e Instalação

Certifique-se de criar um ambiente virtual (venv) para isolar as dependências e instalar os pacotes necessários para trabalhar com o PyTorch e o dataset de imagens:

```bash
# 1. Criar o ambiente virtual
python -m venv venv

# 2. Ativar o ambiente virtual no Windows
.\venv\Scripts\activate

# (Ou no Linux/macOS)
source venv/bin/activate

# 3. Instalar as bibliotecas requeridas
pip install torch torchvision matplotlib
```

## 📂 Arquivos da Aula

- `1_preparacao_imagens.py`: Download, conversão em tensores e normalização das imagens binoculares do dataset NORB.
- `2_modelo_cnn.py`: Definição da arquitetura da Rede Neural Convolucional (`Conv2d`, `MaxPool2d`, e `Linear`).
- `3_treinamento.py`: Loop de treinamento para ajuste dos pesos da rede usando Backpropagation e a função de perda.
- `4_validacao.py`: Teste do modelo treinado usando um conjunto inédito de imagens para validação da acurácia.

## 🎯 O que aprendemos:

- O que são Redes Neurais Convolucionais (CNNs) e por que são ideais para análise de imagens.
- Como baixar e formatar datasets do PyTorch utilizando o módulo `torchvision.transforms`.
- Como estruturar o cérebro visual de uma CNN empilhando camadas `nn.Conv2d` e `nn.MaxPool2d`.
- Como rodar o ciclo de treinamento e validar um classificador de objetos visuais.

## 🚀 Desafio Prático

Após rodar o treinamento e ver o resultado da classificação, tente alterar a arquitetura da sua rede neural. Adicione mais uma camada de convolução (`Conv2d`) ou altere o número de neurônios nas camadas finais. Execute o treinamento novamente e observe se a precisão do seu modelo (accuracy) melhora ou piora.

---

_Curso PythonIA do Zero - Professor Renato Aloi_
