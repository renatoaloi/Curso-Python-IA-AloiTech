import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

# Inicializando o MediaPipe para mãos
mp_maos = mp.solutions.hands
# Detectando apenas 1 mão para evitar confusão no mouse
maos = mp_maos.Hands(max_num_hands=1) 
mp_desenho = mp.solutions.drawing_utils

while True:
    sucesso, frame = cap.read()
    if not sucesso:
        break
        
    frame = cv2.flip(frame, 1)
    
    # O MediaPipe precisa da imagem em formato RGB, mas o OpenCV usa BGR
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Processa a imagem e procura por mãos
    resultado = maos.process(frame_rgb)
    
    # Se encontrou alguma mão na tela
    if resultado.multi_hand_landmarks:
        for mao_landmarks in resultado.multi_hand_landmarks:
            # Desenha os pontos e ligações na imagem original (frame)
            mp_desenho.draw_landmarks(frame, mao_landmarks, mp_maos.HAND_CONNECTIONS)
            
    cv2.imshow("Mouse Virtual - Rastreio", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
