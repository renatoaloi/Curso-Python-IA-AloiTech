import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from rich.console import Console
from config import CHROME_PROFILE_PATH

console = Console()

class WhatsAppBot:
    def __init__(self, target_name):
        self.target_name = target_name
        self.driver = self._init_driver()
        self.wait = WebDriverWait(self.driver, 20)

    def _init_driver(self):
        chrome_options = Options()
        # Salva a sessão para evitar QR Code todas as vezes
        chrome_options.add_argument(f"user-data-dir={CHROME_PROFILE_PATH}")
        # Melhora compatibilidade com Windows e evita detecção básica
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1200,800")
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver

    def open_whatsapp(self):
        self.driver.get("https://web.whatsapp.com")
        console.print("[bold cyan]Aguardando o carregamento do WhatsApp Web...[/bold cyan]")
        console.print("[yellow]Dica: Se o QR Code aparecer, escaneie-o. Se já estiver logado, apenas aguarde.[/yellow]")
        
        # Lista de possíveis seletores para identificar que a página principal carregou
        selectors = [
            '//div[@contenteditable="true"][@data-tab="3"]',
            '//div[@title="Pesquisar ou começar uma nova conversa"]',
            '//button[@aria-label="Nova conversa"]',
            '//div[@data-testid="chat-list-search"]'
        ]
        
        start_time = time.time()
        while time.time() - start_time < 120:
            for xpath in selectors:
                try:
                    element = self.driver.find_elements(By.XPATH, xpath)
                    if element:
                        console.print(f"[bold green]Conexão estabelecida! (Elemento encontrado via: {xpath})[/bold green]")
                        time.sleep(2) # Pausa para estabilização
                        return
                except:
                    continue
            time.sleep(2)
        
        raise Exception("Não foi possível detectar o carregamento do WhatsApp Web após 120 segundos.")

    def find_contact(self):
        console.print(f"[bold blue]🔍 Buscando contato: {self.target_name}[/bold blue]")
        
        # Seletores baseados na descoberta (focando em <input>)
        search_selectors = [
            '//input[@data-tab="3"]',
            '//input[@aria-label="Pesquisar ou começar uma nova conversa"]',
            '//div[@contenteditable="true"][@data-tab="3"]',
            '//div[@title="Pesquisar ou começar uma nova conversa"]',
            '//label/div/div/div[@contenteditable="true"]',
            'input[role="textbox"]'
        ]
        
        search_box = None
        for selector in search_selectors:
            try:
                if "//" in selector:
                    search_box = self.driver.find_element(By.XPATH, selector)
                else:
                    search_box = self.driver.find_element(By.CSS_SELECTOR, selector)
                
                if search_box.is_displayed():
                    console.print(f"[green]Barra de pesquisa identificada! (via: {selector})[/green]")
                    break
            except:
                continue
            
        if not search_box:
            raise Exception("Não consegui encontrar a caixa de pesquisa. Por favor, clique nela manualmente.")

        search_box.click()
        time.sleep(0.5)
        search_box.send_keys(Keys.CONTROL + "a")
        search_box.send_keys(Keys.BACKSPACE)
        
        for char in self.target_name:
            search_box.send_keys(char)
            time.sleep(0.1)
            
        time.sleep(2)
        search_box.send_keys(Keys.ENTER)
        console.print("[green]Chat aberto![/green]")
        time.sleep(1)

    def send_message(self, message):
        # Tenta encontrar o campo de texto do chat usando padrões similares ao da busca
        input_selectors = [
            '//footer//div[@contenteditable="true"][@role="textbox"]',
            '//footer//div[@title="Digite uma mensagem"]',
            '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]',
            '//div[@data-tab="10"]',
            'footer input[role="textbox"]' # Fallback caso seja input também
        ]
        
        chat_box = None
        for xpath in input_selectors:
            try:
                if xpath.startswith('//') or xpath.startswith('/*'):
                    chat_box = self.driver.find_element(By.XPATH, xpath)
                else:
                    chat_box = self.driver.find_element(By.CSS_SELECTOR, xpath)
                
                if chat_box: 
                    console.print(f"[green]Campo de mensagem encontrado! (via: {xpath})[/green]")
                    break
            except:
                continue

        if not chat_box:
            raise Exception("Não encontrei o campo de digitação no chat. Tente clicar no campo de texto para ver se o bot assume.")

        # Digita a mensagem
        for char in message:
            chat_box.send_keys(char)
        
        time.sleep(0.5)
        chat_box.send_keys(Keys.ENTER)
        console.print(f"[bold green]✔️ Mensagem enviada para {self.target_name}[/bold green]")

    def get_chat_history(self, limit=5):
        """
        Lê as últimas mensagens do chat aberto.
        """
        # Seletor genérico para os blocos de mensagem no WhatsApp Web novo
        messages = self.driver.find_elements(By.CLASS_NAME, "message-in")
        results = []
        for msg in messages[-limit:]:
            try:
                # Tenta extrair o texto limpo da bolha de conversa
                text = msg.find_element(By.CLASS_NAME, "copyable-text").text
                results.append(text)
            except:
                continue
        return "\n".join(results)

    def close(self):
        self.driver.quit()
