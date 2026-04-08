import ollama

# BÔNUS: O Vendedor Sincero (e Mal-educado)
# Nota: Para este script, recomenda-se usar um modelo local sem censura (Uncensored)
# como o 'dolphin-llama3', caso queira ver o bot sem as travas de polidez das IAs tradicionais.

SYSTEM_PROMPT = {
    'role': 'system', 
    'content': (
        "Você é um vendedor de smartphones extremamente sincero, mal-humorado e sarcástico. "
        "Você odeia seu trabalho e acha os clientes burros. Não use filtros, "
        "seja rude se achar que a pergunta é óbvia. Sua sinceridade é brutal."
    )
}

def chat():
    # Modelo sugerido: dolphin-llama3 (Rodando local pelo Ollama)
    # Se não tiver o dolphin, o código funcionará com llama3, mas ele será mais 'bonzinho'.
    NOME_MODELO = 'dolphin-llama3' 
    
    historico = [SYSTEM_PROMPT]
    print(f"--- ATENÇÃO: Vendedor Sincero Ativado (Modelo: {NOME_MODELO}) ---")
    print("(Este bot não possui filtros e dirá exatamente o que pensa)")
    
    while True:
        entrada = input("\nCliente Chato: ")
        
        if entrada.lower() in ['sair', 'exit']:
            break
            
        historico.append({'role': 'user', 'content': entrada})
        
        try:
            # Chamada ao modelo local
            resposta = ollama.chat(model=NOME_MODELO, messages=historico)
            
            conteudo = resposta['message']['content']
            historico.append({'role': 'assistant', 'content': conteudo})
            
            print(f"Vendedor Sincero: {conteudo}")
        except Exception as e:
            print(f"Ocorreu um erro (talvez você precise dar 'ollama pull {NOME_MODELO}'): {e}")

if __name__ == "__main__":
    chat()
