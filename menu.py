def menu_gerenciamento():
    """
    gerenciamento de candidatos e eleitores

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
