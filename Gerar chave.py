import time
import random

def gerar_chave():
    print("\nCadastro de título e CPF registrado")
    print("Estamos gerando sua chave...")

    time.sleep(5)

    chave = f"{random.randint(0, 999999):06}"

    print(f"Sua chave é: {chave}")

    return chave


def escolher():
    x = int(input("\nDigite 2 para ir no menu de votação ou 11 para voltar ao gerenciamento: "))

    if x == 2:
        print("Indo para o menu de votação... ")

    elif x == 11:
        print("Voltando ao gerenciamento...")

    else:
        print("Resposta inválida ")
        x = int(input("\nDigite 2 para ir no menu de votação ou 11 para voltar ao gerenciamento: "))
    

gerar_chave()
escolher()
