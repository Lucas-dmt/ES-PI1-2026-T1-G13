### VALIDAÇÃO DO CPF ###

def validar_cpf(cpf):
    cont = 0
    # aqui ele verifica se todos os caracteres são números, 11 dígitos
    for k in range(len(cpf)):
        if cpf[k] >= "0" and cpf[k] <= "9":
            cont += 1

    if len(cpf) != 11 and cont < len(cpf):
        print("O cpf precisa ter 11 dígitos e conter apenas números reais")
        return False
    elif len(cpf) != 11:
        print("O cpf precisa ter 11 dígitos")
        return False
    elif cont != 11:
        print("Utilize apenas números reais")
        return False
    else:
        iguais = 0
        for k in range(len(cpf)):
            if cpf[k] == cpf[0]:
                iguais += 1

        if iguais == 11:
            print("CPF inválido: números repetidos")
            return False

        soma1 = 0
        multiplicacao1 = 10
        for i in range(9):
            soma1 += int(cpf[i]) * multiplicacao1
            multiplicacao1 -= 1

        resto1 = soma1 % 11
        if resto1 < 2:
            first_verify = 0
        else:
            first_verify = 11 - resto1
            if first_verify >= 10:
                first_verify = 0

        soma2 = 0
        multiplicacao2 = 11
        for i in range(9):
            soma2 += int(cpf[i]) * multiplicacao2
            multiplicacao2 -= 1

        soma2 += first_verify * 2
        resto2 = soma2 % 11
        if resto2 < 2:
            second_verify = 0
        else:
            second_verify = 11 - resto2
            if second_verify >= 10:
                second_verify = 0

        if first_verify == int(cpf[9]) and second_verify == int(cpf[10]):
            print("CPF válido!")
            return True
        else:
            print("CPF inválido: erro nos dígitos verificadores.")
            return False


# ==== VALIDAÇÃO DO TÍTULO ====

def campo_vazio(texto):
    if texto == "":
        return True
    for c in texto:
        if c != " ":
            return False
    return True


def apenas_numeros(texto):
    for c in texto:
        if c < "0" or c > "9":
            return False
    return True


def todos_iguais(texto):
    if texto == "":
        return False
    return all(c == texto[0] for c in texto)


def sequencia_crescente(texto):
    for i in range(len(texto) - 1):
        if int(texto[i]) + 1 != int(texto[i + 1]):
            return False
    return True


def validar_titulo(titulo_eleitor):
    if campo_vazio(titulo_eleitor):
        print("Erro: campo vazio.\n")
        return False
    elif not apenas_numeros(titulo_eleitor):
        print("Erro: o título deve conter apenas números.\n")
        return False
    elif len(titulo_eleitor) != 12:
        print("Erro: precisa ter exatamente 12 dígitos.\n")
        return False
    elif sequencia_crescente(titulo_eleitor):
        print("Erro: sequência inválida.\n")
        return False

    uf = int(titulo_eleitor[8:10])
    if uf < 1 or uf > 28:
        print("Erro: UF inválida.\n")
        return False

    numero = titulo_eleitor[:8]
    digitos = titulo_eleitor[10:12]
    pesos1 = [2, 3, 4, 5, 6, 7, 8, 9]
    soma = 0
    for i in range(8):
        soma += int(numero[i]) * pesos1[i]

    resto = soma % 11
    dv1 = 0 if resto == 10 else resto
    soma2 = (int(titulo_eleitor[8]) * 7) + (int(titulo_eleitor[9]) * 8) + (dv1 * 9)
    resto2 = soma2 % 11
    dv2 = 0 if resto2 == 10 else resto2

    if digitos == str(dv1) + str(dv2):
        print("Título válido")
        return True
    else:
        print("Título inválido: dígitos não conferem")
        return False

# === VERIFICAÇÃO DO NOME COMPLETO ===
def verificar_nome(nome_completo):
    valido = False
    while not valido:
        for i in range(len(nome_completo)):
            if nome_completo[i] ==" " and i != 0 and i != len(nome_completo) - 1:
                valido = True
                print("Nome completo válido!")
        if not valido:
            print("ERRO! Digite seu nome e sobrenome:")
            nome_completo = input("Tente novamente:")


                                                                                                                                                                                     