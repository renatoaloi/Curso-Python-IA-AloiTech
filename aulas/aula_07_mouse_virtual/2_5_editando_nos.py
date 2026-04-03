import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_maos = mp.solutions.hands
maos = mp_maos.Hands(max_num_hands=1) 
mp_desenho = mp.solutions.drawing_utils

while True:
    sucesso, frame = cap.read()
    if not sucesso:
        break
        
    frame = cv2.flip(frame, 1)
    
    # Precisamos das dimensões da tela para converter as posições em pixels
    altura_frame, largura_frame, _ = frame.shape
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultado = maos.process(frame_rgb)
    
    if resultado.multi_hand_landmarks:
        for mao_landmarks in resultado.multi_hand_landmarks:
            mp_desenho.draw_landmarks(frame, mao_landmarks, mp_maos.HAND_CONNECTIONS)
            
            # Pegando as coordenadas exclusivas do dedo indicador (ponto 8)
            # O MediaPipe retorna 'x' e 'y' em uma proporção de 0.0 a 1.0 (percentual)
            # Então multiplicamos pelo tamanho da imagem para achar a posição (pixel) exata
            x_indicador = int(mao_landmarks.landmark[8].x * largura_frame)
            y_indicador = int(mao_landmarks.landmark[8].y * altura_frame)
            
            # Desenhando um círculo azul na ponta do indicador (BGR: 255, 0, 0 = Azul)
            cv2.circle(frame, (x_indicador, y_indicador), 15, (255, 0, 0), cv2.FILLED)
            
            # Adicionando o texto "Ponteiro" próximo ao círculo
            cv2.putText(frame, "Ponteiro", (x_indicador + 20, y_indicador), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            
    cv2.imshow("Mouse Virtual - Editando Nós", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
