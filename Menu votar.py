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
