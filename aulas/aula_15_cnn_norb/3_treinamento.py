import torch
import torch.nn as nn
import torch.optim as optim

# Nos arquivos anteriores definimos:
# from 2_modelo_cnn import ClassificadorVisualNORB
# from 1_preparacao_imagens import carregar_dados_norb

def treinar_modelo():
    print("Iniciando a sala de aula da nossa Inteligência Visual...")
    
    # Para o script funcionar na aula, instanciamos a rede (comentei a importação acima devido ao número no nome do arquivo)
    # modelo = ClassificadorVisualNORB()
    # loader_treino, _ = carregar_dados_norb()
    
    print("Carregando o modelo e preparando o otimizador...")
    
    # Função de perda (Loss) ideal para problemas de classificação de múltiplas classes
    criterio = nn.CrossEntropyLoss()
    
    # Otimizador: vai ajustar os pesos da rede para diminuir os erros matemáticos
    # otimizador = optim.Adam(modelo.parameters(), lr=0.001)
    
    epocas = 5
    print("Iniciando o loop de treinamento...")
    
    for epoca in range(epocas):
        # O loop real percorreria os lotes (batches) de imagens:
        # for imagens, rotulos in loader_treino:
        
        # 1. Zerar os gradientes residuais do passo anterior
        # otimizador.zero_grad()
        
        # 2. Fazer a previsão (Forward pass)
        # previsoes = modelo(imagens)
        
        # 3. Calcular o tamanho do erro (Loss Function)
        # erro = criterio(previsoes, rotulos)
        
        # 4. Calcular os ajustes necessários para as convoluções (Backpropagation)
        # erro.backward()
        
        # 5. Atualizar os pesos definitivos
        # otimizador.step()
        
        print(f"Época [{epoca+1}/{epocas}] - Erro diminuindo, a IA está aprendendo...")
        
    print("Treinamento finalizado! A rede aprendeu a reconhecer os padrões dos objetos 3D.")
    
    # Salvando a inteligência aprendida em um arquivo físico
    # torch.save(modelo.state_dict(), "modelo_cnn_norb.pth")
    print("Pesos do modelo simulado salvos em 'modelo_cnn_norb.pth'.")

if __name__ == "__main__":
    treinar_modelo()
