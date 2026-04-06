# Aula 09: Web Scraping no WhatsApp Web com Selenium

Nesta aula, aprendemos a técnica de **Web Scraping** aplicada ao WhatsApp Web. O projeto foi construído de forma incremental, partindo do básico (abrir o navegador) até a extração robusta de histórico de mensagens de múltiplos contatos.

## 🎯 Objetivos da Aula

1.  **Gestão de Perfis (Session Persistence)**: Configurar o Selenium para usar uma pasta de perfil do Chrome (`user-data-dir`), permitindo que o login no WhatsApp seja persistente e evite a leitura constante do QR Code.
2.  **Esperas Inteligentes (Implicit vs Explicit)**: Dominar o uso do `WebDriverWait` e `ExpectedConditions` para lidar com a natureza assíncrona e pesada do WhatsApp Web.
3.  **Localização Avançada com XPATH**: Aprender a construir seletores precisos para encontrar campos de busca, resultados de pesquisa e bolhas de mensagem.
4.  **Iteração de Elementos Dinâmicos**: Criar lógicas para percorrer listas de contatos retornadas por uma busca e interagir com cada uma delas programaticamente.
5.  **Extração de Conteúdo (Scraping)**: "Raspar" o texto das mensagens recebidas e exibi-las no terminal de forma estruturada.

## 🧰 Ferramentas Utilizadas

-   **Python 3.10+**: Linguagem base do projeto.
-   **Selenium**: Framework para automação de navegadores.
-   **WebDriver Manager**: Gerenciador automático do driver do Chrome (ChromeDriver).

## 📂 Arquivos da Aula

O projeto está dividido em scripts numerados para facilitar o acompanhamento da evolução:

-   `1_setup_perfil.py`: Configuração inicial do driver com perfil de usuário persistente.
-   `2_espera_waits.py`: Implementação de esperas inteligentes para aguardar o carregamento da página principal.
-   `3_busca_simples.py`: Lógica básica de clicar na busca, digitar um nome e selecionar o primeiro resultado.
-   `4_busca_robusta.py`: Seleção aprimorada que percorre a lista de resultados e valida o nome do contato antes de clicar.
-   `5_extracao_historico.py`: O projeto completo, realizando a busca e extraindo as últimas mensagens dos contatos encontrados.

## 🚀 Como Executar

### 1. Preparar o Ambiente
Crie e ative seu ambiente virtual (Venv):
```powershell
python -m venv venv
.\venv\Scripts\activate  # No Windows
```

### 2. Instalar Dependências
```powershell
pip install selenium webdriver-manager
```

### 3. Execução sugerida
Recomendamos executar os scripts na ordem numérica para entender a evolução do raciocínio:
```powershell
python 1_setup_perfil.py
# (Após testar o primeiro, prossiga para os próximos)
python 5_extracao_historico.py
```

## ⚠️ Avisos e Boas Práticas

-   **Termos de Serviço**: O uso de automação no WhatsApp deve respeitar os Termos de Serviço da plataforma. Evite disparos em massa ou comportamentos que possam ser interpretados como spam.
-   **Estrutura do DOM**: Sites como o WhatsApp Web mudam seus seletores (classes e IDs) frequentemente. Se o script parar de funcionar, pode ser necessário atualizar os XPATHs e seletores de classe.
-   **Segurança**: Nunca compartilhe sua pasta `chrome_profile`, pois ela contém sua sessão ativa do WhatsApp.

---
*Ass: Equipe do Curso PythonIA do Zero*
