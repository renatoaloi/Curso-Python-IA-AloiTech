import cv2
import mediapipe as mp
import pyautogui
import math

# Desliga a trava de segurança do canto da tela para o código não quebrar
pyautogui.FAILSAFE = False

cap = cv2.VideoCapture(0)
# Pegando o tamanho da tela real do computador para mapeamento
largura_tela, altura_tela = pyautogui.size()

mp_maos = mp.solutions.hands
maos = mp_maos.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_desenho = mp.solutions.drawing_utils

while True:
    sucesso, frame = cap.read()
    if not sucesso: break
        
    frame = cv2.flip(frame, 1)
    altura_frame, largura_frame, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultado = maos.process(frame_rgb)
    
    if resultado.multi_hand_landmarks:
        for mao_landmarks in resultado.multi_hand_landmarks:
            mp_desenho.draw_landmarks(frame, mao_landmarks, mp_maos.HAND_CONNECTIONS)
            
            # Encontrar as coordenadas do Indicador (ponto 8) e Polegar (ponto 4)
            x_indicador = int(mao_landmarks.landmark[8].x * largura_frame)
            y_indicador = int(mao_landmarks.landmark[8].y * altura_frame)
            
            x_polegar = int(mao_landmarks.landmark[4].x * largura_frame)
            y_polegar = int(mao_landmarks.landmark[4].y * altura_frame)
            
            # Movendo o mouse junto com o indicador
            # Converte a coordenada da câmera pra coordenada do monitor
            mouse_x = int((x_indicador / largura_frame) * largura_tela)
            mouse_y = int((y_indicador / altura_frame) * altura_tela)
            
            pyautogui.moveTo(mouse_x, mouse_y)
            
            # Destacar as pontas dos dedos usados
            cv2.circle(frame, (x_indicador, y_indicador), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(frame, (x_polegar, y_polegar), 10, (0, 255, 0), cv2.FILLED)
            
            # Lógica do Clique: Calculando a distância entre o indicador e o polegar
            distancia = math.hypot(x_polegar - x_indicador, y_polegar - y_indicador)
            
            # Se as pontas dos dedos estiverem próximas (menos de 30 pixels), é um clique!
            if distancia < 30:
                cv2.circle(frame, (x_indicador, y_indicador), 10, (0, 0, 255), cv2.FILLED) # Fica vermelho
                pyautogui.click()
                pyautogui.sleep(0.2) # Pausa rápida pra não clicar milhares de vezes
                
    cv2.imshow("Mouse Virtual - Projeto Final", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
