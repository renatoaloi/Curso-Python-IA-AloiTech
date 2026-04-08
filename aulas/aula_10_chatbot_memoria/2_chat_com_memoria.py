import ollama

def chat():
    # Lista que armazenará o contexto da conversa (Memória)
    historico = []
    
    print("--- Chatbot com Memória Ativada ---")
    
    while True:
        pergunta = input("\nVocê: ")
        
        if pergunta.lower() in ['sair', 'exit', 'quit']:
            break
            
        # Adiciona a pergunta do usuário ao histórico
        historico.append({'role': 'user', 'content': pergunta})
        
        try:
            # Enviamos TODO o histórico para o modelo a cada nova mensagem
            resposta = ollama.chat(model='llama3', messages=historico)
            
            # Adiciona a resposta da IA ao histórico para ela lembrar do que disse
            conteudo_resposta = resposta['message']['content']
            historico.append({'role': 'assistant', 'content': conteudo_resposta})
            
            print(f"IA: {conteudo_resposta}")
        except Exception as e:
            print(f"Erro na comunicação com o Ollama: {e}")

if __name__ == "__main__":
    chat()
