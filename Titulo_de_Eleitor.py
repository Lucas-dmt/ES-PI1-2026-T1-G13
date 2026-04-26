import random
import string

eleitores = []

# ==== GERAR CHAVE: ====
import time
import random

def gerar_chave():
    print("\nCadastro de título e CPF registrado ")
    print("Estamos gerando sua chave...")

    time.sleep(5)

    chave = f"{random.randint(0, 999999):06}"

    print(f"Sua chave é: {chave}")
    x = int(input("Digite 2 para ir no menu de votacao ou 11 para voltar ao gerenciamento:"))
    if x == 2: 
    menu_votacao()
    elif x == 11:
    print("Voltando...")
    return
    
    return chave


gerar_chave()
=============================

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
   titulo_eleitor = int(input("Digite o número do título com 12 numeros:"))
    if titulo_eleitor == "11":
            print("Voltando...")
            return
    if len(titulo_eleitor) != 12:
        print("Título inválido ")
        return
    if cont < len(cpf):
        print("O Titulo preicsa ter 12 dígitos e conter apenas números reais")
        titulo_eleitor = int(input("Digite o número do título de Eleitor:"))
                                   
    eleitor_existente = buscar_eleitor(titulo)

    if eleitor_existente:
        print("Título já cadastrado ")
        print("Chave:", eleitor_existente[1])
        print("Já votou:", "Sim" if eleitor_existente[2] else "Não")
        return

    chave = gerar_chave()
    novo = [titulo, chave, False]
    eleitores.append(novo)

    print("Eleitor cadastrado com sucesso ")
    print("Sua chave é:", chave)


def votar():
    titulo = input("Digite o título: ")
    chave = input("Digite a chave: ")

    eleitor = buscar_eleitor(titulo)

    if not eleitor:
        novo cadastro = input("Título não encontrado. Deseja cadastrar? (s/n): ").lower()
        if opcao == "s":
        nome = input("Digite seu nome: ")
        estado = input("Digite o estado em letra Maiuscula(ex: SP, RJ): ").upper()
        cpf = input("insira seu CPF: ")
        
 estados_validos = [
    "AC","AL","AP","AM","BA","CE","DF","ES","GO",
    "MA","MT","MS","MG","PA","PB","PR","PE","PI",
    "RJ","RN","RS","RO","RR","SC","SP","SE","TO"
]

          if estado not in estados_validos:
             print("Estado incorreto.Digite a sigla ")
          elif estado == "0":
             print("Estado nao inserido")

          if cpf == "0":
              print("Cpf nao inserido")
          elif cpf == cpf
              print("Cpf ja esta cadastrado")
         if opcao == "n":
             break 

menu_principal()

    if eleitor[1] != chave:
        print("Chave incorreta")
        return

    if eleitor[2]:
        print("Você já votou ")
        return

    eleitor[2] = True
    print("Voto registrado com sucesso")


def consultar():
    titulo = input("Digite o título: ")

    eleitor = buscar_eleitor(titulo)

    if eleitor:
        print("\nDados do eleitor:")
        print("Título:", eleitor[0])
        print("Chave:", eleitor[1])
        print("Já votou:", "Sim" if eleitor[2] else "Não")
    else:
        print("Eleitor não encontrado")

        print("\n--- ELEITOR ENCONTRADO ---")
                    print(f"Nome: {eleitor[1]}")
                    print(f"Título de Eleitor: {eleitor[2]}")
                    print(f"CPF: {eleitor[3]}")
                    print("Já votou:", "Sim" if eleitor[2] else "Não")
                else:
                    print("\n[!] Erro: Eleitor não encontrado.")

if titulo_eleitor == "11":
            print("Voltando...")
            return

VALIDAR TITULO DE ELEITOR

if len(cpf) != 11 and cont < len(cpf):
                        print("O cpf preicsa ter 11 dígitos e conter apenas números reais")
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
