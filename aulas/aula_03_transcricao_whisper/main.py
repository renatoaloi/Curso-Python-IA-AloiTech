import subprocess
import whisper
import os

def extrair_audio(caminho_video, caminho_audio):
    """
    Função para extrair o áudio de um arquivo de vídeo usando o FFmpeg.
    """
    print(f"🎬 Extraindo áudio de: {caminho_video}...")
    
    # O comando ffmpeg para converter video para MP3
    # -i: arquivo de entrada
    # -q:a 0: melhor qualidade de áudio mp3
    # -map a: mapeia apenas a trilha de áudio
    comando = [
        "ffmpeg", 
        "-i", caminho_video, 
        "-q:a", "0", 
        "-map", "a", 
        caminho_audio,
        "-y" # Sobrescreve se já existir
    ]
    
    # Roda o comando no terminal em segundo plano e omite os logs feios
    subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("✅ Áudio extraído com sucesso!")

def transcrever_audio(caminho_audio):
    """
    Função que carrega a IA Whisper e gera o texto a partir do áudio.
    """
    print("🤖 Carregando o modelo de IA Whisper (Isso pode demorar um pouco na primeira vez)...")
    
    # O Whisper tem vários modelos: 'tiny', 'base', 'small', 'medium', 'large'
    # 'base' é o padrão rápido para testes iniciais
    modelo = whisper.load_model("base")
    
    print("🎧 Ouvindo e transcrevendo... Aguarde.")
    # A IA processa o áudio e nos devolve um dicionário com o resultado
    resultado = modelo.transcribe(caminho_audio)
    
    print("\n" + "="*50)
    print("📜 TRANSCRIÇÃO FINALIZADA:")
    print("="*50)
    print(resultado["text"])
    print("="*50 + "\n")

if __name__ == "__main__":
    # Nomes dos arquivos
    video_entrada = "video_teste.mp4"
    audio_saida = "audio_temporario.mp3"
    
    # Passo 1: Verifica se o vídeo existe na pasta
    if not os.path.exists(video_entrada):
        print(f"❌ Erro: Coloque um vídeo chamado '{video_entrada}' nesta pasta para testar!")
    else:
        # Passo 2: Extrai o áudio
        extrair_audio(video_entrada, audio_saida)
        
        # Passo 3: Transcreve usando IA
        transcrever_audio(audio_saida)
