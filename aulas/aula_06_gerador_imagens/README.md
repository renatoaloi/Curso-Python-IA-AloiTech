# Aula 06: Gerando Imagens Localmente com a sua Placa de Vídeo (Python + Stable Diffusion + Vulkan)

Nesta aula, mudamos um pouco o rumo! Aprendemos como usar a força bruta da sua placa de vídeo (GPU) para gerar imagens localmente usando o Stable Diffusion sem depender de créditos em plataformas online ou assinaturas. Fizemos isso através de uma ponte utilizando a biblioteca `subprocess` do Python, executando um cliente nativo (`sd.cpp`) compilado com suporte à API Vulkan, conseguindo assim alta performance em qualquer GPU!

## 🎯 Objetivos da Aula
1. Instalar o Vulkan SDK para habilitar aceleração agnóstica na placa de vídeo.
2. Instalar o Visual Studio 2022 (Desenvolvimento para Desktop com C++) para compilar no Windows.
3. Baixar, instalar e compilar o `sd.cpp` focando em aceleração Vulkan.
4. Baixar o modelo base oficial `stable-diffusion-v1-5`.
5. Integrar o gerador ao Python utilizando a biblioteca `subprocess`.
6. Criar um script interativo onde o usuário controla o prompt descritivo e a quantidade de passos (steps).

## 🧰 Ferramentas Utilizadas
- **Python 3.x**: Linguagem base para orquestrar e criar nosso gerador interativo.
- **Vulkan SDK**: Interface de hardware responsável pela aceleração gráfica ultra rápida e multiplataforma.
- **Visual Studio 2022**: Para a obtenção dos compiladores nativos de C++ exigidos no Windows.
- **sd.cpp**: Implementação puramente em C e C++ da inferência do Stable Diffusion.
- **Stable Diffusion 1.5**: Conjunto de pesos (modelo base `safetensors`) utilizado para gerar as imagens.

## 📂 Arquivos do Projeto
- `gerador_imagens.py`: Script construído na aula que usa o `subprocess` para chamar nosso executável na GPU.

*(Nota: Os arquivos binários pesados como o `sd.exe` e o `modelo_do_sd.safetensors` são obtidos em aula e **NÃO** acompanham o repositório nativamente)*

## 🚀 Como Executar
1. Certifique-se de que o **Vulkan SDK** e o **Git** estejam devidamente instalados e reconhecidos em sua máquina.
2. Certifique-se de ter clonado e compilado com sucesso o projeto [sd.cpp](https://github.com/leejet/stable-diffusion.cpp) com a bandeira do `VULKAN_BACKEND`. O passo a passo completo está no vídeo desta aula!
3. Baixe o modelo base (`.safetensors`) do HuggingFace e renomeie-o para `modelo_do_sd.safetensors`.
4. Coloque o executável já compilado (`sd.exe`) e o arquivo do modelo na mesma pasta onde está o script `gerador_imagens.py`.
5. Execute o código pelo seu terminal:
   ```bash
   python gerador_imagens.py
   ```
6. Digite o que deseja ver (de preferência digite os *prompts* em inglês) e aguarde sua Placa de Vídeo criar magia resultando no arquivo local `saida_final.png`!
