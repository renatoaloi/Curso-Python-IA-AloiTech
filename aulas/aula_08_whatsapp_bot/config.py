import os

# Nome do contato ou grupo para o teste
FRIEND_NAME = "Nome do Contato"

# Configurações da API (Ollama usa a porta 11434 por padrão)
LLM_API_URL = "http://localhost:11434/api/generate"

# Configurações do Selenium
# O perfil do Chrome será salvo nesta pasta local para não precisar de QR Code toda vez
CHROME_PROFILE_PATH = os.path.abspath("chrome_profile")

# Mensagens padrão
INITIAL_GREETING = (
    f"Opa {FRIEND_NAME.split()[0]}, isso é um teste do meu novo script do whatsapp, "
    "pode responder qualquer coisa aqui pra eu rodar a IA?"
)
