def menu_gerenciamento():
    """
    gerenciamento de candidatos e eleitores
    args:
        none
    returns:
          none
    """
    opcao = 0
    while opcao !=11:
        print("\n === MENU GERENCIAMENTO === ")
        print("1 - Cadastrar eleitores")
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
    try:
        opcao = input("Escolha uma opção:")
    except ValueError:
        opcao = 0
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
            print("Cadastrado.")
        case 2:
            print("A listagem de eleitores ainda não foi feita")
        case 3:
            print("A busca de eleitor ainda não foi feita")
        case 4:
            print("Edição de eleitor ainda não foi feita")
        case 5:
            print("Remoção de eleitor ainda não foi feita")
        case 6:
                nome_completo_candidato=input("Digite seu nome completo:")
                numero_candidato=int(input("Seu número para votação:"))
                id_partido=int(input("Informe o ID do partido:"""))
                comando="INSERT INTO candidatos (nome_completo_candidato,numero_candidato,id_partido) VALUES (%s, %s, %s)"
                valores=(nome_completo_candidato,numero_candidato,id_partido)
                executar(comando,valores)
                print("Cadastrado.")
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
def abrir_votacao():
    """
    menu de abrir votação, realiza zerezima e identifica o mesario
    args:
        none
    returns:
          none
    """
    opcao = 0
    while opcao != 3:
        print("\n === SISTEMA DE VOTAÇÃO ===")
        print("1 - Identificar mesario")
        print("2 - Realizar zerezima")
        print("3 - Voltar")
        try:
            opcao = input("Escolha uma opção:")
        except ValueError:
            opcao = 0
        match opcao:
            case 1:
                print("A identificação de mesario ainda nao foi feita.")
            case 2:
                print("Zerezima ainda nao foi feita")
            case 3:
                print("voltando ao menu de votação...")
                



