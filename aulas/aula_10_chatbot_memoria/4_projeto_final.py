import ollama

SYSTEM_PROMPT = {
    'role': 'system', 
    'content': "Você é um vendedor especialista em smartphones. Seja prestativo e persuasivo."
}

def chat():
    historico = [SYSTEM_PROMPT]
    print("--- Chatbot Pro (Comandos: /limpar, /historico, sair) ---")
    
    while True:
        entrada = input("\nVocê: ")
        
        if entrada.lower() in ['sair', 'exit', 'quit']:
            break
            
        # Comando para limpar a memória
        if entrada.lower() == '/limpar':
            historico = [SYSTEM_PROMPT]
            print("-> Memória limpa com sucesso!")
            continue
            
        # Comando para listar o histórico bruto
        if entrada.lower() == '/historico':
            print("\n--- Histórico Atual ---")
            for i, msg in enumerate(historico):
                # Mostra apenas os primeiros 50 caracteres para não poluir
                resumo = (msg['content'][:50] + '..') if len(msg['content']) > 50 else msg['content']
                print(f"{i}. [{msg['role'].upper()}]: {resumo}")
            continue
        
        # Adiciona a entrada do usuário ao histórico
        historico.append({'role': 'user', 'content': entrada})
        
        try:
            # Chamada ao modelo
            resposta = ollama.chat(model='llama3', messages=historico)
            
            conteudo = resposta['message']['content']
            historico.append({'role': 'assistant', 'content': conteudo})
            
            print(f"IA: {conteudo}")
        except Exception as e:
            print(f"Erro na comunicação: {e}")

if __name__ == "__main__":
    chat()
