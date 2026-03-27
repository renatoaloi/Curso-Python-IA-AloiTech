import yt_dlp
import whisper
import ollama
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
    modelo = whisper.load_model("base")
    resultado = modelo.transcribe(caminho_audio, fp16=False)
    print("[+] Transcrição concluída. Texto extraído com sucesso.")
    return resultado["text"]

def gerar_titulos(texto_transcrito):
    print("[*] Conectando com a IA para gerar títulos mágicos...")
    prompt = f"Baseado no seguinte texto de um vídeo, crie 3 opções de títulos virais e chamativos para o YouTube. Retorne apenas os 3 títulos numerados.\n\nTexto: {texto_transcrito}"
    resposta = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
    return resposta['message']['content']

def gerar_descricao(texto_transcrito):
    print("[*] Criando descrição otimizada para SEO...")
    prompt = f"Crie uma descrição de 3 parágrafos para o YouTube baseada no seguinte texto. A descrição deve ser envolvente e usar palavras-chave relevantes.\n\nTexto: {texto_transcrito}"
    resposta = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
    return resposta['message']['content']

def gerar_tags(texto_transcrito):
    print("[*] Extraindo as melhores tags...")
    prompt = f"Extraia as 15 melhores tags (palavras-chave curtas) para um vídeo do YouTube sobre esse assunto. Retorne APENAS as tags separadas por vírgula e sem NENHUM outro texto ou formatação. \n\nTexto: {texto_transcrito}"
    resposta = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
    return resposta['message']['content']

def gerar_prompts_thumbnail(texto_transcrito):
    print("[*] Imaginando thumbnails virais...")
    prompt = f"Baseado no texto a seguir, sugira 3 ideias visuais (prompts) detalhadas para criar a thumbnail (capa) do vídeo do YouTube. Descreva o que deve aparecer na imagem, as cores e a emoção.\n\nTexto: {texto_transcrito}"
    resposta = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
    return resposta['message']['content']

def salvar_resultado(titulos, descricao, tags, thumbnails):
    with open("pacote_youtube.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("🔥 TÍTULOS SUGERIDOS 🔥\n")
        arquivo.write(titulos + "\n\n")
        
        arquivo.write("📝 DESCRIÇÃO DO VÍDEO (SEO) 📝\n")
        arquivo.write(descricao + "\n\n")
        
        arquivo.write("🏷️ TAGS YOUTUBE 🏷️\n")
        arquivo.write(tags + "\n\n")
        
        arquivo.write("🖼️ IDEIAS PARA THUMBNAIL (PROMPTS) 🖼️\n")
        arquivo.write(thumbnails + "\n")
        
    print("[+] Arquivo 'pacote_youtube.txt' gerado com sucesso!")

if __name__ == "__main__":
    print("====================================")
    print("🚀 ASSISTENTE DE YOUTUBE COM IA")
    print("====================================\n")
    
    url_video = input("Cole a URL do vídeo do YouTube (ex: um Short curto): ")
    
    try:
        arquivo_audio = baixar_audio(url_video)
        texto = transcrever_audio(arquivo_audio)
        
        print(f"\n[Resumo da Transcrição]: {texto[:150]}...\n")
        
        titulos = gerar_titulos(texto)
        descricao = gerar_descricao(texto)
        tags = gerar_tags(texto)
        thumbnails = gerar_prompts_thumbnail(texto)
        
        salvar_resultado(titulos, descricao, tags, thumbnails)
        
    except Exception as e:
        print(f"\n[!] Ocorreu um erro durante a execução: {e}")
    finally:
        if os.path.exists("audio_baixado.mp3"):
            os.remove("audio_baixado.mp3")
            print("[*] Arquivo de áudio temporário removido.")
