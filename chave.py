import time
import random
def gerar_chave(menu_votacao, menu_gerenciamento):
    print("\nCadastro de título e CPF registrado")
    print("Estamos gerando sua chave...")

    time.sleep(2)

    chave = f"{random.randint(0, 999999):06}"
    print("Sua chave é:", chave)

    x = 0

    while x != 2 and x != 11:
        x = int(input("\nDigite 2 para votação ou 11 para gerenciamento: "))

        if x == 2:
            print("Indo para votação...")
            menu_votacao()

        elif x == 11:
            print("Voltando ao gerenciamento...")
            menu_gerenciamento()

        else:
            print("Opção inválida\n")
    return chave