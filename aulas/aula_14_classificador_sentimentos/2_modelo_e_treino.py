import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from torch.utils.data import Dataset, DataLoader
from collections import Counter

# Aula 14.2: Arquitetura e Treinamento (A Mágica)

# --- REPETINDO PREPARAÇÃO (Para o script ser independente) ---
df = pd.read_csv("comentarios_videos.csv")
todas_as_palavras = " ".join(df['texto'].str.lower()).split()
contagem = Counter(todas_as_palavras)
vocabulario = {palavra: i for i, (palavra, _) in enumerate(contagem.most_common(100))}

def frase_para_tensor(frase, vocab):
    vetor = torch.zeros(len(vocab))
    for palavra in frase.lower().split():
        if palavra in vocab:
            vetor[vocab[palavra]] = 1
    return vetor

class MeuDataset(Dataset):
    def __init__(self, df, vocab):
        self.dados = df
        self.vocab = vocab
    def __len__(self): return len(self.dados)
    def __getitem__(self, idx):
        X = frase_para_tensor(self.dados.iloc[idx]['texto'], self.vocab)
        y = torch.tensor(self.dados.iloc[idx]['sentimento'], dtype=torch.float32)
        return X, y

dataset = MeuDataset(df, vocabulario)
carregador = DataLoader(dataset, batch_size=4, shuffle=True)
# -----------------------------------------------------------

# 1. DEFINIÇÃO DA ARQUITETURA
class ClassificadorTexto(nn.Module):
    def __init__(self, tamanho_vocab):
        super(ClassificadorTexto, self).__init__()
        # Camada Linear: y = wx + b
        # Entrada: tamanho do vocabulário (100)
        # Saída: 1 (Positivo ou Negativo)
        self.camada_entrada = nn.Linear(tamanho_vocab, 16) # 16 Neurônios na camada oculta
        self.ativacao = nn.ReLU() # Função de ativação
        self.camada_saida = nn.Linear(16, 1)
        self.sigmoide = nn.Sigmoid() # Transforma o número final em uma probabilidade de 0 a 1
        
    def forward(self, x):
        x = self.camada_entrada(x)
        x = self.ativacao(x)
        x = self.camada_saida(x)
        x = self.sigmoide(x)
        return x

# 2. INSTANCIANDO O MODELO, FUNÇÃO DE PERDA E OTIMIZADOR
modelo = ClassificadorTexto(len(vocabulario))
criterio = nn.BCELoss() # Binary Cross Entropy (Ideal para 0 ou 1)
otimizador = optim.Adam(modelo.parameters(), lr=0.01) # Adam é um dos melhores otimizadores

# 3. LOOP DE TREINAMENTO
print("Iniciando Treinamento...")
epocas = 50 # Quantas vezes a IA vai ler o dataset completo

for epoca in range(epocas):
    perda_total = 0
    for X_lote, y_lote in carregador:
        # Resetamos os gradientes
        otimizador.zero_grad()
        
        # Forward: A IA tenta prever
        previsoes = modelo(X_lote).squeeze() # squeeze remove dimensões extras
        
        # Calculamos o erro
        perda = criterio(previsoes, y_lote)
        
        # Backward: A IA aprende com o erro (Matemática pesada aqui!)
        perda.backward()
        
        # Passo do otimizador: Ajusta os pesos W e b
        otimizador.step()
        
        perda_total += perda.item()
    
    if (epoca + 1) % 10 == 0:
        print(f"Época {epoca+1}/{epocas} - Perda (Loss): {perda_total/len(carregador):.4f}")

# 4. SALVANDO O CÉREBRO DA IA
torch.save({'state_dict': modelo.state_dict(), 'vocab': vocabulario}, "modelo_ia.pth")
print("\nTreinamento Finalizado! Modelo salvo como 'modelo_ia.pth'")
