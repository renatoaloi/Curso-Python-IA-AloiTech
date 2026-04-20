import torch

# Aula 13.1: Entendendo Tensores (Os átomos da IA)
#
# Um Tensor é a unidade fundamental de dados no Deep Learning. 
# Pense neles como "Containers Inteligentes" de números.
# Enquanto uma lista do Python é apenas uma gaveta de valores, 
# um Tensor é uma estrutura otimizada que pode ser processada 
# milhares de vezes mais rápido por uma GPU (Placa de Vídeo).
#
# Eles podem ter várias dimensões:
# - 0D (Escalar): Um único número (Ex: o preço de uma casa)
# - 1D (Vetor): Uma lista de números (Ex: histórico de preços)
# - 2D (Matriz): Uma tabela (Ex: pixels de uma foto em P&B)
# - 3D (Cubo): Um empilhamento de tabelas (Ex: uma foto colorida RGB)

# 1. Criando um tensor simples (Escalar)
item = torch.tensor(13.0)
print(f"Tensor 0D (Escalar): {item}, Shape: {item.shape}")

# 2. Criando um vetor (1D)
vetor = torch.tensor([1.0, 2.0, 3.0])
print(f"Tensor 1D (Vetor): {vetor}, Shape: {vetor.shape}")

# 3. Criando uma matriz (2D)
matriz = torch.tensor([[1, 2], [3, 4]])
print(f"Tensor 2D (Matriz):\n{matriz}\nShape: {matriz.shape}")

# 4. Criando um tensor 3D (Cubo de dados)
# Útil para representar imagens coloridas (RGB) ou sequências de dados
cubo = torch.tensor([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print(f"\nTensor 3D (Cubo):\n{cubo}\nShape: {cubo.shape}")

# 4. Operações Matemáticas
a = torch.tensor([1, 2])
b = torch.tensor([3, 4])
soma = a + b
print(f"Soma: {soma}")

# 5. O SEGREDO DO APRENDIZADO: Gradients
# No PyTorch, podemos marcar um tensor para "seguir" as mudanças matemáticas
x = torch.tensor(2.0, requires_grad=True)
y = x ** 2  # y = x²

# Calculando a derivada (Backpropagation manual simples)
y.backward()

# Qual a inclinação (gradiente) de x² quando x=2? (A resposta é 2x, ou seja, 4)
print(f"Gradiente em x=2: {x.grad}")

print("\nConclusão: O PyTorch não é só para números, ele 'sabe' matemática!")
