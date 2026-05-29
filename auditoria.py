from datetime import datetime
import time
from conexaobd import buscar
from criptografia import descriptografar_hill
auditoria = []
protocolos = []

#========= SALVAR PROTOCOLO =========
def salvar_protocolo(protocolo):
    """
    Armazena temporariamente um protocolo de votação na lista de controle em memória.

    Requisitos Atendidos:
        - RF007.01: Módulo Auditoria - Registro de sessões de protocolos gerados.

    Args:
        protocolo (str): Código identificador do protocolo a ser armazenado.

    Returns:
        None
    """

    protocolos.append(protocolo)


#========= MOSTRAR PROTOCOLOS =========
def mostrar_protocolos():
    """
    Recupera, decifra e exibe todos os protocolos oficiais armazenados na base de dados.

    A função consome os dados do banco de dados, decodifica cada registro 
    criptografado via Cifra de Hill inversa e realiza uma listagem complementar 
    ordenada dos protocolos retidos em memória ativa.

    Requisitos Atendidos:
        - RF007.02: Módulo Auditoria - Descriptografia e conciliação de protocolos.

    Returns:
        None
    """

    print("\nVerificando protocolos oficiais...")

    comando = "SELECT protocolo_votacao_cifrado FROM votos"
    resultados = buscar(comando, [])  # Busca os protocolos cifrados no banco de dados

    if resultados is not None:
        for resultado in resultados:
            protocolo_cifrado = resultado[0]
            protocolo_decifrado = descriptografar_hill(protocolo_cifrado)  # Decifra o protocolo usando a chave inversa
            print(f"Protocolo encontrado: {protocolo_decifrado}")
    else:
        print("Nenhum protocolo encontrado")


    time.sleep(2)

    print("\n===== PROTOCOLOS DE VOTACAO =====\n")

    if protocolos == []:

        print("Nenhum protocolo registrado.")

    else:

        protocolos_ordenados = sorted(protocolos)

        print("Protocolos registrados oficialmente:\n")

        for protocolo in protocolos_ordenados:

            print(protocolo)

        print("\nAuditoria concluida com sucesso.")


#========= REGISTRAR LOG =========
def registrar_log(mensagem):
     """
    Gera e insere uma entrada de dados com data e hora na lista de auditoria.

    Requisitos Atendidos:
        - RF007.03: Módulo Auditoria - Captura cronológica de eventos críticos do sistema.

    Args:
        mensagem (str): Descrição do evento ou alerta a ser registrado.

    Returns:
        None
    """

    horario = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log = f"[{horario}] {mensagem}"

    auditoria.append(log)


#========= MOSTRAR LOGS =========
def mostrar_logs():
    """
    Exibe em ordem cronológica todos os eventos de log capturados em memória.

    Requisitos Atendidos:
        - RF007.04: Módulo Auditoria - Interface de inspeção visual de rastros e alertas.

    Returns:
        None
    """

    print("\nAtualizando registros atuais...")

    time.sleep(2)

    print("\n===== LOGS =====\n")

    if auditoria == []:

        print("Nenhum log encontrado.")

    else:

        for log in auditoria:

            print(log)


#========= MENU AUDITORIA =========
def menu_auditoria():
    """
    É o painel de navegação secundário para operação do módulo de auditoria.

    Gerencia o fluxo de telas permitindo que o operador inspecione logs de acesso 
    ou faça o batimento de protocolos oficiais antes de retornar ao menu anterior.

    Requisitos Atendidos:
        - RF007.05: Módulo Auditoria - Painel de controle de rotinas de auditoria.

    Returns:
        None
    """

    opcao = 0

    while opcao != 3:

        print("\n=== AUDITORIA DA VOTACAO ===")

        print("1 - Exibir logs")
        print("2 - Exibir protocolos")
        print("3 - Voltar")

        try:
            opcao = int(input("\nEscolha uma opcao: "))
        except ValueError:
            opcao = 0

        if opcao == 1:

            mostrar_logs()

        elif opcao == 2:

            mostrar_protocolos()

        elif opcao == 3:

            print("\nVoltando ao menu de votacao...")

        else:

            print("\nOpcao invalida")
