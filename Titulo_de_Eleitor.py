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


==============================Codigo da validacao====



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

if cpf_valido:

    print("\nCadastro registrado com sucesso!")
    print("Gerando chave...")

    time.sleep(5)

    chave = f"{random.randint(0, 999999):06}"

    print(f"Sua chave é: {chave}")

    def escolher():
    x = int(input("\nDigite 2 para votação ou 11 para gerenciamento: "))

    if x == 2:














==============CORREÇÃO==========

def apenas_numeros(texto):
    for c in texto:
        if c < "0" or c > "9":
            return False
    return True


def todos_iguais(texto):
    return all(c == texto[0] for c in texto)


def sequencia_crescente(texto):
    for i in range(len(texto) - 1):
        if int(texto[i]) + 1 != int(texto[i + 1]):
            return False
    return True


titulo_valido = False

while not titulo_valido:
    titulo = input("Digite o número do título de eleitor (12 dígitos): ")

    # 1. tamanho
    if len(titulo) != 12:
        print("Erro: precisa ter exatamente 12 dígitos.\n")
        continue

    # 2. apenas números (sem isdigit)
    if not apenas_numeros(titulo):
        print("Erro: o título deve conter apenas números.\n")
        continue

    # 3. não pode ser tudo igual (ex: 111111111111)
    if todos_iguais(titulo):
        print("Erro: número inválido (todos os dígitos são iguais).\n")
        continue

    # 4. não pode ser sequência óbvia (123456789012)
    if sequencia_crescente(titulo):
        print("Erro: número inválido (sequência crescente).\n")
        continue

    # 5. regra extra simples (UF do título: posições 9 e 10)
    uf = int(titulo[8:10])
    if uf < 1 or uf > 28:
        print("Erro: código de estado inválido no título.\n")
        continue

    # se passou em tudo
    titulo_valido = True
    print("\nTítulo válido! Cadastro confirmado.")



