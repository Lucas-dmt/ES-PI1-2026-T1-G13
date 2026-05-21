def menu_abrir_votacao(urna_aberta):
    """
    menu de abrir votação, identifica mesario e realiza a zerezima
    args:
        none
    returns:
        none
    """
    mesario_autenticado = False
    opcao = 0
    while opcao != 2:
        print("\n=== ABRIR SISTEMA DE VOTACAO ===")
        print("1 - Abrir sistema")
        print("2 - Voltar")
        try:
            opcao = int(input("Escolha uma opcao: "))
        except ValueError:
            opcao = 0

        match opcao:
            case 1:
                if urna_aberta:
                    print("A urna já está aberta.")
                else:
                    titulo = input("Digite o título do mesário:")
                    prefixo_cpf = input("4 primeiros dígitos do CPF do mesário:")
                    chave = input("Chave de acesso:")
                    comando = """ SELECT * FROM eleitores WHERE titulo_eleitor = %s AND prefixo_cpf = %s AND chave_acesso_cifrada = %s AND mesario = 1 """
                    valores = (titulo,prefixo_cpf,chave) 
                    resultado = buscar(comando,valores)
                    if resultado:
                        mesario_autenticado = True
                        print("Mesário autenticado.")
                    
                        # Impede zerézima sem mesário
                    if not resultado:
                        mesario_autenticado = False
                        print("Autentique um mesario primeiro.")
                        continue
                    # Impede abrir novamente
                    if urna_aberta:
                        print("A urna já esta aberta.")
                        continue
                    comando = """ SELECT COUNT(*) FROM eleitores WHERE ja_votou = 1 """
                    resultado = buscar(comando, ())
                    votos = resultado[0]
                    print("\n=== ZEREZIMA ===")
                    print(f"Total de votos registrados: {resultado[0]}")
                    
                    if votos > 0:
                        print("\nHouve uma anomalia no sistema, a urna não pode ser aberta.")
                    else:
                        urna_aberta = True
                        print("\nUrna liberada para votação.")
                    
            case 2:
                print("Voltando ao menu de votacao...")
            case _:
                print("Opcao invalida.")
    return urna_aberta