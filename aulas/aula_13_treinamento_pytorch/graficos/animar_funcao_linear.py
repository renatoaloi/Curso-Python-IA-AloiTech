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
DURATION = 8  # Segundos totais
TOTAL_FRAMES = FPS * DURATION

# Cores (Estética Tech/Neon)
BG_COLOR = (10, 10, 10)
AXIS_COLOR = (80, 80, 80)
LINE_COLOR = (0, 255, 255)     # Cyan (Reta y = wx)
POINT_COLOR = (0, 255, 100)    # Verde Neon
DASH_COLOR = (200, 200, 200)   # Cinza claro para linhas de alinhamento
TEXT_COLOR = (255, 255, 255)

# Posição do Eixo (Offset) - Colocando um pouco para a esquerda e para baixo
OFFSET_X = 200
OFFSET_Y = HEIGHT - 150

def draw_dashed_line(draw, p1, p2, fill, width=1, dash_length=10):
    """Desenha uma linha tracejada entre p1 e p2."""
    x1, y1 = p1
    x2, y2 = p2
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if dist == 0: return
    
    segments = int(dist / dash_length)
    dx = (x2 - x1) / dist
    dy = (y2 - y1) / dist
    
    for i in range(0, segments, 2):
        start = (x1 + dx * i * dash_length, y1 + dy * i * dash_length)
        end = (x1 + dx * (i + 1) * dash_length, y1 + dy * (i + 1) * dash_length)
        draw.line([start, end], fill=fill, width=width)

def draw_frame(frame_idx, w, x_list, scale_x, scale_y):
    # 1. Preparar Fontes
    try:
        font_main = ImageFont.truetype("arial.ttf", 40)
        font_info = ImageFont.truetype("arial.ttf", 30)
    except:
        font_main = ImageFont.load_default()
        font_info = ImageFont.load_default()

    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Desenhar Eixos
    draw.line([(OFFSET_X - 100, OFFSET_Y), (WIDTH, OFFSET_Y)], fill=AXIS_COLOR, width=2)
    draw.line([(OFFSET_X, 0), (OFFSET_X, OFFSET_Y + 100)], fill=AXIS_COLOR, width=2)
    
    # Desenhar Reta y = wx de ponta a ponta (dentro da área visível)
    x_start, x_end = -1, 20 # Range estendido
    p_start = (OFFSET_X + x_start * scale_x, OFFSET_Y - (w * x_start) * scale_y)
    p_end = (OFFSET_X + x_end * scale_x, OFFSET_Y - (w * x_end) * scale_y)
    draw.line([p_start, p_end], fill=LINE_COLOR, width=3)
    
    # Lógica de salto: Qual item da lista mostrar?
    num_items = len(x_list)
    frames_per_item = TOTAL_FRAMES // num_items
    current_idx = min(frame_idx // frames_per_item, num_items - 1)
    
    current_x = x_list[current_idx]
    current_y = w * current_x
    
    # Converter para pixels
    px = OFFSET_X + (current_x * scale_x)
    py = OFFSET_Y - (current_y * scale_y)
    
    # Desenhar Linhas de Alinhamento (Tracejadas)
    # Linha até o Eixo X
    draw_dashed_line(draw, (px, py), (px, OFFSET_Y), fill=DASH_COLOR, width=2)
    # Linha até o Eixo Y
    draw_dashed_line(draw, (px, py), (OFFSET_X, py), fill=DASH_COLOR, width=2)
    
    # Ponto Animado
    r = 12
    draw.ellipse([px-r, py-r, px+r, py+r], fill=POINT_COLOR, outline=TEXT_COLOR, width=2)
    
    # Legendas de valores nos eixos
    draw.text((px - 15, OFFSET_Y + 10), f"x={current_x}", fill=TEXT_COLOR, font=font_info)
    draw.text((OFFSET_X - 100, py - 15), f"y={current_y:.2f}", fill=TEXT_COLOR, font=font_info)

    # Painel de Informações (Topo)
    legenda = f"Função Linear: y = {w} * {current_x} = {current_y:.2f}"
    draw.rectangle([0, 0, WIDTH, 80], fill=(0, 0, 0, 180))
    
    bbox = draw.textbbox((0, 0), legenda, font=font_main)
    tw = bbox[2] - bbox[0]
    draw.text(((WIDTH - tw) // 2, 15), legenda, font=font_main, fill=TEXT_COLOR)

    # Indicação do Peso (W)
    draw.text((OFFSET_X + 50, 100), f"Peso (w) = {w}", fill=LINE_COLOR, font=font_main)

    img.save(f"{TEMP_DIR}/frame_{frame_idx:04d}.png")

def main():
    print("--- ANIMADOR DE FUNÇÃO LINEAR (y = wx) ---")
    try:
        w = float(input("Digite o valor do peso (w): "))
        x_str = input("Digite a lista de valores de X separados por vírgula (ex: 1, 2, 3): ")
        x_list = [float(x.strip()) for x in x_str.split(",")]
    except ValueError:
        print("Valores inválidos! Usando w=2 e x=[1, 2, 3, 4, 5]")
        w = 2.0
        x_list = [1, 2, 3, 4, 5]

    # Cálculo automático de escala para caber na tela
    max_x = max(x_list) if x_list else 1
    max_y = w * max_x
    
    # Queremos que o ponto mais distante fique a ~80% da tela
    scale_x = (WIDTH - OFFSET_X - 100) / max_x
    scale_y = (OFFSET_Y - 100) / max_y
    
    # Usamos o menor valor de escala para manter a proporção 1:1 se desejado, 
    # Caminho relativo ao local do script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    videos_dir = os.path.join(base_dir, "videos")
    
    if not os.path.exists(videos_dir):
        os.makedirs(videos_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    OUTPUT_VIDEO = os.path.join(videos_dir, f"linear_anim_w{w}_{timestamp}.mp4")

    print(f"Gerando animação para y = {w}x com {len(x_list)} pontos...")
    
    for i in range(TOTAL_FRAMES):
        draw_frame(i, w, x_list, scale_x, scale_y)
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
        print(f"\n[SUCESSO] Vídeo gerado em: {OUTPUT_VIDEO}")
        if os.path.exists(TEMP_DIR):
            shutil.rmtree(TEMP_DIR)
    else:
        print("[ERRO] Erro ao gerar vídeo:")
        print(result.stderr)

if __name__ == "__main__":
    main()
