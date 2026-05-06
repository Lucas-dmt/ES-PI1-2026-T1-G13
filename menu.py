from conexaobd import executar  #importa a função de execução da conexaobd
from conexaobd import buscar
from chave import gerar_chave
from validacoes import validar_cpf
from validacoes import validar_titulo
from validacoes import verificar_nome
def menu_gerenciamento(): 
    """
    gerenciamento de eleitores e candidatos
    args:
        none
    returns:
        nones
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
        match opcao:
            case 1:
                nome_completo = input("Digite seu nome completo:")
                verificar_nome(nome_completo)
                titulo_eleitor = input("Digite o Título de Eleitor:")
                validar_titulo(titulo_eleitor)
                cpf = input("digite seu CPF:")
                prefixo_cpf = cpf[:4] #pega os 4 primeiros dígitos
                validar_cpf(cpf)
                # ==== MESÁRIO ====
                mesario = input("Mesário s/n:").lower()
                if mesario == "s":
                    mesario = 1
                else:
                    mesario = 0
                chave = gerar_chave()
                             # A partir daqui até o print, o CPF é validado antes de ser salvado
                comando = "INSERT INTO eleitores (nome, titulo_eleitor, prefixo_cpf, cpf, mesario, chave_acesso_cifrada, ja_votou) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                valores = (nome_completo,titulo_eleitor, prefixo_cpf, cpf, mesario, chave, 0)
                executar(comando,valores)
                print("Cadastrado.")   
            case 2:
                print("Listagem de eleitores ainda nao foi feita.")
            case 3:
             # ==== BUSCAR ELEITOR ====
                cpf_inserido = input("Digite o seu CPF:")
                comando = "SELECT * FROM eleitores WHERE cpf = %s"
                valores = (cpf_inserido,)
                eleitor = buscar(comando, valores)
                if eleitor:
                    print("\n--- ELEITOR ENCONTRADO ---")
                    print(f"Nome: {eleitor[1]}")
                    print(f"Título de Eleitor: {eleitor[2]}")
                    print(f"CPF: {eleitor[3]}")
                    print("Já votou:", "Sim" if eleitor[2] else "Não")
                else:
                    print("\n[!] Erro: Eleitor não cadastrado.")
            case 4:
                print("Edicao de eleitor ainda nao foi feita.")
            case 5:
                print("Remocao de eleitor ainda nao foi feita.")
            case 6:
         # ==== CADASTRO DE CANDIDATO ==== 
                nome_completo_candidato = input("Digite seu nome completo:")
                numero_candidato = int(input("Seu número para votação:"))
                id_partido = int(input("Informe o ID do partido:"))
                comando = "INSERT INTO candidatos (candidato ,numero_votacao ,id_partido) VALUES (%s, %s, %s)"
                valores = (nome_completo_candidato,numero_candidato,id_partido)
                executar(comando,valores)
 
                print("Cadastrado com sucesso!")
            case 7:
                print("Listagem de candidatos ainda nao foi feita.")
            case 8:
             # ==== BUSCA DE CANDIDATO ====
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