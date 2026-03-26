import yt_dlp
import whisper
import ollama # Requer ter o Ollama instalado e o modelo llama3 baixado localmente
import os

def baixar_audio(url):
    print(f"[*] Baixando áudio de: {url}")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio_baixado.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'quiet': True,
        'no_warnings': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("[+] Download e extração de áudio concluídos.")
    return "audio_baixado.mp3"

def transcrever_audio(caminho_audio):
    print("[*] Carregando modelo Whisper (base) e transcrevendo...")
    # O modelo 'base' exige menos processamento e é mais rápido para nossos testes
    modelo = whisper.load_model("base")
    
    # O parâmetro fp16=False evita alertas em CPUs sem suporte a meia precisão (comum no Windows)
    resultado = modelo.transcribe(caminho_audio, fp16=False)
    
    print("[+] Transcrição concluída. Texto extraído com sucesso.")
    return resultado["text"]

def gerar_titulos(texto_transcrito):
    print("[*] Conectando com a IA (Llama 3 via Ollama) para gerar títulos mágicos...")
    
    prompt = f"""
    Você é um especialista em YouTube e marketing digital brasileiro.
    Baseado na transcrição de um vídeo abaixo, crie 3 opções de títulos altamente 
    vírais e chamativos para o YouTube. Os títulos devem gerar curiosidade e cliques.
    Retorne apenas os 3 títulos em português do Brasil em uma lista numerada.
    
    Transcrição do Vídeo:
    {texto_transcrito}
    """
    
    # Fazendo requisição para a IA local (Ollama)
    resposta = ollama.chat(model='llama3', messages=[
        {'role': 'user', 'content': prompt}
    ])
    
    return resposta['message']['content']

if __name__ == "__main__":
    print("====================================")
    print("🤖 GERADOR DE TÍTULOS COM IA")
    print("====================================\n")
    
    url_video = input("Cole a URL do vídeo do YouTube (ex: um Short curto): ")
    
    try:
        # Passo 1: Baixar Áudio usando yt-dlp e FFmpeg
        arquivo_audio = baixar_audio(url_video)
        
        # Passo 2: Transcrever Áudio usando a IA da OpenAI (Whisper)
        texto = transcrever_audio(arquivo_audio)
        
        # Mostrar um trecho da transcrição para validar
        print(f"\n[Resumo da Transcrição]: {texto[:150]}...\n")
        
        # Passo 3: Gerar Títulos virais usando o LLM (Llama 3)
        titulos_sugeridos = gerar_titulos(texto)
        
        print("\n===========================")
        print("🔥 TÍTULOS SUGERIDOS 🔥")
        print("===========================\n")
        print(titulos_sugeridos)
        
    except Exception as e:
        print(f"\n[!] Ocorreu um erro durante a execução: {e}")
    finally:
        # Passo 4: Limpeza do arquivo de áudio temporário do PC
        if os.path.exists("audio_baixado.mp3"):
            os.remove("audio_baixado.mp3")
            print("\n[*] Arquivo de áudio temporário removido.")
