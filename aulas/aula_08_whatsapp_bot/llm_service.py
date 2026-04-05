import requests
import json
from config import LLM_API_URL

def generate_response_options(chat_history):
    """
    Envia o histórico de chat para o Ollama local e gera 3 opções de resposta.
    """
    # Prompt estruturado para instruir a IA
    prompt = (
        "[INST] Analise a seguinte conversa do WhatsApp e identifique o humor do contato. "
        "Em seguida, sugira 3 opções de resposta distintas e úteis (curtas e naturais). "
        "Sua resposta final deve ser EXCLUSIVAMENTE um objeto JSON válido no formato:\n"
        "{\n"
        "  \"analise_humor\": \"...\", \n"
        "  \"sugestoes\": [\"Opção 1\", \"Opção 2\", \"Opção 3\"]\n"
        "}\n\n"
        f"Histórico:\n{chat_history} [/INST]"
    )

    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "num_predict": 256,
            "stop": ["[/INST]", "</s>"]
        }
    }

    try:
        response = requests.post(LLM_API_URL, json=payload, timeout=60)
        response.raise_for_status()
        
        # O Ollama retorna a resposta no campo "response"
        content = response.json().get("response", "{}")
        
        # Limpa possíveis blocos de código se o LLM enviar como ```json
        content = content.replace("```json", "").replace("```", "").strip()
        return json.loads(content)
    except Exception as e:
        return {
            "error": f"Erro ao comunicar com Ollama: {str(e)}",
            "sugestoes": ["Erro ao gerar sugestões", "Tente novamente", "Ignorar"]
        }
