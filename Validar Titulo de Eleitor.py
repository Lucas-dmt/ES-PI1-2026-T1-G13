# ========================= # VALIDAÇÃO DO TITULO DE ELEITOR # =========================
titulo_valido = False

while not titulo_valido:

    titulo_eleitor = input("Título de eleitor: ")

    if len(titulo_eleitor) != 12:
        print("Título inválido: precisa ter 12 dígitos")

    else:

        titulo_valido = True

        for c in titulo_eleitor:
            if c < "0" or c > "9":
                titulo_valido = False

        if not titulo_valido:
            print("Título inválido: só pode conter números")

        else:

            numero = titulo_eleitor[:8]
            uf = titulo_eleitor[8:10]
            digitos = titulo_eleitor[10:12]

            pesos1 = [2, 3, 4, 5, 6, 7, 8, 9]

            soma = 0
            for i in range(8):
                soma += int(numero[i]) * pesos1[i]

            resto = soma % 11
            dv1 = 0 if resto == 10 else resto

            soma2 = (int(uf[0]) * 7) + (int(uf[1]) * 8) + (dv1 * 9)

            resto2 = soma2 % 11
            dv2 = 0 if resto2 == 10 else resto2

            if digitos == str(dv1) + str(dv2):
                print("Título válido")
                titulo_valido = True
            else:
                print("Título inválido: dígitos não conferem")
                titulo_valido = False
                
# ========================= # VALIDAÇÃO DO CPF # =========================

cpf_valido = False

while not cpf_valido:

    cpf = input("CPF: ")

    cont = 0

    for k in cpf:
        if "0" <= k <= "9":
            cont += 1

    if len(cpf) != 11:
        print("O CPF precisa ter 11 dígitos")

    elif cont != 11:
        print("Utilize apenas números")

    else:

        iguais = 0
        for k in cpf:
            if k == cpf[0]:
                iguais += 1

        if iguais == 11:
            print("CPF inválido: números repetidos")

        else:

            soma1 = 0
            peso = 10

            for i in range(9):
                soma1 += int(cpf[i]) * peso
                peso -= 1

            resto1 = soma1 % 11
            prim_verificacao = 0 if resto1 < 2 else 11 - resto1

            soma2 = 0
            peso = 11

            for i in range(9):
                soma2 += int(cpf[i]) * peso
                peso -= 1

            soma2 += prim_verificacao * 2

            resto2 = soma2 % 11
            sec_verificacao = 0 if resto2 < 2 else 11 - resto2

            if prim_verificacao == int(cpf[9]) and sec_verificacao == int(cpf[10]):
                print("CPF válido!")
                cpf_valido = True
            else:
                print("CPF inválido: dígitos não conferem")


# ========================= # GERAÇÃO DE CHAVE # =========================
import time
import random

if cpf_valido and titulo_valido:

    print("\nCadastro registrado com sucesso!")
    print("Gerando chave...")

    time.sleep(5)

    chave = f"{random.randint(0, 999999):06}"

    print(f"Sua chave é: {chave}")

    def escolher():
    x = int(input("\nDigite 2 para votação ou 11 para gerenciamento: "))

    if x == 2:
        print("Indo para votação...")

    elif x == 11:
        print("Voltando ao gerenciamento...")

    else:
        print("Opção inválida")
        
        return escolher()
