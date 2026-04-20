import torch
import torch.nn as nn
import torch.optim as optim

# Aula 13.2: Hello World da IA (Porta Lógica OR)
# O objetivo aqui é ensinar a rede a entender a lógica:
# 0 OR 0 = 0
# 0 OR 1 = 1
# 1 OR 0 = 1
# 1 OR 1 = 1

# 1. DADOS DE TREINAMENTO (Entradas e Respostas Esperadas)
X = torch.tensor([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
y = torch.tensor([[0.0], [1.0], [1.0], [1.0]])

# 2. DEFINIÇÃO DA REDE NEURAL MAIS SIMPLES DO MUNDO
# nn.Linear(2, 1) significa: 2 entradas, 1 saída
# Ele vai criar automaticamente os Pesos (W) e o Viés (b)
modelo = nn.Sequential(
    nn.Linear(2, 1),
    nn.Sigmoid() # Transforma o resultado em um número entre 0 e 1
)

# 3. OTIMIZADOR E FUNÇÃO DE ERRO
# Queremos minimizar o erro entre a previsão da IA e a resposta real (y)
criterio = nn.MSELoss() 
otimizador = optim.SGD(modelo.parameters(), lr=0.1)

# 4. LOOP DE TREINAMENTO
print("Treinando a IA para aprender a porta OR...")
for epoca in range(1000):
    # Passo 1: Forward (A IA tenta adivinhar)
    previsao = modelo(X)
    
    # Passo 2: Calcular o Erro (Loss)
    erro = criterio(previsao, y)
    
    # Passo 3: Backpropagation (O Segredo!)
    otimizador.zero_grad() # Limpa os gradientes anteriores
    erro.backward()        # Calcula para onde ajustar os pesos
    otimizador.step()      # Ajusta os pesos de fato
    
    if (epoca + 1) % 200 == 0:
        print(f"Época {epoca+1}/1000 - Erro: {erro.item():.4f}")

# 5. TESTANDO A IA
print("\nTeste Final:")
com_quem_testar = torch.tensor([[0.0, 0.0], [1.0, 1.0]])
resultado = modelo(com_quem_testar)

for i in range(len(com_quem_testar)):
    entrada = com_quem_testar[i].tolist()
    previsao = resultado[i].item()
    print(f"Entrada: {entrada} -> Previsão da IA: {previsao:.4f} ({'TRUE' if previsao > 0.5 else 'FALSE'})")

print("\nConclusão: A IA aprendeu a lógica OR apenas olhando os exemplos!")
