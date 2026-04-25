import random
import string

eleitores = []

def gerar_chave():
    caracteres = string.ascii_letters + string.digits
    chave = ""
    for i in range(6):
        chave += random.choice(caracteres)
    return chave

def buscar_eleitor(titulo):
    for eleitor in eleitores:
        if eleitor[0] == titulo:
            return eleitor
    return None

nums = [int(n) for n in titulo]

    pesos = [2,3,4,5,6,7,8,9]
    soma = 0

for i in range(8):
    soma = sum(nums[i] * pesos[i])
    resto = soma % 11
if resto == 10 :
    divisao1 = 0 
else:
   resto
 
    soma2 = (nums[8]*7) + (nums[9]*8) + (dv1*9)
    resto2 = soma2 % 11

if resto2 == 10:
    divisão2 = 0
else:
    divisão2 = resto2

    return nums[10] == divisao1 and nums[11] == divisao2

def cadastrar():
    titulo = input("Digite o título (12 números): ")

    if len(titulo) != 12 or not titulo.isdigit():
        print("Título inválido ❌")
        return

    eleitor_existente = buscar_eleitor(titulo)

    if eleitor_existente:
        print("Título já cadastrado ✅")
        print("Chave:", eleitor_existente[1])
        print("Já votou:", "Sim✅" if eleitor_existente[2] else "Não❌")
        return

    chave = gerar_chave()
    novo = [titulo, chave, False]
    eleitores.append(novo)

    print("Eleitor cadastrado com sucesso ✅")
    print("Sua chave é:", chave)


def votar():
    titulo = input("Digite o título: ")
    chave = input("Digite a chave: ")

    eleitor = buscar_eleitor(titulo)

    if not eleitor:
        print("Eleitor não cadastrado ❌")
        return

    if eleitor[1] != chave:
        print("Chave incorreta ❌")
        return

    if eleitor[2]:
        print("Você já votou ❌")
        return

    eleitor[2] = True
    print("Voto registrado com sucesso ✅")


def consultar():
    titulo = input("Digite o título: ")

    eleitor = buscar_eleitor(titulo)

    if eleitor:
        print("\nDados do eleitor:")
        print("Título:", eleitor[0])
        print("Chave:", eleitor[1])
        print("Já votou:", "Sim✅" if eleitor[2] else "Não❌")
    else:
        print("Eleitor não encontrado ❌")


