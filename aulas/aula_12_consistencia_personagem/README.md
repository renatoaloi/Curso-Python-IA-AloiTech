# Aula 12 - Consistência de Personagem (Identity Lock)

Nesta aula, aprendemos a manter o rosto de um personagem fixo em diferentes cenas e estilos usando as ferramentas **PuLID** e **IP-Adapter** dentro do ComfyUI.

## Instalando o Manager

Abra o terminal na pasta `ComfyUI/custom_nodes` e execute:

```bash
git clone https://github.com/ltdrdata/ComfyUI-Manager.git
```

## Novos Pacotes Python (InsightFace)

O PuLID depende da biblioteca `insightface`. No terminal, dentro da pasta do ComfyUI e com seu **venv ativado**, rode:

```bash
# 1. Criar o ambiente virtual
python -m venv venv

# 2. Ativar o ambiente virtual no Windows
.\venv\Scripts\activate

# (Ou no Linux/macOS)
source venv/bin/activate

# 3. Instalar as bibliotecas requeridas
pip install insightface
```

## Onde baixar e colocar os modelos (Hugging Face)

Os modelos não vêm com o ComfyUI, você precisa baixar os arquivos (geralmente `.safetensors` ou `.pt`) nos links abaixo e colar nas pastas corretas.

- **Eva CLIP:** Baixe o arquivo `EVA02_CLIP_L_336_psz14_s6B.pt` ([Link Oficial no Hugging Face](https://huggingface.co/QuanSun/EVA-CLIP/tree/main)) e coloque em `models/clip_vision/` (usado apenas pelo PuLID).
- **PuLID Model (Formato IP-Adapter):** O nó oficial do ComfyUI requer uma versão específica do modelo formatada como IP-Adapter. Baixe o arquivo **`ip-adapter_pulid_sdxl_fp16.safetensors`** ([Link Oficial no Hugging Face do Huchenlei](https://huggingface.co/huchenlei/ipadapter_pulid/tree/main)) e coloque na pasta `models/pulid/`.
- **IP-Adapter Models & Vision:** Para o estilo funcionar, você precisa de DOIS arquivos:
  1. O modelo IP-Adapter base SDXL (ex: `ip-adapter-plus_sdxl_vit-h.safetensors`) salvo em `models/ipadapter/`.
  2. O interpretador de visão **`CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors`** (renomeie o `model.safetensors` do [Hugging Face h94](https://huggingface.co/h94/IP-Adapter/tree/main/models/image_encoder)) e salve na pasta `models/clip_vision/` ao lado do Eva CLIP. O IP-Adapter não funciona sem ele!

Reinicie o ComfyUI. Agora você verá o botão **"Manager"** no menu lateral.

## Conteúdo Bônus - O que instalar?

1. No Manager, procure por **"Auxiliary"** e instale o **ComfyUI-ControlnetAux** (ID 1324).
2. No Manager, procure também por **"DWPose"** e instale o **ComfyUI-DWPose** (ou **ComfyUI_DWPoseDeluxe**). Ele é o nó especializado para capturar a pose com precisão.
3. **MUITO IMPORTANTE:** Após a instalação, você precisa fechar o terminal (a janela preta) do ComfyUI e abrir de novo. Apenas dar F5 no navegador não funciona para novos nós.

## Download do Modelo de Controle (Mandatório):

Além dos nós, você precisa baixar o "cérebro" do OpenPose para SDXL:

| Arquivo                               | Pasta Destino        | Link                                                                                                                     |
| ------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `diffusion_pytorch_model.safetensors` | `models/controlnet/` | [Hugging Face](https://huggingface.co/xinsir/controlnet-openpose-sdxl-1.0/blob/main/diffusion_pytorch_model.safetensors) |

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

_Curso PythonIA do Zero - Professor Renato Aloi_
