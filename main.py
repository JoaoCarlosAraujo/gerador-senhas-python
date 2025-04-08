import random
import string
import subprocess

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def copiar_para_area_transferencia(texto):
    try:
        processo = subprocess.Popen(['clip'], stdin=subprocess.PIPE, shell=True)
        processo.communicate(input=texto.encode('utf-8'))
        print("Senha copiada para a área de transferência.")
    except Exception as e:
        print("Erro ao copiar para a área de transferência:", e)

def main():
    print("Gerador de Senhas Fortes")
    tamanho = input("Digite o tamanho da senha (padrão 12): ")
    try:
        tamanho = int(tamanho)
    except ValueError:
        tamanho = 12

    senha = gerar_senha(tamanho)
    print("\nSenha gerada:", senha)
    copiar_para_area_transferencia(senha)

if __name__ == "__main__":
    main()
