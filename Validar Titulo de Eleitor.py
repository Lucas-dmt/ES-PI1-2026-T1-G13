if len(titulo_eleitor) != 12:
    print("Título inválido: precisa ter 12 dígitos")
else:

    titulo_valido = True

    for c in titulo_eleitor:
        if c < "0" or c > "9":
            valido = False

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
        else:
            print("Título inválido: dígitos não conferem")



if cpf_valido and titulo_valido:
  
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

else:
    print("\nCadastro inválido")

