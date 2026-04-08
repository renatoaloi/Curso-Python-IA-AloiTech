import ollama

def chat():
    print("--- Bem-vindo ao Chatbot IA (Digite 'sair' para encerrar) ---")
    
    while True:
        pergunta = input("\nVocê: ")
        
        if pergunta.lower() in ['sair', 'exit', 'quit']:
            break
            
        # Chamada simples ao modelo (sem memória entre as mensagens)
        try:
            resposta = ollama.chat(model='llama3', messages=[
                {'role': 'user', 'content': pergunta}
            ])
            
            print(f"IA: {resposta['message']['content']}")
        except Exception as e:
            print(f"Erro ao conectar com Ollama: {e}")

if __name__ == "__main__":
    chat()
