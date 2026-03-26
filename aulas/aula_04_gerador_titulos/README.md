# Aula 04: Criador de Títulos para YouTube com IA

Nesta aula, amarramos os conhecimentos adquiridos criando nosso primeiro projeto prático: um robô em Python que baixa o áudio de um vídeo do YouTube, faz a transcrição com Whisper, e utiliza a inteligência artificial local com um LLM (ex: Llama 3 via Ollama) para gerar opções chamativas e virais de títulos para os seus vídeos!

## 🎯 Objetivos da Aula
1. Aprender a baixar áudio de vídeos do YouTube usando a biblioteca `yt-dlp`.
2. Integrar a IA Whisper para transcrever os vídeos baixados de forma eficiente.
3. Conectar a transcrição a um modelo de linguagem (LLM) que analisa o roteiro.
4. Gerar imediatamente 3 opções criativas e otimizadas de títulos para testes A/B.

## 🧰 Ferramentas Utilizadas
- **Python 3.x**
- **yt-dlp**: Para extrair áudio diretamente da URL do YouTube.
- **FFmpeg**: Necessário para o `yt-dlp` e Whisper trabalharem com os arquivos `.mp3`.
- **Whisper (OpenAI)**: IA local que transforma áudio em texto (reconhecimento de fala).
- **Ollama**: Ferramenta em background rodando o modelo `llama3` localmente e enviando respostas para o Python.

## 📂 Arquivos do Projeto
- `gerador_titulos.py`: O script principal escrito e explicado em aula, que executa toda a orquestração do download, transcrição e geração de ideias.

## 🚀 Como Executar
1. Certifique-se de ter o Python, FFmpeg e o Ollama instalados em sua máquina.
2. No terminal, caso seja seu primeiro acesso, baixe o modelo da IA com o comando `ollama run llama3`.
3. Inicie seu ambiente virtual (ex: `venv`).
4. Instale as dependências executando: `pip install yt-dlp openai-whisper ollama`.
5. Execute o script com o comando `python gerador_titulos.py`.
6. Cole a URL de um vídeo curto do YouTube (como um Short) e aguarde a mágica!
