from datetime import datetime
import time
import random

auditoria = []

arquivo_log = "auditoria_log.txt"
arquivo_protocolos = "protocolos.txt"


# ========= SALVAR PROTOCOLO =========

def salvar_protocolo(protocolo):

    with open(arquivo_protocolos, "a", encoding="utf-8") as arquivo:

        arquivo.write(protocolo + "\n")


# ========= MOSTRAR PROTOCOLOS =========

def mostrar_protocolos():

    print("\nVerificando protocolos oficiais...")

    time.sleep(3)

    print("\n===== PROTOCOLOS DE VOTACAO =====\n")

    try:

        with open(arquivo_protocolos, "r", encoding="utf-8") as arquivo:

            protocolos = arquivo.readlines()

            if protocolos == []:

                print("Nenhum protocolo encontrado.")

            else:

                protocolos.sort()

                print("Protocolos registrados oficialmente:\n")

                for protocolo in protocolos:

                    print(protocolo.replace("\n", ""))

                print("\nAuditoria concluida com sucesso.")

    except FileNotFoundError:

        print("Arquivo oficial de protocolos nao encontrado.")


# ========= REGISTRAR LOG =========

def registrar_log(mensagem):

    horario = datetime.now().strftime("%H:%M:%S")

    with open(arquivo_log, "a", encoding="utf-8") as arquivo:

        arquivo.write(f"[{horario}] {mensagem}\n")

    auditoria.append(f"[{horario}] {mensagem}")


# ========= MOSTRAR LOGS =========

def mostrar_logs():

    print("\nAtualizando registros atuais...")

    time.sleep(3)

    print("\n===== LOGS =====\n")

    try:

        with open(arquivo_log, "r", encoding="utf-8") as arquivo:

            logs = arquivo.read()

            if logs == "":

                print("Nenhum log encontrado.")

            else:

                print(logs)

    except FileNotFoundError:

        print("Arquivo de logs nao encontrado.")


#============== VALIDAR PROTOCOLO ========= 

def validar_protocolo():

    print("\n===== VALIDACAO DE PROTOCOLO =====")

    protocolo_digitado = input("\nDigite o protocolo: ")

    try:

        with open(arquivo_protocolos, "r", encoding="utf-8") as arquivo:

            protocolos = arquivo.readlines()

            encontrados = 0

            for protocolo in protocolos:

                protocolo = protocolo.replace("\n", "")

                if protocolo == protocolo_digitado:

                    encontrados += 1

            if encontrados == 1:

                print("\nPROTOCOLO VALIDO")
                print("Nenhuma fraude encontrada.")

                registrar_log(
                    "AUDITORIA: Protocolo validado com sucesso."
                )

            elif encontrados > 1:

                print("\nALERTA DE FRAUDE")
                print("Protocolo duplicado encontrado.")

                registrar_log(
                    "ALERTA: Possivel fraude por protocolo duplicado."
                )

            else:

                print("\nPROTOCOLO INVALIDO")
                print("O protocolo nao existe na base oficial.")

                registrar_log(
                    "ALERTA: Tentativa de validacao de protocolo falso."
                )

    except FileNotFoundError:

        print("\nArquivo de protocolos nao encontrado.")


# ========= MENU AUDITORIA =========

def menu_auditoria():

    opcao = 0

    while opcao != 4:

        print("\n=== AUDITORIA DA VOTACAO ===")

        print("1 - Exibir logs")
        print("2 - Exibir protocolos")
        print("3 - Validar protocolos") 
        print("4 - Voltar")

        opcao = int(input("\nEscolha uma opcao: "))

        if opcao == 1:

            mostrar_logs()

        elif opcao == 2:

            mostrar_protocolos()

        elif opcao == 3:

            validar_protocolo()

        elif opcao == 4:

            print("\nVoltando ao menu de votacao...")

        else:
            print("\n Opçao invalida")

menu_votacao()
    
# ========= REGISTROS =========

registrar_log(
    "ABERTURA: Votação iniciada com sucesso. Total de votos zerado."
)

registrar_log(
    "ALERTA: Tentativa de voto duplo"
)

registrar_log(
    "ALERTA: Tentativa de acesso negado"
)

registrar_log(
    "SUCESSO: Voto realizado com sucesso"
)

registrar_log(
    "ENCERRAMENTO: Votação finalizada com sucesso."
)

if votos < 0:

    registrar_log(
        "ALERTA: Alteração suspeita nos votos"
    )

if protocolo not in protocolos:

    print("Protocolo inválido!")

    registrar_log(
        "ALERTA: Protocolo inválido detectado"
    )
    
# ========= GERAR PROTOCOLO TESTE =========

protocolo = gerar_protocolo(13)

salvar_protocolo(protocolo)

# ========= ABRIR MENU =========

menu_auditoria()
