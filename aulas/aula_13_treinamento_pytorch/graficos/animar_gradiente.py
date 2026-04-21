import os
import sys
import subprocess
import math
import shutil
from datetime import datetime

# Instalando dependências se necessário
try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Instalando Pillow...")
    subprocess.run([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageDraw, ImageFont

# CONFIGURAÇÕES DE DIRETÓRIOS
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
TEMP_DIR = os.path.join(ROOT_DIR, "tmp")

# CONFIGURAÇÕES DA ANIMAÇÃO
WIDTH, HEIGHT = 1280, 720
FPS = 30
DURATION = 4  # segundos
TOTAL_FRAMES = FPS * DURATION

# Cores (Estética Tech/Neon)
BG_COLOR = (10, 10, 10)
AXIS_COLOR = (100, 100, 100)
CURVE_COLOR = (0, 255, 255)    # Cyan
POINT_COLOR = (255, 255, 255)  # White
TEXT_COLOR = (255, 255, 255)

# NOVAS CORES DE STATUS
COLOR_SUCCESS = (0, 255, 100)  # Verde Neon
COLOR_ERROR = (255, 50, 50)    # Vermelho Neon

# Escala do gráfico
SCALE_X = 100 
SCALE_Y = 20
OFFSET_X = WIDTH // 2
OFFSET_Y = HEIGHT - 150

def draw_frame(frame_idx, target_x):
    # 1. Preparar Fontes no topo para reuso
    font_size_main = 40
    font_size_info = 30
    try:
        font_main = ImageFont.truetype("arial.ttf", font_size_main)
        font_info = ImageFont.truetype("arial.ttf", font_size_info)
    except:
        font_main = ImageFont.load_default()
        font_info = ImageFont.load_default()

    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Desenhar Eixos
    draw.line([(0, OFFSET_Y), (WIDTH, OFFSET_Y)], fill=AXIS_COLOR, width=2)
    draw.line([(OFFSET_X, 0), (OFFSET_X, HEIGHT)], fill=AXIS_COLOR, width=2)
    
    # Progresso da animação (0.0 a 1.0)
    progress = frame_idx / TOTAL_FRAMES
    
    # Desenhar a Parábola (y = x²)
    points = []
    for x_val in range(-600, 600, 5):
        x_float = x_val / 100.0
        y_float = x_float ** 2
        px_curve = OFFSET_X + (x_float * SCALE_X)
        py_curve = OFFSET_Y - (y_float * SCALE_Y)
        points.append((px_curve, py_curve))
    
    if len(points) > 1:
        draw.line(points, fill=CURVE_COLOR, width=3)
        
    # Ponto x animado de 0 até o target_x
    current_x = progress * target_x 
    current_y = current_x ** 2
    
    px = OFFSET_X + (current_x * SCALE_X)
    py = OFFSET_Y - (current_y * SCALE_Y)
    
    # DEFINIR COR DO GRADIENTE BASEADO NA LÓGICA DO USUÁRIO
    TANGENT_COLOR = COLOR_SUCCESS if current_x < 2.0 else COLOR_ERROR

    # Desenhar Reta Tangente (Gradiente) conforme o ponto se move
    if progress > 0.5: # Começa a mostrar o gradiente no meio da animação
        slope = 2 * current_x # Derivada de x² é 2x
        x1, x2 = current_x - 1.0, current_x + 1.0
        y1 = slope * (x1 - current_x) + current_y
        y2 = slope * (x2 - current_x) + current_y
        
        p1x, p1y = OFFSET_X + (x1 * SCALE_X), OFFSET_Y - (y1 * SCALE_Y)
        p2x, p2y = OFFSET_X + (x2 * SCALE_X), OFFSET_Y - (y2 * SCALE_Y)
        draw.line([(p1x, p1y), (p2x, p2y)], fill=TANGENT_COLOR, width=5)
        
        # Legenda do Gradiente (USANDO FONT_INFO)
        draw.text((px + 20, py - 80), f"Gradiente = {slope:.2f}", fill=TANGENT_COLOR, font=font_info)
        status_text = "DENTRO DO LIMITE" if current_x < 2.0 else "PERIGO: FORA DO LIMITE"
        draw.text((px + 20, py - 45), status_text, fill=TANGENT_COLOR, font=font_info)

    # Ponto Pulsante
    r = 8
    draw.ellipse([px-r, py-r, px+r, py+r], fill=TANGENT_COLOR) # O ponto assume a cor do status
    
    # Legenda Principal (Inferior)
    legenda = f"Testando peso: x = {current_x:.2f}"
    
    # Fundo da legenda (TOPO)
    # Colocamos no topo para não ser coberto pelos controles do tocador de vídeo
    draw.rectangle([0, 0, WIDTH, 80], fill=(0,0,0, 150))
    # Centralizar texto
    bbox = draw.textbbox((0, 0), legenda, font=font_main)
    tw = bbox[2] - bbox[0]
    draw.text(((WIDTH - tw) // 2, 15), legenda, font=font_main, fill=TEXT_COLOR)

    # Salvar frame
    img.save(f"{TEMP_DIR}/frame_{frame_idx:04d}.png")

def main():
    # Pergunta o valor de X para o usuário
    try:
        val_x = input("Digite o valor de X para a animação (ex: 1.5 ou 3.0): ")
        target_x = float(val_x)
    except ValueError:
        print("Valor inválido! Usando padrão x = 2.5")
        target_x = 2.5

    # Define o nome do arquivo com timestamp e o valor de X
    # Caminho relativo ao local do script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    videos_dir = os.path.join(base_dir, "videos")
    
    if not os.path.exists(videos_dir):
        os.makedirs(videos_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    OUTPUT_VIDEO = os.path.join(videos_dir, f"gradient_anim_x{target_x}_{timestamp}.mp4")

    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)
        
    print(f"Gerando animação para x={target_x}...")
    print(f"Gerando {TOTAL_FRAMES} frames...")
    
    for i in range(TOTAL_FRAMES):
        draw_frame(i, target_x)
        if i % 30 == 0:
            print(f"Frame {i}/{TOTAL_FRAMES}...")
            
    print("Compilando vídeo com FFmpeg...")
    cmd = [
        "ffmpeg", "-y",
        "-framerate", str(FPS),
        "-i", f"{TEMP_DIR}/frame_%04d.png",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        OUTPUT_VIDEO
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"\n[SUCESSO] Video gerado em: {OUTPUT_VIDEO}")
        if os.path.exists(TEMP_DIR):
            shutil.rmtree(TEMP_DIR)
    else:
        print("[ERRO] Erro ao gerar vídeo:")
        print(result.stderr)

if __name__ == "__main__":
    main()
