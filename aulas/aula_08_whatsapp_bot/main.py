import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from whatsapp_client import WhatsAppBot
from llm_service import generate_response_options
from config import FRIEND_NAME, INITIAL_GREETING

console = Console()

def main():
    console.print(Panel.fit("🤖 Bot de Atendimento WhatsApp (MVP)", style="bold blue"))
    
    bot = WhatsAppBot(FRIEND_NAME)
    
    try:
        bot.open_whatsapp()
        
        # Inicia a conversa
        bot.find_contact()
        bot.send_message(INITIAL_GREETING)
        
        while True:
            console.print("\n[bold yellow]Menu de Comando:[/bold yellow]")
            console.print("1. [green]Ler Histórico e Gerar Sugestões[/green]")
            console.print("2. [red]Encerrar[/red]")
            
            choice = Prompt.ask("Escolha uma opção", choices=["1", "2"], default="1")
            
            if choice == "2":
                break
            
            qtde_msg = Prompt.ask("Quantas mensagens recentes ler para análise?", default="5")

            # Lê o chat
            console.print("Lendo as mensagens recentes...")
            history = bot.get_chat_history(int(qtde_msg))
            if not history:
                console.print("[red]Erro: Não foi possível ler as mensagens.[/red]")
                continue
                
            console.print(Panel(f"[bold green]Histórico Lido:[/bold green]\n{history}"))
            
            # Gera sugestões
            with console.status("IA Pensando nas sugestões..."):
                result = generate_response_options(history)
            
            if "error" in result:
                console.print(f"[red]{result['error']}[/red]")
                continue
                
            console.print(f"[bold magenta]Análise de Humor:[/bold magenta] {result.get('analise_humor', 'N/A')}")
            
            # Menu de Sugestões
            sugestoes = result.get('sugestoes', [])
            for i, s in enumerate(sugestoes, 1):
                console.print(f"{i}. {s}")
            console.print("4. [yellow]Escrever Mensagem Customizada[/yellow]")
            console.print("5. [blue]Voltar[/blue]")
            
            sub_choice = Prompt.ask("O que deseja fazer?", choices=["1", "2", "3", "4", "5"], default="1")
            
            if sub_choice == "5":
                continue
                
            msg_to_send = ""
            if sub_choice == "4":
                msg_to_send = Prompt.ask("Sua mensagem")
            elif sub_choice in ["1", "2", "3"]:
                msg_to_send = sugestoes[int(sub_choice)-1]
            
            if msg_to_send:
                bot.send_message(msg_to_send)
                console.print(f"[bold green]Mensagem enviada com sucesso:[/bold green] {msg_to_send}")

    except Exception as e:
        console.print(f"[bold red]Erro fatal na orquestração:[/bold red] {str(e)}")
    finally:
        bot.close()
        console.print("[bold red]Bot finalizado.[/bold red]")

if __name__ == "__main__":
    main()