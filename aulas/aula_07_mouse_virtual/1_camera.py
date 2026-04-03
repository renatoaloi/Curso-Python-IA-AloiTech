import cv2

# Inicializa a captura de vídeo (0 geralmente é a webcam principal)
cap = cv2.VideoCapture(0)

while True:
    # Lê a imagem atual da câmera
    sucesso, frame = cap.read()
    
    if not sucesso:
        print("Erro ao acessar a câmera.")
        break
        
    # Efeito espelho (ajuda na imersão)
    frame = cv2.flip(frame, 1)    
        
    # Mostra a imagem numa janela
    cv2.imshow("Mouse Virtual - Camera", frame)
    
    # Espera 1 milissegundo e verifica se a tecla 'q' foi pressionada para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
# Libera a câmera e fecha as janelas
cap.release()
cv2.destroyAllWindows()
