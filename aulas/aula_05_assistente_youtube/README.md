# Aula 05: Assistente Completo de YouTube (Descrições, Tags e Thumbnails)

Nesta aula, aprofundamos nosso uso de Inteligência Artificial Local. Partindo do código base da Aula 04, evoluímos o gerador de títulos para um assistente completo que emite Títulos, Descrições otimizadas para SEO, Tags formatadas para o YouTube e Prompts para geração de Thumbnails, gravando um "pacote" pronto em um arquivo `.txt`.

## 🎯 Objetivos da Aula
1. Reaproveitar as bibliotecas `yt-dlp` e Whisper para baixar e transcrever vídeos.
2. Explorar técnicas iniciais de Engenharia de Prompt, melhorando o envio de instruções para a IA.
3. Obter uma descrição envolvente e engajadora feita pelo modelo Llama 3 (via Ollama).
4. Gerar 15 palavras-chave exatas separadas por vírgula para SEO de YouTube.
5. Obter 3 ideias criativas (prompts) de Thumbnails para geração de imagens.
6. Aprender a gravar todo o resultado (output) em um arquivo `.txt` automaticamente usando a linguagem Python.

## 🧰 Ferramentas Utilizadas
- **Python 3.x**
- **yt-dlp**: Para extrair áudio diretamente da URL.
- **FFmpeg**: Necessário para manipular o `.mp3`.
- **Whisper (OpenAI)**: IA local que transforma áudio em texto (reconhecimento de fala).
- **Ollama**: Rodando o modelo `llama3` localmente para analisar nosso texto e criar SEO.

## 📂 Arquivos do Projeto
- `assistente_youtube.py`: O script principal escrito nesta aula com os novos prompts.
- `pacote_youtube.txt`: Arquivo texto gerado pelo Python em tempo real de execução, contendo os Títulos, Descrições, Tags e Prompts de Thumbnails consolidados.

## 🚀 Como Executar
1. Certifique-se de ter o Python, FFmpeg e o Ollama instalados em sua máquina.
2. Inicie o seu ambiente virtual (`venv`).
3. No terminal, instale as dependências se já não as tiver com: `pip install yt-dlp openai-whisper ollama`.
4. Garanta que você já tenha rodado o modelo no Ollama (`ollama run llama3`).
5. Execute o script com o comando `python assistente_youtube.py`.
6. Cole a URL de um vídeo do YouTube.
7. Confira a pasta do projeto após a conclusão para visualizar o pacote no seu novo arquivo `pacote_youtube.txt`!
