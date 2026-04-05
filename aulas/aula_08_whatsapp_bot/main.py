import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from whatsapp_client import WhatsAppBot
from llm_service import generate_response_options
from config import FRIEND_NAME, INITIAL_GREETING

console = Console()

def main():
    bot = WhatsAppBot(FRIEND_NAME)
    
    try:
        console.print(Panel("[bold green]Iniciando conexão com o WhatsApp...[/bold green]", title="WhatsAloi", border_style="green"))
        bot.open_whatsapp()
        bot.find_contact()
        
        # Envia mensagem inicial se for o primeiro acesso
        console.print(Panel(INITIAL_GREETING, title="Mensagem Inicial", border_style="cyan"))
        bot.send_message(INITIAL_GREETING)
        
        console.print(Panel("[bold yellow]Aguardando resposta...[/bold yellow]", title="Status", border_style="yellow"))
        
        while True:
            # Espera um tempo razoável antes de verificar novamente
            time.sleep(5)
            
            # Lê as últimas mensagens (limitado a 10 para não poluir)
            history = bot.get_chat_history(limit=10)
            
            # Gera sugestões baseadas no histórico
            ai_response = generate_response_options(history)
            
            if "error" in ai_response:
                console.print(f"[red]Erro: {ai_response['error']}[/red]")
                continue
                
            suggestions = ai_response.get("sugestoes", [])
            
            # Exibe as sugestões de forma organizada
            console.print(Panel("\n".join(suggestions), title="Sugestões da IA", border_style="green"))
            
            # Pergunta ao usuário o que fazer
            user_input = Prompt.ask(
                "\n[bold yellow]Sua resposta (ou digite para customizar)[/bold yellow]",
                default=suggestions[0] if suggestions else ""
            )
            
            # Envia a resposta escolhida/digitada
            bot.send_message(user_input)
            
    except Exception as e:
        console.print(f"[bold red]Erro crítico: {e}[/bold red]")
    finally:
        bot.close()

if __name__ == "__main__":
    main()
