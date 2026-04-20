import torch
import torch.nn as nn

# Aula 13.4: Testando sua IA Treinada (Inferência)

# 1. Definindo a mesma arquitetura
class ClassificadorTexto(nn.Module):
    def __init__(self, tamanho_vocab):
        super(ClassificadorTexto, self).__init__()
        self.camada_entrada = nn.Linear(tamanho_vocab, 16)
        self.ativacao = nn.ReLU()
        self.camada_saida = nn.Linear(16, 1)
        self.sigmoide = nn.Sigmoid()
        
    def forward(self, x):
        return self.sigmoide(self.camada_saida(self.ativacao(self.camada_entrada(x))))

# 2. Carregando o "Cérebro" e o Vocabulário
checkpoint = torch.load("modelo_ia.pth")
vocabulario = checkpoint['vocab']

modelo = ClassificadorTexto(len(vocabulario))
modelo.load_state_dict(checkpoint['state_dict'])
modelo.eval() # Modo de avaliação (não treina mais)

# 3. Função para prever
def prever_sentimento(frase):
    # Transforma frase em vetor
    vetor = torch.zeros(len(vocabulario))
    for palavra in frase.lower().split():
        if palavra in vocabulario:
            vetor[vocabulario[palavra]] = 1
    
    # Faz a conta
    with torch.no_grad():
        probabilidade = modelo(vetor).item()
    
    return "POSITIVO 😊" if probabilidade > 0.5 else "NEGATIVO 😠", probabilidade

# 4. Loop de interação
print("--- TESTADOR DE SENTIMENTO IA ---")
print("Digite 'sair' para encerrar.")

while True:
    texto_usuario = input("\nDigite um comentário para a IA analisar: ")
    if texto_usuario.lower() == 'sair':
        break
    
    resultado, confianca = prever_sentimento(texto_usuario)
    print(f"Resultado: {resultado}")
    print(f"Confiança: {confianca:.2%}")
