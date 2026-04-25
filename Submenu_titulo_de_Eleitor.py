def menu_eleitor():

while opçao != 4:
    print("\n===== SISTEMA DE VOTAÇÃO =====")
    print("1 - Cadastrar eleitor")
    print("2 - Votar")
    print("3 - Consultar eleitor")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        votar()      #alterar o votar() para outro menu de votação existente
    elif opcao == "3":
        consultar()
    elif opcao == "4":
        print("Encerrando...")
        break

menu_principal()
    else:
        print("Opção inválida ❌")
   try: 
        opcao = int(input("Escolha uma opcao: "))
   except ValueError: 
        opçao = 0
