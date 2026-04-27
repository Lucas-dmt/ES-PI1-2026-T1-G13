titulo_eleitor = input("Digite o número do título:")

def campo_vazio(texto):
    return texto == ""

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

    if len(titulo_eleitor) != 12:
        print("Erro: precisa ter exatamente 12 dígitos.\n")
        titulo_eleitor = input("Digite novamente: ")
        continue

    if not apenas_numeros(titulo_eleitor):
        print("Erro: apenas números.\n")
        titulo_eleitor = input("Digite novamente: ")
        continue

    if todos_iguais(titulo_eleitor):
        print("Erro: números iguais.\n")
        titulo_eleitor = input("Digite novamente: ")
        continue

    if sequencia_crescente(titulo_eleitor):
        print("Erro: sequência inválida.\n")
        titulo_eleitor = input("Digite novamente: ")
        continue

    uf = int(titulo_eleitor[8:10])
    if uf < 1 or uf > 28:
        print("Erro: UF inválida.\n")
        titulo_eleitor = input("Digite novamente: ")
        continue

    if campo_vazio(titulo_eleitor):
        print("Erro: vazio.\n")
        titulo_eleitor = input("Digite novamente: ")
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
    else:
        print("Título inválido: dígitos não conferem")
        titulo_eleitor = input("Digite novamente: ")
