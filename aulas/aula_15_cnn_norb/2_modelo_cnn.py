import torch
import torch.nn as nn
import torch.nn.functional as F

class ClassificadorVisualNORB(nn.Module):
    def __init__(self):
        super(ClassificadorVisualNORB, self).__init__()
        
        # O NORB possui imagens de 1 canal (escala de cinza) capturadas de forma binocular.
        # Estamos assumindo entrada de 1 canal (imagem 96x96) para simplificar a didática.
        
        # 1. Primeira Camada de Convolução: Extrai padrões básicos (bordas, linhas)
        # Entrada: 1 canal (imagem) | Saída: 16 filtros de características | Kernel: Janela 3x3
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, padding=1)
        
        # Camada de Pooling: Reduz o tamanho da imagem pela metade, guardando apenas o essencial
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        
        # 2. Segunda Camada de Convolução: Extrai formas mais complexas
        # Entrada: 16 filtros anteriores | Saída: 32 novos filtros mais complexos
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1)
        
        # Após 2 convoluções e 2 poolings, a imagem de 96x96 cai para 24x24 pixels.
        # Total de características finais: 32 canais * 24 pixels * 24 pixels = 18432
        self.fc1 = nn.Linear(32 * 24 * 24, 128)
        
        # 3. Saída Final: 5 categorias de brinquedos (animais, humanos, aviões, caminhões, carros)
        self.fc2 = nn.Linear(128, 5)

    def forward(self, x):
        # Passo a passo da informação dentro do "cérebro"
        
        # Passa pela convolução 1 -> Ativação ReLU (remove valores negativos) -> Pooling
        x = self.pool(F.relu(self.conv1(x)))
        
        # Passa pela convolução 2 -> Ativação ReLU -> Pooling
        x = self.pool(F.relu(self.conv2(x)))
        
        # Achata a matriz multidimensional em um vetor 1D para a rede densa final
        x = x.view(-1, 32 * 24 * 24)
        
        # Passa pelas camadas neurais tradicionais
        x = F.relu(self.fc1(x))
        x = self.fc2(x) # Retorna os scores (logits) para as 5 categorias
        
        return x

if __name__ == "__main__":
    modelo = ClassificadorVisualNORB()
    print("Estrutura da nossa Rede Neural Convolucional:")
    print(modelo)
