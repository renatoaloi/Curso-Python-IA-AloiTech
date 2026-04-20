import torch
import pandas as pd
from torch.utils.data import Dataset, DataLoader
from collections import Counter

# Aula 13.2: O Pipeline de Dados (De Texto para Números)

# 1. Carregando o Dataset Real (CSV)
df = pd.read_csv("comentarios_videos.csv")
print("Exemplo do Dataset:")
print(df.head())

# 2. Processamento de Texto: Criando o Vocabulário
# Precisamos de uma lista de todas as palavras únicas que a nossa IA conhece
todas_as_palavras = " ".join(df['texto'].str.lower()).split()
contagem = Counter(todas_as_palavras)
# Pegamos as 100 palavras mais comuns (simplificando)
vocabulario = {palavra: i for i, (palavra, _) in enumerate(contagem.most_common(100))}
print(f"\nTamanho do Vocabulário: {len(vocabulario)}")

# 3. Função "Bag of Words" (Saco de Palavras)
# Transforma uma frase em um vetor de 0s e 1s
def frase_para_tensor(frase, vocab):
    vetor = torch.zeros(len(vocab))
    for palavra in frase.lower().split():
        if palavra in vocab:
            vetor[vocab[palavra]] = 1
    return vetor

# 4. Criando o Dataset Customizado do PyTorch
class MeuDataset(Dataset):
    def __init__(self, df, vocab):
        self.dados = df
        self.vocab = vocab
    
    def __len__(self):
        return len(self.dados)
    
    def __getitem__(self, idx):
        frase = self.dados.iloc[idx]['texto']
        sentimento = self.dados.iloc[idx]['sentimento']
        
        X = frase_para_tensor(frase, self.vocab)
        y = torch.tensor(sentimento, dtype=torch.float32)
        
        return X, y

# 5. O DataLoader (O garçom de dados)
dataset_treino = MeuDataset(df, vocabulario)
carregador = DataLoader(dataset_treino, batch_size=4, shuffle=True)

# Testando um lote (batch)
X_lote, y_lote = next(iter(carregador))
print(f"\nShape do Lote X: {X_lote.shape}") # [4, 100] -> 4 frases, vetor de 100 palavras
print(f"Sentimentos do Lote: {y_lote}")

print("\nDados preparados! Agora podemos treinar a rede.")
