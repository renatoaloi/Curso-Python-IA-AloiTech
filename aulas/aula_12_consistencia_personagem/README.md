# Aula 12 - Consistência de Personagem (Identity Lock)

Nesta aula, aprendemos a manter o rosto de um personagem fixo em diferentes cenas e estilos usando as ferramentas **PuLID** e **IP-Adapter** dentro do ComfyUI.

## 🎯 O que foi visto:
1. **PuLID**: Técnica avançada para "travar" a identidade facial a partir de uma foto de referência.
2. **IP-Adapter Plus**: Como controlar o estilo, vestimenta e composição sem afetar o rosto.
3. **Fluxo Narrativo**: Criação de uma sequência de imagens (Storyboarding) com o mesmo personagem.
4. **Otimização de VRAM**: Uso do **VAE Decode (Tiled)** para rodar modelos pesados em GPUs de 8GB.

## 🛠️ Requisitos Novos:
- **ComfyUI Manager** (para instalar os nós customizados).
- Nódulos: `ComfyUI_PuLID_Flux` e `ComfyUI_IPAdapter_Plus`.
- Bibliotecas: `pip install insightface`.

## 📂 Arquivos desta Aula:
- `prompts.txt`: Lista de prompts usados nos exemplos do mago.
- `exemplo_comfy_ui.json`: Arquivo base (SDXL padrão) para começar o fluxo da aula.

---
*Curso PythonIA do Zero - Professor Renato Aloi*
