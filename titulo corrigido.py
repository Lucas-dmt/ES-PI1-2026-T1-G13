titulo_eleitor = input("Digite o número do título:")

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


titulo_valido = False

while not titulo_valido:

    if not apenas_numeros(titulo_eleitor):
        print("Erro: o título deve conter apenas números e sem espaço.\n")
        titulo_eleitor = input("Digite novamente o Titulo: ")
        continue

    if campo_vazio(titulo_eleitor):
        print("Erro: o campo não pode ser vazio\n")
        titulo_eleitor = input("Digite novamente o Titulo: ")
        continue

    if len(titulo_eleitor) != 12:
        print("Erro: precisa ter exatamente 12 dígitos.\n")
        titulo_eleitor = input("Digite novamente o Titulo: ")
        continue

    if sequencia_crescente(titulo_eleitor):
        print("Erro: sequência inválida.\n")
        titulo_eleitor = input("Digite novamente o Titulo: ")
        continue

    uf = int(titulo_eleitor[8:10])
    if uf < 1 or uf > 28:
        print("Erro: UF inválida.\n")
        titulo_eleitor = input("Digite novamente o Titulo: ")
        continue

    if campo_vazio(titulo_eleitor):
        print("Erro: vazio.\n")
        titulo_eleitor = input("Digite novamente o Titulo: ")
        continue

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

        cpf = input("Digite seu CPF:")
        
    else:
        print("Título inválido: dígitos não conferem")
        titulo_eleitor = input("Digite novamente: ")
 # ======= VALIDAÇÃO DO CPF ======
def campo_vazio(texto):
    return texto == ""

cont = 0
while cont != 11:
    cont = 0

    # aqui ele verifica se todos os caracteres são números, 11 dígitos
    for k in range(len(cpf)):
        if cpf[k] >= "0" and cpf[k] <= "9":
            cont += 1

    if len(cpf) != 11 and cont < len(cpf):
        print("O cpf prescisa ter 11 dígitos e conter apenas números reais")
        cpf = input("CPF:")
        cont = 0

    elif len(cpf) != 11:
        print("O cpf precisa ter 11 dígitos")
        cpf = input("CPF:")
        cont = 0

    elif cont != 11:
        print("Utilize apenas números reais")
        cpf = input("CPF:")
        cont = 0

    elif campo_vazio(cpf):
        print("O cpf não pode estar vazio.\n")
        cpf = input("CPF:")
        count = 0

    else:  # a partir desse "else", acontece a verificação matemática.
        iguais = 0  # verifica se o cpf não possui todos os dígitos iguais.

        for k in range(len(cpf)):
            if cpf[k] == cpf[0]:
                iguais += 1

        if iguais == 11:
            print("CPF inválido: números repetidos")
            cpf = input("CPF:")
            cont = 0

        else:
            soma1 = 0
            multiplicacao1 = 10

            for i in range(9):
                soma1 += int(cpf[i]) * multiplicacao1
                i += 1
                multiplicacao1 -= 1

            resto1 = soma1 % 11

            if resto1 < 2:
                first_verify = 0
            else:
                first_verify = 11 - resto1
                if first_verify >= 10:
                    first_verify = 0

            # Cálculo do segundo dígito verificador
            soma2 = 0
            multiplicacao2 = 11

            for i in range(9):
                soma2 += int(cpf[i]) * multiplicacao2
                i += 1
                multiplicacao2 -= 1

            soma2 += first_verify * 2
            resto2 = soma2 % 11

            if resto2 < 2:
                second_verify = 0
            else:
                second_verify = 11 - resto2
                if second_verify >= 10:
                    second_verify = 0

            # Validação final
            if first_verify == int(cpf[9]) and second_verify == int(cpf[10]):
                print("CPF válido!")

            else:
                print("CPF inválido: erro nos dígitos verificadores.")
                cpf = input("CPF: ")
                cont = 0


def gerar_chave():
    print("\nCadastro de título e CPF registrado")
    print("Estamos gerando sua chave...")

    time.sleep(5)

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


gerar_chave()
