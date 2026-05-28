from datetime import datetime
import time
from conexaobd import buscar
from criptografia import descriptografar_hill
auditoria = []
protocolos = []

#========= SALVAR PROTOCOLO =========
def salvar_protocolo(protocolo):

    protocolos.append(protocolo)


#========= MOSTRAR PROTOCOLOS =========
def mostrar_protocolos():

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

    horario = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log = f"[{horario}] {mensagem}"

    auditoria.append(log)


#========= MOSTRAR LOGS =========
def mostrar_logs():

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