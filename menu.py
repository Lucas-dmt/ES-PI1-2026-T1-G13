from datetime import datetime
import time
from conexaobd import executar  #importa a função de execução da conexaobd
from validacoes import validar_titulo
from validacoes import pedir_cpf
from validacoes import verificar_nome
from conexaobd import buscar   #importa a funcao buscar de conexaobd
from chave import gerar_chave #importa a funcao de geracao de chave de chave.py
from chave_protocolo import gerar_protocolo #importa a funcao de geracao de geracao de protocolo em protocolo.py
from auditoria import mostrar_logs, mostrar_protocolos, validar_protocolo, registrar_log

def menu_gerenciamento(): 
    """
    gerenciamento de eleitores e candidatos
    args:
        none
    returns:
        nones
    """
    opcao = 0  #comecamos a opcao com 0 so para entrar no menu pela primeira vez
    while opcao !=7: #menu continua abrindo enquanto o usuario nao escolher a opcao de voltar
        print("\n=== MENU GERENCIAMENTO ===")
        print("1 - Cadastrar eleitor")
        print("2 - Buscar eleitor")
        print("3 - Cadastrar candidato")
        print("4 - Buscar candidato")
        print("5 - Criar Partido")
        print("6 - Buscar Partido")
        print("7 - Voltar")
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
                cpf = pedir_cpf()
                prefixo_cpf = cpf[:4] #pega os 4 primeiros dígitos
                # ==== MESÁRIO ====
                mesario = input("Mesário s/n:").lower()
                if mesario == "s":
                    mesario = 1
                else:
                    mesario = 0
                chave = gerar_chave(nome_completo)
                             # A partir daqui até o print, o CPF é validado antes de ser salvado
                comando = "INSERT INTO eleitores (nome, titulo_eleitor, prefixo_cpf, cpf, mesario, chave_acesso_cifrada, ja_votou) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                valores = (nome_completo,titulo_eleitor, prefixo_cpf, cpf, mesario, chave, 0)
                executar(comando,valores)
                print("Cadastrado.")   
            case 2:
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
                    print("Mesário:", "Sim" if eleitor[5] else "Não")
                    print("Já votou:", "Sim" if eleitor[7] else "Não")
                else:
                    print("\n[!] Erro: Eleitor não cadastrado.")
            case 3:
         # ==== CADASTRO DE CANDIDATO ==== 
                nome_completo_candidato = input("Digite seu nome completo:")
                numero_candidato = int(input("Seu número para votação:"))
                id_partido = int(input("Informe o ID do partido:"))
                comando = "INSERT INTO candidatos (candidato ,numero_votacao ,id_partido) VALUES (%s, %s, %s)"
                valores = (nome_completo_candidato,numero_candidato,id_partido)
                executar(comando,valores)
 
                print("Cadastrado com sucesso!")
            case 4:
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
                else:
                    print("\n[!] Erro: Eleitor não cadastrado.")
            case 5:
             # ==== CRIAÇÃO DE PARTIDO ====
                nome_partido = input("Digite o nome do partido:")
                sigla_partido = input("Digite a sigla do partido:")
                comando = "INSERT INTO partidos (partido, sigla) VALUES (%s, %s)"
                valores = (nome_partido, sigla_partido)
                executar(comando, valores)
                print("Partido cadastrado com sucesso!")
            case 6:
             # ==== BUSCA DE PARTIDO ==== 
                sigla_partidoB = input("Digite a sigla do partido:")
                comando = "SELECT partido FROM partidos WHERE sigla = %s"
                valores = (sigla_partidoB,)
                resultado = buscar(comando, valores)
                if resultado:
                    print(f"Partido: {resultado[0]}")
                else:
                    print("\n[!] Erro: Partido não cadastrado.")
            case 7:
                print("Voltando ao menu principal...")
            case _:
                print("Opcao invalida.")
def menu_abrir_votacao(urna_aberta,registrar_log):
    """
    menu de abrir votação, identifica mesario e realiza a zerezima
    args:
        none
    returns:
        none
    """
    mesario_autenticado = False
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
                cpf = input("CPF do mesário:")
                comando = """ SELECT * FROM eleitores WHERE cpf = %s AND mesario = 1 """
                valores = (cpf,) 
                resultado = buscar(comando,valores)
                if resultado:
                    mesario_autenticado = True
                    print("Mesário autenticado.")
                else: 
                    print("Mesário não autorizado")
            case 2:
                # Impede zerézima sem mesário
                if not mesario_autenticado:
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

            case 3:
                print("Voltando ao menu de votacao...")
            case _:
                print("Opcao invalida.")
    return urna_aberta

def menu_encerramento(urna_aberta,registrar_log):
    if  urna_aberta == False:
        print("\nA urna já está fechada ou não foi aberta.")
        return urna_aberta
    
    executando = True
    while executando == True:
        print("\n=== MENU DE ENCERRAMENTO ===")
        print("1 - Iniciar Protocolo de Fechamento")
        print("2 - Voltar")
        try:
            opcao=int(input("digite 1 ou 2: "))
        except ValueError:
            print("Opção inválida. Voltando para o menu de votação...")
            return urna_aberta
    
        match opcao:
            case 1:
                try:
                    titulo = input("digite o título:")
                    prefixo_cpf = input("insira os 4 primeiros dígitos dpo cpf:")
                    chave = input("chave de acesso:")

                    comando = "SELECT chave_acesso_cifrada FROM eleitores WHERE titulo_eleitor = %s AND prefixo_cpf = %s AND mesario = 1 "           
                    valores = (titulo, prefixo_cpf)
                    resultado = buscar(comando, valores)

                    if resultado != None:
                        if resultado[0] == chave: 
                            print("Chave correta!")
                            confirmação = input("Deseja realmente encerrar a votação? (Sim/Não)")
                            if confirmação =='Sim':
                                segunda_chave = input("digite a chave novamente:")                        
                                if resultado[0] == segunda_chave:
                                    print("URNA ENCERRADA")
                                    urna_aberta=False
                                    executando = False
                                    menu_resultados()
                                    return urna_aberta
                                else:
                                    print("Erro. a chave está errada")
                                    return urna_aberta


                            elif confirmação == 'Não':
                                print("Operação cancelada.")                        
                                return urna_aberta  

                            else:
                                print("Resposta inválida. Operação cancelada.")
                                return urna_aberta          
                        else:
                            print("Chave incorreta.") 
                            return urna_aberta                   
                    else:
                        print("Mesário não encontrado ou sem permissão.")
                        return urna_aberta

                except ValueError:
                     print(f"Erro: Digite apenas números para Título e CPF.")
                     return urna_aberta
            case 2:
                print("Voltando para o menu de votação...")
                return urna_aberta

            case _:
                print("Opção inválida")
                return urna_aberta
    return urna_aberta
    
def menu_auditoria():
    """
    menu de auditoria da votação, exibe logs e protocolos
    args:
        none
    returns:
        none
    """
    opcao = 0

    while opcao != 4:

        print("\n=== AUDITORIA DA VOTACAO ===")

        print("1 - Exibir logs")
        print("2 - Exibir protocolos")
        print("3 - Validar protocolos") 
        print("4 - Voltar")

        opcao = int(input("\nEscolha uma opcao: "))

        match opcao:
            case 1:

                mostrar_logs()
        
            case 2:

                mostrar_protocolos()
                
            case 3:
        
                validar_protocolo()

            case 4:

                print("\nVoltando ao menu de votacao...")

                menu_votacao()

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
    urna_aberta = False
    opcao = 0
    while opcao != 5:
        print("\n=== MENU VOTACAO ===")
        print("1 - Votar")
        print("2 - Abrir sistema de votacao")
        print("3 - Auditoria da votacao")
        print("4 - Resultados da votacao")
        print("5 - Voltar")
        try:
            opcao = int(input("Escolha uma opcao: "))
        except ValueError:
            opcao = 0

        match opcao:
            case 1:
                if urna_aberta:
                    print("\n === VOTAR ===")
                    verificar_cpf = 0
                    while verificar_cpf == 0:
                        cpf =input("Seu CPF: ")
                        comando = "SELECT nome, ja_votou FROM eleitores WHERE cpf = %s"
                        resultado = buscar(comando, (cpf,))
                        if resultado == None:
                            print("CPF não encontrado. Tente novamente.")
                        elif resultado[1] == 1:
                            print(f"Eleitor {resultado[0]} já votou. Você não pode votar novamente.")
                            registrar_log()
                        else:
                            print(f"Bem-vindo, {resultado[0]}! Você pode votar agora.")
                            verificar_cpf = 1
                    verificar_chave = 0
                    while verificar_chave == 0:
                        chave = input("Digite sua chave de acesso: ")
                        comando = "SELECT chave_acesso_cifrada FROM eleitores WHERE cpf = %s"
                        resultado = buscar(comando, (cpf,))
                        if resultado and resultado[0] == chave:
                            print("Chave correta! Você pode votar.")
                            verificar_chave = 1
                        else:
                            print("Chave incorreta. Tente novamente.")
                    parte_final = 0
                    while parte_final == 0:
                        candidato = int(input("Insira o numero do candidato que voce deseja votar: "))
                        comando = "SELECT candidato FROM candidatos WHERE numero_votacao = %s"
                        resultado = buscar(comando, (candidato,))
                        if resultado:
                            parte_final = 1
                            comando = "UPDATE eleitores SET ja_votou = %s, candidato_votado = %s WHERE cpf = %s"
                            valores = (1, candidato, cpf)
                            executar(comando, valores)
                            print(f"Você votou no candidato: {resultado[0]}")
                            registrar_log()

                            protocolo = gerar_protocolo(candidato)
                        
                        else:
                            print("Candidato não encontrado. Tente novamente.")
                            registrar_log()

                    
                else:
                    print("A urna esta fechada, tente novamente mais tarde")
            case 2:
                urna_aberta = menu_abrir_votacao(urna_aberta)
            case 3:
                menu_auditoria()
            case 4:
                menu_resultados()
            case 5:
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
