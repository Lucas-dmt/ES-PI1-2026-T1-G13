 PEDRO
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
 main
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
PEDRO
        try: #tenta transformar o que o usuario digitou em numero
            opcao = int(input("Escolha uma opcao: "))
        except ValueError: #se o usuario digitar letra ou algo invalido, a opcao vira 0 (ValueError)
            opcao = 0

        #a partir daqui o programa verifica qual numero foi escolhido   
        from conexaobd import executar    
        match opcao:
            case 1:
                nome_completo = input("Digite seu nome completo:")
            titulo_eleitor = int(input("Digite o número do título:"))
            cpf = input("Digite seu CPF:")
            prefixo_cpf = cpf[:4]
            mesario = input("Mesário s/n:").lower()
            if mesario == "s":
                mesario = 1
            else:
                mesario = 0
            valores = (nome_completo,titulo_eleitor,cpf, prefixo_cpf)
            comando = "INSERT INTO eleitores (nome, titulo_eleitor, prefixo_cpf, cpf_cifrado, mesario, chave_acesso_cifrada, ja_votou) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            executar(comando,valores)
            print("Cadastrado.")                  #validção do cpf.
                cont=0                                      #assegura que o cpf tem todos os 11 dígitos, os quais devem ser apenas números.
                while cont!=11:                             #obs:o cont=0 dentro do while serve para reiniciar a contagem de dígitos após uma tentativa de digitação.
                    cont=0                                  #esta primeira parte verifica se há 11 dígitos, sendo eles apenas números reais.
                    for k in range (len(cpf)):
                        if cpf[k]>="0" and cpf[k]<="9":
                            cont+=1
                    if len(cpf) != 11 and cont != 11:
                        print("o cpf precisa ter 11 dígitos e apenas números reais")
                        cpf=input("CPF:")
                    elif len(cpf) != 11 or cont != 11:
                        if len(cpf) != 11:
                            print("o cpf precisa ter 11 dígitos")
                        else:
                            print("utilize apenas números reais")
                        cpf=input("CPF:")
                        cont = 0 
                    else:                                                       #a partir desse "else", acontece a verificação matemática.
                        iguais=0                                                #em primeiro lugar, verifica-se se o cpf não possui todos os dígitos iguais.
                        for k in range (len(cpf)):                              #em segundo lugar, é verificado o primeiro dígito de verificação.
                            if cpf[k] == cpf[0]:                                #em terceiro lugar, é verificado o segundo dígito de verificação.
                                iguais+=1                                       #depois, os dígitos verificadores são comparados e então validados.
                        if iguais == 11:
                            print("CPF inválido: números repetidos")
                            cpf = input("CPF:")
                            cont = 0
                        else:
                            soma1=0
                            multiplicacao1=10
                            for i in range(9):
                                soma1+=int(cpf[i])*multiplicacao1               #nesta linha, a string cpf é convertida em número inteiro,
                                i+=1                                            #para que possa ser multiplicada como um número.
                                multiplicacao1-=1
                            resto1=soma1%11
                            if resto1<2:
                                first_verify=0
                            else:
                                first_verify=11-resto1
                                if first_verify>=10:
                                    first_verify=0

                           
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

                            if first_verify == int(cpf[9]) and second_verify == int(cpf[10]):
                                print("CPF válido!")
                        
                            else:
                                print("CPF inválido: erro nos dígitos verificadores.")
                                cpf = input("CPF: ")
                                cont = 0



                mesario=input("Mesário s/n:")
                comando="INSERT INTO eleitores (nome,titulo_eleitor,cpf,mesario) VALUES (%s, %s, %s,%s)"
                valores=(nome_completo,titulo_eleitor,cpf,mesario)
                executar(comando,valores)
                print("Cadastrado com sucesso!")
            case 2:
                print("Listagem de eleitores ainda nao foi feita.")
            case 3:
                print("Busca de eleitor ainda nao foi feita.")
            case 4:
                print("Edicao de eleitor ainda nao foi feita.")
            case 5:
                print("Remocao de eleitor ainda nao foi feita.")
            case 6:

    
    main
                nome_completo_candidato=input("Digite seu nome completo:")
                numero_candidato=int(input("Seu número para votação:"))
                id_partido=int(input("Informe o ID do partido:"""))
                comando="INSERT INTO candidatos (nome_completo_candidato,numero_candidato,id_partido) VALUES (%s, %s, %s)"
                valores=(nome_completo_candidato,numero_candidato,id_partido)
                executar(comando,valores)
 PEDRO
                print("Cadastrado com sucesso!")
            case 7:
                print("Listagem de candidatos ainda nao foi feita.")
            case 8:
                print("Busca de candidato ainda nao foi feita.")
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

 main
        print("1 - Identificar mesario")
        print("2 - Realizar zerezima")
        print("3 - Voltar")
        try:
 PEDRO
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

         



