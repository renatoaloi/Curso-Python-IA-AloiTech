import ollama

# Mensagem de sistema que define o comportamento (Persona)
SYSTEM_PROMPT = {
    'role': 'system', 
    'content': (
        "Você é um vendedor especialista em smartphones e tecnologia de última geração. "
        "Seu objetivo é ajudar o cliente a escolher o melhor aparelho, sendo sempre educado, "
        "conhecedor técnico e persuasivo. Tente fechar a venda oferecendo acessórios ou "
        "mencionando benefícios como garantia estendida."
    )
}

def chat():
    # Iniciamos o histórico já com a instrução do sistema (System Prompt)
    historico = [SYSTEM_PROMPT]
    
    print("--- Atendimento Especializado em Tecnologia ---")
    
    while True:
        pergunta = input("\nCliente: ")
        
        if pergunta.lower() in ['sair', 'exit', 'quit']:
            break
            
        # Adiciona a pergunta do cliente ao histórico
        historico.append({'role': 'user', 'content': pergunta})
        
        try:
            resposta = ollama.chat(model='llama3', messages=historico)
            
            conteudo_resposta = resposta['message']['content']
            historico.append({'role': 'assistant', 'content': conteudo_resposta})
            
            print(f"Vendedor: {conteudo_resposta}")
        except Exception as e:
            print(f"Erro no atendimento: {e}")

if __name__ == "__main__":
    chat()
