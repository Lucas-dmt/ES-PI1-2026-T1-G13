from datetime import datetime
import time
from conexaobd import buscar_tudo
from criptografia import descriptografar_hill

auditoria = []


#======= MOSTRAR PROTOCOLOS =========
def mostrar_protocolos():

   print("\n===== PROTOCOLOS =====\n")

   query = "SELECT protocolo_votacao_cifrado FROM votos"
   resultado = buscar_tudo(query)

   if not resultado:
       print("Nenhum protocolo encontrado.")
       return
   for linha in resultado:

       protocolo_cripto = linha[0]
       protocolo = descriptografar_hill(protocolo_cripto)

       print(protocolo)



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