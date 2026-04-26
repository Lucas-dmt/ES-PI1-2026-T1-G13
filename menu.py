 
def menu_gerenciamento(): 
    """
    gerenciamento de eleitores e candidatos
    args:
        none
    returns:
        none
    """
    opcao = 0  #comecamos a opcao com 0 so para entrar no menu pela primeira vez
    while opcao !=11: #menu continua abrindo enquanto o usuario nao escolher a opcao de voltar
        print("\n=== MENU GERENCIAMENTO ===")
        print("1 - Cadastrar eleitor")
 
        print("2 - Listar eleitores")
        print("3 - Buscar eleitor")
        print("4 - Editar eleitor")
        print("5 - Remover eleitor")
        print("6 - Cadastrar candidato")
        print("7 - Listar candidatos")
        print("8 - Buscar candidato")
        print("9 - Editar candidato")
        print("10 - Remover candidato")
        print("11 - Voltar")

        try: #tenta transformar o que o usuario digitou em numero
            opcao = int(input("Escolha uma opcao: "))
        except ValueError: #se o usuario digitar letra ou algo invalido, a opcao vira 0 (ValueError)
            opcao = 0

        #a partir daqui o programa verifica qual numero foi escolhido   
        from conexaobd import executar  #importa a função de execução da conexaobd
        match opcao:
            case 1:
                nome_completo = input("Digite seu nome completo:")
                titulo_eleitor = int(input("Digite o número do título de eleitor:"))
                cpf = input("Digite seu CPF:")
                prefixo_cpf = cpf[:4] #pega os 4 primeiros dígitos
                mesario = input("Mesário s/n:").lower()
                if mesario == "s":
                    mesario = 1
                else:
                    mesario = 0
                valores = (nome_completo,titulo_eleitor,cpf, prefixo_cpf)
                comando = "INSERT INTO eleitores (nome, titulo_eleitor, prefixo_cpf, cpf_cifrado, mesario, chave_acesso_cifrada, ja_votou) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                executar(comando,valores)
                print("Cadastrado.")   
             
       #=============== VALIDAÇÃO DO TITULO DE ELEITOR ========== 
def campo_vazio(texto):
    return texto == ""

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
    if len(titulo_eleitor) != 12:
        print("Erro: precisa ter exatamente 12 dígitos.\n")
        continue

    # 2. apenas números 
    if not apenas_numeros(titulo_eleitor):
        print("Erro: o título deve conter apenas números.\n")
        continue

    # 3. não pode ser tudo igual (ex: 111111111111)
    if todos_iguais(titulo_eleitor):
        print("Erro: número inválido (todos os dígitos são iguais).\n")
        continue

    # 4. não pode ser sequência óbvia (123456789012)
    if sequencia_crescente(titulo_eleitor):
        print("Erro: número inválido (sequência crescente).\n")
        continue

    # 5. UF do título: posições 9 e 10
    uf = int(titulo_eleitor[8:10])
    if uf < 1 or uf > 28:
        print("Erro: código de estado inválido no título.\n")
        continue
    #6. não pode ter campo vazio
    if campo_vazio(titulo_eleitor):
            print("Erro: o título não pode estar vazio.\n")
            continue
 
    # Verifica se o campo foi validado
    if titulo_valido = True
    print("\nTítulo válido com sucesso!")
    print(cpf)

    else:

        titulo_valido = True

        for c in titulo_eleitor:
            if c < "0" or c > "9":
                titulo_valido = False

        if not titulo_valido:
            print("Título inválido: só pode conter números")

        else:

            numero = titulo_eleitor[:8] # 8 primeiros digitos
            uf = titulo_eleitor[8:10] # codigo do estado com 2 digitos
            digitos = titulo_eleitor[10:12] #ultimos 2 digitos (verificadores)

             #============ CALCULO DO PRIMEIRO DIGITO ========
            pesos1 = [2, 3, 4, 5, 6, 7, 8, 9]

            soma = 0
            for i in range(8):
                soma += int(numero[i]) * pesos1[i]

            resto = soma % 11
            dv1 = 0 if resto == 10 else resto

             #============ CALCULO DO SEGUNDO DIGITO ========
            soma2 = (int(uf[0]) * 7) + (int(uf[1]) * 8) + (dv1 * 9)

            resto2 = soma2 % 11
            dv2 = 0 if resto2 == 10 else resto2
             #============= VALIDAÇÃO FINAL =========
            if digitos == str(dv1) + str(dv2):
                print("Título válido")
                titulo_valido = True
            else:
                print("Título inválido: dígitos não conferem")
                titulo_valido = False

            # ==== VALIDAÇÃO DO CPF ====
             def campo_vazio(texto):
            return texto  == ""

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

                    elif campo_vazio(cpf):
                        print("Erro: o título não pode estar vazio.\n")
                        cpf = input("CPF:")
                        count = 0
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

# ==== GERAR CHAVE: ====
import time
import random

def gerar_chave():
    print("\nCadastro de título e CPF registrado ")
    print("Estamos gerando sua chave...")

    time.sleep(5) # tempo de 5 segundos para gerar a chave 

    chave = f"{random.randint(0, 999999):06}" # gera uma chave aleatoria de 6 digitos inteiros

    print(f"Sua chave é: {chave}")
    x = int(input("Digite 2 para ir no menu de votacao ou 11 para voltar ao gerenciamento:"))
    if x == 2: 
    menu_votacao()
    elif x == 11:
    print("Voltando...")
    menu_gerenciamento()
    
    return chave


gerar_chave()


           # ==== INSERÇÃO NO BANCO ====
                comando="INSERT INTO eleitores (nome,titulo_eleitor,cpf,mesario) VALUES (%s, %s, %s,%s)"
                valores=(nome_completo,titulo_eleitor,cpf,mesario)
                executar(comando,valores)
                print("Cadastrado com sucesso!")
            case 2:
                print("Listagem de eleitores ainda nao foi feita.")
            case 3:
                from conexaobd import buscar
                cpf_inserido = input("Digite o seu CPF:")
                comando = "SELECT * FROM eleitores WHERE cpf_cifrado = %s"
                valores = (cpf_inserido,)
                eleitor = buscar(comando, valores)
                if eleitor:
                    print("\n--- ELEITOR ENCONTRADO ---")
                    print(f"Nome: {eleitor[1]}")
                    print(f"Título de Eleitor: {eleitor[2]}")
                    print(f"CPF: {eleitor[3]}")
                else:
                    print("\n[!] Erro: Eleitor não cadastrado.")
            case 4:
                print("Edicao de eleitor ainda nao foi feita.")
            case 5:
                print("Remocao de eleitor ainda nao foi feita.")
            case 6:
         # ==== CADASTRO DE CANDIDATO ==== 
                nome_completo_candidato=input("Digite seu nome completo:")
                numero_candidato=int(input("Seu número para votação:"))
                id_partido=int(input("Informe o ID do partido:"""))
                comando="INSERT INTO candidatos (nome_completo_candidato,numero_candidato,id_partido) VALUES (%s, %s, %s)"
                valores=(nome_completo_candidato,numero_candidato,id_partido)
                executar(comando,valores)
 
                print("Cadastrado com sucesso!")
            case 7:
                print("Listagem de candidatos ainda nao foi feita.")
            case 8:
                from conexaobd import buscar
                numero_candidatoB = int(input("Digite o número do candidato:"))
                comando = """
                 SELECT c.candidato, p.partido, p.sigla
                 FROM candidatos c
                 JOIN partidos p ON c.id_partido = p.id_partido
                 WHERE c.numero_votacao = %s
                """
                valores = (numero_candidatoB,)
                resultado = buscar(comando, valores)
                if resultado:
                    print("\n--- INFORMAÇÕES DO CANDIDATO ---")
                    print(f"Nome: {resultado[0]}")
                    print(f"Partido: {resultado[1]}")
                    print(f"Sigla: {resultado[2]}")
            case 9:
                print("Edicao de candidatos ainda nao foi feita.")
            case 10:
                print("Remocao de candidato ainda nao foi feita.")
            case 11:
                print("Voltando ao menu principal...")
            case _:
                print("Opcao invalida.")

def menu_abrir_votacao():
    """
    menu de abrir votação, identifica mesario e realiza a zerezima
    args:
        none
    returns:
        none
    """
    opcao = 0
    while opcao != 3:
        print("\n=== ABRIR SISTEMA DE VOTACAO ===")


        print("1 - Identificar mesario")
        print("2 - Realizar zerezima")
        print("3 - Voltar")
        try:

            opcao = int(input("Escolha uma opcao: "))
        except ValueError:
            opcao = 0

        match opcao:
            case 1:
                print("Identificacao do mesario ainda nao foi feita.")
            case 2:
                print("Zerezima ainda nao foi feita.")
            case 3:
                print("Voltando ao menu de votacao...")
            case _:
                print("Opcao invalida.")

def menu_auditoria():
    """
    menu de auditoria da votação, exibe logs e protocolos
    args:
        none
    returns:
        none
    """
    opcao = 0
    while opcao != 3:
        print("\n=== AUDITORIA DA VOTACAO ===")
        print("1 - Exibir logs")
        print("2 - Exibir protocolos")
        print("3 - Voltar")
        try:
            opcao = int(input("Escolha uma opcao: "))
        except ValueError:
            opcao = 0

        match opcao:
            case 1:
                print("Exibicao de logs ainda nao foi feita.")
            case 2:
                print("Exibicao de protocolos ainda nao foi feita.")
            case 3:
                print("Voltando ao menu de votacao...")
            case _:
                print("Opcao invalida.")

def menu_resultados():
    """
    resultados da votação
    args: 
        none
    returns:
        none
    """
    opcao = 0
    while opcao != 5:
        print("\n=== RESULTADOS DA VOTACAO ===")
        print("1 - Boletim de urna")
        print("2 - Estatistica de comparecimento")
        print("3 - Votos por partido")
        print("4 - Validacao de integridade")
        print("5 - Voltar")
        try:
            opcao = int(input("Escolha uma opcao: "))
        except ValueError:
            opcao = 0

        match opcao:
            case 1:
                print("Boletim de urna ainda nao foi feito.")
            case 2:
                print("Estatistica de comparecimento ainda nao foi feita.")
            case 3:
                print("Votos por partido ainda nao foram feitos.")
            case 4:
                print("Validacao de integridade ainda nao foi feita.")
            case 5:
                print("Voltando ao menu de votacao...")
            case _:
                print("Opcao invalida.")

def menu_votacao():
    """
    menu principal de votação
    args:
        none
    returns:
        none
    """
    opcao = 0
    while opcao != 4:
        print("\n=== MENU VOTACAO ===")
        print("1 - Abrir sistema de votacao")
        print("2 - Auditoria da votacao")
        print("3 - Resultados da votacao")
        print("4 - Voltar")
        try:
            opcao = int(input("Escolha uma opcao: "))
        except ValueError:
            opcao = 0

        match opcao:
            case 1:
                menu_abrir_votacao()
            case 2:
                menu_auditoria()
            case 3:
                menu_resultados()
            case 4:
                print("Voltando ao menu principal...")
            case _:
                print("Opcao invalida.")

def menu_principal():
    """
    menu principal, onde todo o sistema roda
    args:
        none
    returns:
        none
    """
    opcao = 0
    while opcao != 3:
        print("\n=== SISTEMA LAD.PY ===")
        print("1 - Gerenciamento")
        print("2 - Votacao")
        print("3 - Sair")
        try:
            opcao = int(input("Escolha uma opcao: "))
        except ValueError:
            opcao = 0

        match opcao:
            case 1:
                menu_gerenciamento()
            case 2:
                menu_votacao()
            case 3:
                print("Saindo...")
            case _:
                print("Opcao invalida.")
menu_principal()

         



