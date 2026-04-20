import torch
import torch.nn as nn
import torch.optim as optim

# Aula 13.3: Problema do XOR (OU Exclusivo)
# Objetivo: Ensinar a rede a lidar com dados que não são linearmente separáveis.

# 1. DADOS DE TREINAMENTO
# Note que incluímos um ponto extra [2.0, 2.0] para teste de limite.
X = torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [2.0, 2.0]
])
y = torch.tensor([
    [0.0],
    [1.0],
    [1.0],
    [1.0],
    [0.0]
])

# 2. ARQUITETURA DA REDE
# Usamos uma camada oculta de 4 neurônios com ativação ReLU para resolver a não-linearidade.
modelo = nn.Sequential(
    nn.Linear(2, 4),
    nn.ReLU(),
    nn.Linear(4, 1),
    nn.Sigmoid()
)

# 3. CRITÉRIO DE ERRO E OTIMIZADOR
criterio = nn.MSELoss()
otimizador = optim.SGD(modelo.parameters(), lr=0.2)

# 4. LOOP DE TREINAMENTO (2000 Épocas)
for epoca in range(2000):
    # Forward: A IA faz a previsão
    previsao = modelo(X)
    
    # Cálculo do Erro
    erro = criterio(previsao, y)
    
    # Backpropagation: Ajuste dos Pesos
    otimizador.zero_grad()
    erro.backward()
    otimizador.step()
    
    # Exibição do progresso a cada 100 épocas
    if (epoca + 1) % 100 == 0:
        print(f"Época: {epoca+1}/1000 | Previsão: {previsao} | Esperado: {y} Erro: {erro.item():.4f}")

# 5. TESTE COM NOVOS DADOS
data_teste = torch.tensor([
    [1.0, 0.0],
    [2.0, 2.0]
])
resultado = modelo(data_teste)

# Exibição dos resultados finais formatados
for i in range(len(data_teste)):
    entrada = data_teste[i].tolist()
    previsao = resultado[i].item()
    print(f"Entrada: {entrada} -> Previsão da IA: {previsao:.4f} ({'TRUE' if previsao > 0.5 else 'FALSE'})")