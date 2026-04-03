# Aula 07: Mouse Virtual com IA (Visão Computacional)

Nesta aula, aprendemos a criar um "Mouse Virtual" que funciona sem toque físico, sendo controlado apenas por gestos da mão capturados pela webcam. Usamos o poder combinado de Python, OpenCV, MediaPipe e PyAutoGUI para identificar os nós (landmarks) das nossas mãos em tempo real, fazer o mapeamento posicional da câmera com a tela real do computador, e implementar uma lógica baseada em distância geométrica entre os dedos para efetuar os "cliques", criando um mecanismo de filme de ficção científica do zero!

## 🎯 Objetivos da Aula
1. Entender como inicializar e transmitir o vídeo de uma webcam usando OpenCV.
2. Explorar ferramentas que ajudam a identificar a lista de câmeras conectadas no sistema (Windows).
3. Utilizar o MediaPipe para realizar o rastreamento em tempo real dos pontos articulados da mão (Hand Tracking).
4. Isolar nós essenciais da mão (como a ponta do dedo indicador e a ponta do polegar).
5. Interagir diretamente com o sistema operacional, convertendo as coordenadas virtuais em movimentação bruta do mouse via PyAutoGUI.

## 🧰 Ferramentas Utilizadas
- **Python**: A linguagem e ambiente principal para orquestrar e fazer tudo rodar.
- **OpenCV (`opencv-python`)**: Interface gigantesca de visão computacional, usada nesse projeto para acessar o hardware da webcam, trabalhar renderização das janelas e inverter o vídeo espelhando a imagem.
- **MediaPipe (`mediapipe`)**: A poderosa tecnologia do Google AI de Machine Learning. Fornece modelos pré-treinados facilitando todo o trabalho pesado de reconhecer todas as juntas da mão sem que a gente precise treinar uma rede neural da estaca zero.
- **PyAutoGUI (`pyautogui`)**: Biblioteca versátil que envia eventos para o sistema operacional emulando movimento de mouse e cliques no nível físico.
- **PyGrabber (`pygrabber`) *[Opcional, com foco no Windows]*:** Utilitário prático usado em aula para conectar com os drivers DirectShow ajudando a mapear o nome e o "Índice" da câmera desejada no Windows.

## 📂 Arquivos do Projeto
- `0_descobrir_camera.py`: Um script rápido de diagnóstico que lista todas as webcams pelo nome da fabricante e o ID correspondente usado no OpenCV (ajuda a evitar "chutes" de portas).
- `1_camera.py`: Código Base. A primeira etapa com a importação simples, abre a webcam e projeta a exibição corrigindo o modo espelho.
- `2_rastreamento.py`: Implementação da lógica de Visão Computacional. Ele tenta identificar mãos na câmera processando os frames em RGB e empilha uma camada visual de teias que formam o esqueleto mapeado.
- `2_5_editando_nos.py`: Etapa educacional focada no letramento em Landmarks, demonstrando como isolar dados puros. Pega exclusivamente o Ponto 8 (ponteiro indicador) e mostra como extrair apenas seu 'X e Y' de dentro dos objetos aninhados.
- `3_projeto_final.py`: A versão definitiva do código. Une toda a fundamentação. Sincroniza a câmera com a resolução nativa da sua tela para guiar o mouse, e calcula a hipotenusa da reta formada entre a ponta do indicador e do polegar para acionar o sinal que imita o clique mecânico do mouse.

## 🚀 Como Executar
1. Antes de iniciar, recomendamos que abra a pasta no terminal e ative o seu próprio ambiente virtual isolado (`venv`).
2. Tendo seu ambiente preparado, instale as dependências usando os pacotes Python:
   ```bash
   pip install opencv-python mediapipe pyautogui
   ```
3. *(Apenas para Windows)* Caso tenha múltiplas câmeras e desejar listar os índices corretamente para substituir dentro dos códigos listados abaixo antes de iniciar. Instale o pacote adicional:
   ```bash
   pip install pygrabber
   python 0_descobrir_camera.py
   ```
4. Para abrir diretamente a versão madura gerada no clímax do projeto prático, testada e completa:
   ```bash
   python 3_projeto_final.py
   ```
5. Com a execução rodando, faça o formato de pinça apontando o dedo na frente da lente de modo iluminado e veja o mouse acompanhar seus gestos. Para finalizar e retornar ao terminal, traga o foco na aba e pare a execução enviando a tecla `q`.
