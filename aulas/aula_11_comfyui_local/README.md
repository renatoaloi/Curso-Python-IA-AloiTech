# Aula 11 - ComfyUI: Geração de Imagens Profissional e Local

Bem-vindo à Aula 11 do curso **PythonIA do Zero**! Nesta aula, vamos instalar e configurar o **ComfyUI**, a interface baseada em nódulos mais poderosa para geração de imagens com IA.

Diferente das aulas anteriores, esta aula é 100% sobre configuração de ambiente e criação de fluxos de trabalho (workflows) visuais. Não teremos arquivos `.py` para rodar, masterizaremos o uso da ferramenta e a organização dos modelos.

---

## 🛠️ 1. Instalação Passo a Passo

### 1.0 Instalar o Git
Se você ainda não tem o Git instalado no seu computador, baixe e instale agora:
- **Link:** [https://git-scm.com/downloads](https://git-scm.com/downloads)
- **Instrução:** Clique em "Download for Windows", instale com as opções padrão.
- **IMPORTANTE:** Após a instalação, feche e abra novamente o seu terminal de comando para que o Git seja reconhecido!

Siga os comandos abaixo no seu terminal (PowerShell ou Bash) dentro da sua pasta de projetos.

### 1.1 Clonar o Projeto e Criar Ambiente
```bash
# Clone o repositório oficial
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI

# Crie e ative o ambiente virtual
python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```

### 1.2 Instalação por Hardware (ESCOLHA A SUA ROTA)

#### **🚀 Rota A: NVIDIA (Placas RTX/GTX)**
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
```

#### **🏎️ Rota B: AMD Radeon (Rota 1 - DirectML)**
*Ideal para placas RX 6000/7000 de entrada ou notebooks.*
```bash
pip install torch-directml
pip install -r requirements.txt
```
> **Comando para abrir:** `python main.py --directml --force-fp32 --lowvram`

#### **🔥 Rota C: AMD Radeon (Rota 2 - ROCm 2026)**
*Recomendado para RX 7600 ou superior. Alta performance e economia de VRAM.*
*Requisito: Python 3.12.7.*
```bash
# 0. Instalar requisitos e desinstalar versões incompatíves
pip install -r requirements.txt
pip uninstall torch torchaudio torchvideo

# 1. SDK e Bibliotecas
pip install --no-cache-dir https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/rocm_sdk_core-7.2.1-py3-none-win_amd64.whl https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/rocm_sdk_devel-7.2.1-py3-none-win_amd64.whl https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/rocm_sdk_libraries_custom-7.2.1-py3-none-win_amd64.whl https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/rocm-7.2.1.tar.gz

# 2. PyTorch ROCm
pip install --no-cache-dir https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/torch-2.9.1%2Brocm7.2.1-cp312-cp312-win_amd64.whl https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/torchaudio-2.9.1%2Brocm7.2.1-cp312-cp312-win_amd64.whl https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/torchvision-0.24.1%2Brocm7.2.1-cp312-cp312-win_amd64.whl
```

> **Comando para abrir:** `python main.py`

#### **🐢 Rota D: Apenas CPU**
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt
```
> **Comando para abrir:** `python main.py --cpu`

---

## 📂 2. Download e Organização de Modelos

Para que o ComfyUI funcione, você precisa baixar os modelos abaixo e colocá-los nas pastas corretas dentro de `ComfyUI/models/`.

### 📥 Links para Download:
- **Checkpoint Juggernaut XL v9:** [HuggingFace - Download](https://huggingface.co/RunDiffusion/Juggernaut-XL-v9/blob/main/Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors)
- **Modelo SDXL VAE:** [HuggingFace - Download](https://huggingface.co/stabilityai/sdxl-vae/resolve/main/sdxl_vae.safetensors?download=true)
- **LoRA Detail Tweaker XL:** [CivitAI - Download](https://civitai.com/api/download/models/135867?type=Model&format=SafeTensor)
- **Upscaler 4x-UltraSharp:** [HuggingFace - Download](https://huggingface.co/lokCX/4x-Ultrasharp/resolve/main/4x-UltraSharp.pth?download=true)
- **Suporte AMD ROCm Windows:** [Site Oficial AMD](https://www.amd.com/pt/products/software/rocm.html)

### Onde colocar os arquivos:
1.  **Checkpoint (O Cérebro):** `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors`
    - Destino: `models/checkpoints/`
2.  **VAE (O Corretor de Cores):** `sdxl_vae.safetensors`
    - Destino: `models/vae/`
3.  **LoRA (O Detalhador):** `add-detail-xl.safetensors`
    - Destino: `models/loras/`
4.  **Upscaler (Super Resolução):** `4x-UltraSharp.pth`
    - Destino: `models/upscale_models/`

---

## 💡 Dicas de Ouro (Troubleshooting)

- **F5 / Refresh:** Se você colocou um modelo na pasta e ele não aparece no ComfyUI, dê um **F5** no seu navegador ou clique no botão **Refresh** lateral.
- **Erro de Memória (Out of Memory):** Se sua placa der erro no Upscaling, substitua o nódulo `VAE Decode` pelo **`VAE Decode (Tiled)`**. Ele fatia o trabalho e economiza muita memória!
- **Cores Cinzas:** Se sua imagem sair sem cor, verifique se você conectou o nódulo **VAE Loader** corretamente no **VAE Decode**.

---

## 🚀 Desafio da Aula

Gere uma imagem usando o seu próprio rascunho de papel como base através do fluxo de **Img2Img** que vimos na aula! Poste o antes e o depois no grupo de alunos!

---
*Professor Renato Aloi - Curso PythonIA do Zero*
