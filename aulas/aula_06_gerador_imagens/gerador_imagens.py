import subprocess
import time

def gerar_imagem(prompt, steps):
    comando = [
        "sd.exe",
        "-m", "modelo_do_sd.safetensors",
        "-p", prompt,
        "--steps", str(steps),
        "-o", "saida_final.png"
    ]
    
    print(f"\n🖼️ Mágica de {steps} passos engatilhada, aguarde a GPU...")
    
    try:
        # Usamos subprocess.run para chamar o executável compilado em C++ (sd.exe)
        subprocess.run(comando, check=True)
        print("\n✅ Arte gerada e liberta com sucesso! Verifique o arquivo 'saida_final.png'.")
    except FileNotFoundError:
        print("\n[!] ERRO: O executável 'sd.exe' não foi encontrado!")
        print("    Certifique-se de que você compilou o sd.cpp com Vulkan conforme a aula.")
        print("    O 'sd.exe' e o 'modelo_do_sd.safetensors' devem estar na mesma pasta deste script.")
    except subprocess.CalledProcessError as e:
        print(f"\n[!] ERRO durante a geração da imagem (Código de saída: {e.returncode})")
        print("    Verifique se você possui VRAM suficiente e se os drivers Vulcan estão instalados.")
    except Exception as e:
        print(f"\n[!] ERRO INESPERADO: {e}")

if __name__ == "__main__":
    print("====================================")
    print("🟢 GERADOR MÁGICO NA GPU V1.0 🟢")
    print("====================================\n")
    
    prompt_usuario = input("Diga, o que você quer gerar na imagem?: ")
    steps_usuario = input("Quantos passos (steps)? Tente algo entre 10 e 30: ")
    
    # Tratamento simples para segurança do formato numérico:
    if not steps_usuario.isdigit():
        print("[*] Valor inválido para passos. Utilizando o padrão de 20 steps.")
        steps_usuario = "20"
    
    gerar_imagem(prompt_usuario, steps_usuario)
