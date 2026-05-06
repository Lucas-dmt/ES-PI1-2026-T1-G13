### VALIDAÇÃO DO CPF ###

def validar_cpf(cpf):
     cont = 0                             
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


# ==== VALIDAÇÃO DO TÍTULO ====

# Função que verifica se o campo está vazio ou só tem espaço
def campo_vazio(texto):
                    if texto == "":
                        return True
                    for c in texto:
                        if c != " ":
                            return False
                    return True
                # Função que verifica se todos os caracteres são números
def apenas_numeros(texto):
                    for c in texto:
                        if c < "0" or c > "9":
                            return False
                    return True
                # Função que verifica se todos os dígitos são iguais (ex: 111111111111)
def todos_iguais(texto):
                    if texto == "":
                        return False
                    return all(c == texto[0] for c in texto)
                # Função que verifica se é uma sequência crescente (ex: 123456...)  
def sequencia_crescente(texto):
    for i in range(len(texto) - 1):
        if int(texto[i]) + 1 != int(texto[i + 1]):
            return False
    return True

def validar_titulo(titulo_eleitor):
 # Variável de controle do loop
 titulo_valido = False
 # Loop que só para quando o título for válido
 while not titulo_valido:
# Verifica se está vazio
    if campo_vazio(titulo_eleitor):
        print("Erro: campo vazio.\n")
        titulo_eleitor = input("Tente novamente:")
 # Verifica se só tem números
    elif not apenas_numeros(titulo_eleitor):
        print("Erro: o título deve conter apenas números.\n")
        titulo_eleitor = input("Tente novamente:")
# Verifica tamanho correto (12 dígitos)
    elif len(titulo_eleitor) != 12:
        print("Erro: precisa ter exatamente 12 dígitos.\n")
        titulo_eleitor = input("Tente novamente:")
# Verifica sequência crescente inválida
    elif sequencia_crescente(titulo_eleitor):
        print("Erro: sequência inválida.\n")
        titulo_eleitor = input("Tente novamente:")
    else:
 # Extrai UF (posição 8 e 9 do número)
        uf = int(titulo_eleitor[8:10])
        if uf < 1 or uf > 28:
            print("Erro: UF inválida.\n")
            titulo_eleitor = input ("Tente novamente:")
            continue
        else:
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
                titulo_valido = True
            else:
                print("Título inválido: dígitos não conferem")

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
                                                                                                                                                       