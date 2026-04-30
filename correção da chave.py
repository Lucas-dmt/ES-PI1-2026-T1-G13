import time
import random
def gerar_chave(menu_votacao, menu_gerenciamento):
    print("\nCadastro de título e CPF registrado")
    print("Estamos gerando sua chave...")

    time.sleep(5)
    
nome = input("Digite seu nome completo: ")

letras = nome[:2]# as 2 primeiras letras do nome

for i in range(len(nome)):
    if nome[i] == " ":
        letras += nome[i + 1]# soma as 2 primeiras letras,pula o espaço e junta a primeira letra do sobrenome depois do i espaço
     
chave = letras.upper() + f"{random.randint(1000, 9999)}"

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
