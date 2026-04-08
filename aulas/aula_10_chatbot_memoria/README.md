# Aula 10: Chatbot com Memória e Skill de Vendas (Ollama)

Nesta aula, exploramos o funcionamento interno dos Chatbots, implementando um sistema de **memória persistente** e definindo **personas** especializadas usando modelos de IA rodando 100% localmente com o Ollama.

## 🎯 Objetivos da Aula

1.  **Loop Contínuo de Chat**: Criar uma interface simples via terminal que permite conversas ininterruptas com a IA.
2.  **Gerenciamento de Contexto (Memória)**: Entender como as IAs "lembram" das mensagens anteriores através do envio do histórico completo a cada nova iteração.
3.  **System Prompts e Personas**: Utilizar o `role: 'system'` para transformar um modelo genérico em um especialista (neste caso, um vendedor de tecnologia).
4.  **Comandos Customizados**: Implementar lógicas de controle dentro do chat, como limpar a memória (`/limpar`) ou visualizar os dados brutos (`/historico`).
5.  **Modelos Locais e Liberdade**: Demonstrar o poder de rodar IAs locais, permitindo o uso de modelos sem censura e personas mais ousadas.

## 🧰 Ferramentas Utilizadas

-   **Python 3.10+**: Linguagem base.
-   **Ollama**: Plataforma para rodar modelos de linguagem grandes (LLMs) localmente.
-   **Biblioteca Python `ollama`**: Cliente oficial para integração do Python com o servidor Ollama.
-   **Modelos Recomendados**: `llama3`, `mistral`, ou `dolphin-llama3` (para o bônus).

## 📂 Arquivos da Aula

O projeto está dividido de forma incremental para facilitar o aprendizado:

-   `1_chat_basico.py`: Estrutura inicial de loop e chamada simples à API.
-   `2_chat_com_memoria.py`: Introdução da lista de histórico para dar "memória" ao bot.
-   `3_vendedor_tech.py`: Aplicação de Persona (Vendedor Especialista) via System Prompt.
-   `4_projeto_final.py`: Versão completa com comandos de gerenciamento e tratamento de erros.
-   `5_bonus_uncensored.py`: Script bônus explorando modelos sem alinhamento e personas ácidas/sinceras.

## 🚀 Como Executar

### 1. Preparar o Ollama
Certifique-se de que o Ollama está instalado e rodando. Baixe os modelos necessários:
```bash
ollama pull llama3
ollama pull dolphin-llama3  # Para o script bônus
```

### 2. Preparar o Ambiente Python
Crie e ative seu ambiente virtual (Venv) na pasta da aula:
```powershell
python -m venv venv
.\venv\Scripts\activate  # No Windows
```

### 3. Instalar Dependências
```powershell
pip install ollama
```

### 4. Execução sugerida
Recomendamos testar os scripts na ordem numérica para acompanhar a evolução do projeto:
```powershell
python 1_chat_basico.py
# (Teste a memória, o comportamento do vendedor e os comandos finais)
python 4_projeto_final.py
```

## ⚠️ Dica de Ouro
Lembre-se que quanto maior o histórico enviado para a IA, mais processamento será exigido da sua máquina. Em aplicações de produção, costumamos usar técnicas como **Janela de Contexto** (enviar apenas as últimas X mensagens) ou **Resumo de Histórico** para não exceder o limite de memória dos modelos.

---
*Ass: Equipe do Curso PythonIA do Zero*
