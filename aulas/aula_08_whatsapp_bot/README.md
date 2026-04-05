# Aula 08: WhatsApp Bot com IA Local (Ollama + Python)

Nesta aula, aprendemos a construir um assistente inteligente para o WhatsApp do absoluto zero. Diferente de bots simples que apenas respondem comandos fixos, este projeto utiliza **Inteligência Artificial (LLM)** rodando localmente no seu computador através do **Ollama** para ler o contexto das conversas e sugerir respostas naturais e úteis.

## 🎯 Objetivos da Aula

1.  **Automação com Selenium**: Entender como automatizar tarefas em navegadores, especificamente no WhatsApp Web, lidando com seletores dinâmicos e carregamento de página.
2.  **Integração com IA Local**: Aprender a conectar scripts Python com o Ollama, permitindo o uso de modelos como **Mistral** ou **Llama 3** sem custos de API.
3.  **Gestão de Perfis de Navegação**: Configurar o Chrome para persistir sessões, evitando a necessidade de ler o QR Code a cada execução.
4.  **Interface de Terminal Rica**: Utilizar a biblioteca `Rich` para criar painéis, cores e prompts amigáveis no terminal.
5.  **Fluxo Humano-na-Alça (HITL)**: Implementar uma lógica onde a IA sugere respostas, mas o usuário tem o controle final antes do envio.

## 🧰 Ferramentas Utilizadas

-   **Python 3.10+**: Linguagem base do projeto.
-   **Selenium**: Ferramenta de automação de navegadores.
-   **WebDriver Manager**: Facilita a gestão do driver do Chrome.
-   **Ollama**: Plataforma para rodar modelos de IA localmente.
-   **Rich**: Biblioteca para embelezar a saída no terminal.
-   **Requests**: Para realizar chamadas HTTP para a API local do Ollama.

## 📂 Arquivos do Projeto

-   `config.py`: Centraliza todas as configurações como nome do contato, URLs e caminhos de pastas.
-   `whatsapp_client.py`: Contém a classe `WhatsAppBot` que encapsula toda a lógica do Selenium (abrir chat, buscar contato, ler histórico e enviar mensagens).
-   `llm_service.py`: Responsável pela comunicação com o Ollama, enviando o histórico da conversa e recebendo as sugestões formatadas em JSON.
-   `main.py`: O "cérebro" do projeto que orquestra os outros módulos em um loop contínuo de interação.

## 🚀 Como Executar

### 1. Pré-requisitos
Certifique-se de ter o Chrome instalado e o Ollama rodando com o modelo Mistral:
```powershell
ollama run mistral
```

### 2. Configurar o Ambiente
Crie e ative seu ambiente virtual, depois instale as dependências:
```powershell
python -m venv venv
.\venv\Scripts\activate  # No Windows
pip install selenium webdriver-manager requests rich
```

### 3. Ajustar Configurações
Abra o arquivo `config.py` e altere a variável `FRIEND_NAME` para o nome exato do contato ou grupo que você deseja testar.

### 4. Rodar o Bot
```powershell
python main.py
```

## ⚠️ Avisos de Segurança

-   **Uso Responsável**: Automatizar o WhatsApp pode violar os termos de serviço se usado para spam. Use este script apenas para fins educacionais e produtividade pessoal.
-   **QR Code**: Na primeira execução, você precisará ler o QR Code. Graças ao `CHROME_PROFILE_PATH` no `config.py`, seu login será salvo na pasta `chrome_profile` para as próximas vezes.

---
*Ass: Equipe do Curso PythonIA do Zero*
