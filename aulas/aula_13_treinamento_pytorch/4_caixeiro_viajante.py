import torch
import torch.nn as nn
import torch.optim as optim

# Aula 13.4: Projeto - Área de Cobertura (Delivery)
# Objetivo: Treinar uma IA para decidir se uma coordenada (Lat, Long)
# está dentro da nossa região de atendimento ou não.

# 1. DADOS DE TREINAMENTO (Sintéticos)
# Coordenada Central (Ex: Centro de SP): -23.5505, -46.6333

# [Latitude, Longitude] - Dados Brutos
X_bruto = torch.tensor([
    [-23.55765, -46.64445], # 0, 0
    [-23.54585, -46.64464], # 0, 1
    [-23.55851, -46.62572], # 1, 0
    [-23.54561, -46.6264]   # 1, 1
], dtype=torch.float32)

# IMPORTANTE: Normalização (Min-Max Scaling)
# Por que normalizar? As coordenadas são números muito grandes e próximos.
# A IA "se perde" tentando calcular pesos para números como -23.5505.
# Vamos transformar tudo para uma escala entre 0 e 1.
x_min = X_bruto.min(dim=0).values
x_max = X_bruto.max(dim=0).values
X = (X_bruto - x_min) / (x_max - x_min)

# Respostas: 1.0 (Atendido), 0.0 (Não Atendido)
y = torch.tensor([
    [0.0], [1.0], [1.0], [1.0]
], dtype=torch.float32)

# 2. DEFINIÇÃO DA REDE NEURAL
# Com os dados normalizados, a rede aprende MUITO mais rápido.
modelo = nn.Sequential(
    nn.Linear(2, 16),   # Aumentamos para 16 neurônios para uma "fronteira" mais precisa
    nn.ReLU(),
    nn.Linear(16, 1),   
    nn.Sigmoid()
)

# 3. CONFIGURAÇÃO
criterio = nn.BCELoss()
otimizador = optim.Adam(modelo.parameters(), lr=0.01)

# 4. LOOP DE TREINAMENTO
print("Ensinando a IA a reconhecer nossa área de atendimento (com dados normalizados)...")
for epoca in range(1000):
    previsao = modelo(X)
    erro = criterio(previsao, y)
    
    otimizador.zero_grad()
    erro.backward()
    otimizador.step()
    
    if (epoca + 1) % 200 == 0:
        print(f"Época {epoca+1}/1000 - Erro: {erro.item():.4f}")

# 5. TESTANDO COM NOVOS ENDEREÇOS
print("\n--- TESTANDO NOVAS COORDENADAS ---")
testes_brutos = torch.tensor([
    [-23.55005, -46.63411], # Atende
    [-23.5568, -46.64378],  # Não atende
    [-23.55753, -46.64978], # Fora da área (não atendido)
    [-23.54266, -46.62401]  # Fora da área (atendido)
], dtype=torch.float32)

# ATENÇÃO: Precisamos normalizar os dados de teste usando o MESMO min e max do treino!
testes = (testes_brutos - x_min) / (x_max - x_min)

with torch.no_grad():
    resultado = modelo(testes)
    
    for i in range(len(testes)):
        lat, lon = testes_brutos[i].tolist()
        prob = resultado[i].item()
        status = "✅ ATENDIDO" if prob > 0.5 else "❌ NÃO ATENDIDO"
        print(f"Coordenada Original: [{lat:.4f}, {lon:.4f}]")
        print(f"Status da IA: {status} (Confiança: {prob:.2%})\n")

print("\nConclusão: A IA agora consegue classificar territórios geograficamente!")