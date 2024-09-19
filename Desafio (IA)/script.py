import random
import string

def gerar_palavra_aleatoria(tamanho):
    return ''.join(random.choices(string.ascii_lowercase, k=tamanho))

def adivinhacao_maquina():
    palavra_usuario = input("Digite uma palavra: ").lower()
    comprimento = len(palavra_usuario)
    
    tentativa = ""
    tentativas = 0

    while tentativa != palavra_usuario:
        tentativa = gerar_palavra_aleatoria(comprimento)
        tentativas += 1
        print(f"Tentativa {tentativas}: {comprimento}: {tentativa}")
    

    print(f"\nA máquina acertou a palavra '{palavra_usuario}' após {tentativas} vezes!")

adivinhacao_maquina()