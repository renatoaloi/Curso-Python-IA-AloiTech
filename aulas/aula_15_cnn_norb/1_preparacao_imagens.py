import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

def carregar_dados_norb(batch_size=32):
    """
    Função para carregar as imagens binoculares e convertê-las em tensores.
    """
    print("Iniciando a preparação do Dataset NORB...")
    
    # As transformações convertem a imagem bruta para matrizes matemáticas (Tensores)
    # e normalizam os pixels para ajudar a rede neural a aprender mais rápido.
    transformacao = transforms.Compose([
        transforms.Resize((96, 96)), # O NORB geralmente usa imagens 96x96
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,)) # Normalização de cores
    ])
    
    try:
        # Tenta carregar o dataset nativo. Caso a versão do PyTorch não suporte SmallNORB nativamente,
        # o professor usará um script customizado para a aula.
        dataset_treino = datasets.SmallNORB(root='./data', split='train', download=True, transform=transformacao)
        dataset_teste = datasets.SmallNORB(root='./data', split='test', download=True, transform=transformacao)
        
        loader_treino = DataLoader(dataset_treino, batch_size=batch_size, shuffle=True)
        loader_teste = DataLoader(dataset_teste, batch_size=batch_size, shuffle=False)
        
        print(f"Dados carregados! Treino: {len(dataset_treino)} amostras | Teste: {len(dataset_teste)} amostras.")
        return loader_treino, loader_teste
        
    except AttributeError:
        print("Aviso: O dataset SmallNORB não está disponível nativamente na sua versão do torchvision.")
        print("Você precisará de um script customizado para extrair os arquivos binários do Yann LeCun.")
        return None, None

if __name__ == "__main__":
    carregar_dados_norb()
