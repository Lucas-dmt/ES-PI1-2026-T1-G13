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
    print("Digite 11 para voltar ao gerenciamento")
    if titulo_eleitor == "11":
        print("Voltando...")
        return menu_gerenciamento()

cont = 0                             
   while cont != 11:                             
    cont = 0 
    for k in range(len(cpf)): 
     if cpf[k] >= "0" and cpf[k] <= "9":
    cont += 1
    if len(titulo_eleitor) != 12:
        print("Título inválido ")
        return
    if cont < len(titulo_eleitor):
        print("O Titulo preicsa ter 12 dígitos e conter apenas números reais")
        return titulo_eleitor

    if len(titulo_eleitor) != 12 and cont < len(titulo-eleitor):
        print("O titulo precisa ter 12 dígitos e conter apenas números reais")
        titulo_eleitor = input("Titulo:") 
        cont = 0

    elif len(titulo_eleitor) != 12:
        print("O Titulo precisa ter 12 dígitos")
        titulo_eleitor= input("Titulo:")
        cont = 0

    elif cont != 12:
         print("Utilize apenas números reais")
         titulo_eleitor = input("Titulo:")
         cont = 0

                                   
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



print("Digite 11 para voltar ao gerenciamento")
    if titulo_eleitor == "11":
        print("Voltando...")
        return menu_gerenciamento()



VALIDAR CPF
cont = 0 
cpf_valido = True
                while cont != 11:                             
                    cont = 0 
                    # aqui ele verifica se todos os caracteres são números, 11 dígitos
                    for k in range(len(cpf)): 
                        if cpf[k] >= "0" and cpf[k] <= "9":
                            cont += 1
                           
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
                    else:                                                       # a partir desse "else", acontece a verificação matemática.
                        iguais=0                                                # em primeiro lugar, verifica-se se o cpf não possui todos os dígitos iguais.
                        for k in range (len(cpf)):                              # em segundo lugar, é verificado o primeiro dígito de verificação.
                            if cpf[k] == cpf[0]:                                # em terceiro lugar, é verificado o segundo dígito de verificação.
                                iguais+=1                                       # depois, os dígitos verificadores são comparados e então validados.
                        if iguais == 11:
                            print("CPF inválido: números repetidos")
                            cpf = input("CPF:")
                            cont = 0
                        else:
                            soma1=0
                            multiplicacao1=10
                            for i in range(9):
                                soma1+=int(cpf[i])*multiplicacao1               # nesta linha, a string "cpf" é convertida em número inteiro,
                                i+=1                                            # para que possa ser multiplicada como um número.
                                multiplicacao1-=1
                            resto1=soma1%11
                            if resto1<2:
                                first_verify=0
                            else:
                                first_verify=11-resto1
                                if first_verify>=10:
                                    first_verify=0

                            #Cálculo do segundo dígito verificador
                            soma2=0                                            
                            multiplicacao2=11
                            for i in range(9):
                                soma2+=int(cpf[i])*multiplicacao2
                                i+=1
                                multiplicacao2-=1
                            soma2+=first_verify*2
                            resto2=soma2%11
                            if resto2<2:
                                second_verify=0
                            else:
                                second_verify=11-resto2
                                if second_verify>=10:
                                    second_verify=0
                             #Validação final
                            if first_verify == int(cpf[9]) and second_verify == int(cpf[10]):   
                                print("CPF válido!")
                        
                            else:
                                print("CPF inválido: erro nos dígitos verificadores.")
                                cpf = input("CPF: ")
                                cont = 0

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



