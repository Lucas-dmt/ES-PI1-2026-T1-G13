from datetime import datetime
import time
import random


auditoria = []
arquivo_log = "auditoria_log.txt"
arquivo_protocolos = "protocolos.txt"


#=========GERAR PROTOCOLO DEPOIS DE VOTAR=================

def gerar_protocolo(candidato):

    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    letra1 = random.choice(letras) # Gera letra Ateatoria
    letra2 = random.choice(letras) # Gera letra Ateatoria

    numeros = random.randint(10000, 99999)

    protocolo = "V" + letra1 + letra2 + "26" + str(candidato) + str(numeros)

    return protocolo

#========MANIPULACAO DE ARQUIVO PARA SALVAR PROTOCOLO===

def salvar_protocolo(protocolo):

    with open(ARQUIVO_PROTOCOLOS, "a", encoding="utf-8") as arquivo:
        arquivo.write(protocolo + "\n")

protocolo = gerar_protocolo(22)

salvar_protocolo(protocolo)

print("\nProtocolo gerado:")
print(protocolo)


#============MOSTRAR PROTOCOLOS===========
def mostrar_protocolos():

    print("\nVerificando protocolos oficiais...")

    time.sleep(3)

    print("\n===== PROTOCOLOS DE VOTACAO =====\n")

    try:

        # Abre o arquivo de protocolos no modo leitura
        with open(arquivo_protocolos, "r", encoding="utf-8") as arquivo:

            # Le todas as linhas e guarda em uma lista
            protocolos = arquivo.readlines()

            # Verifica se nao existe nenhum protocolo
            if protocolos == []:

                print("Nenhum protocolo encontrado.")

            else:

                # Organiza os protocolos 
                protocolos.sort()

                print("Protocolos registrados oficialmente:\n")

                # Percorre protocolo por protocolo
                for protocolo in protocolos:

                    # Remove a quebra de linha (\n)
                    print(protocolo.replace("\n", ""))

                print("\nAuditoria concluida com sucesso.")

    except FileNotFoundError:

        print("Arquivo oficial de protocolos nao encontrado.")



#======================== MENU AUDITORIA ======================
def menu_auditoria():
        auditoria = 0

        while auditoria != 3:

            print("\n=== AUDITORIA DA VOTACAO ===")

            print("1 - Exibir logs")
            print("2 - Exibir protocolos")
            print("3 - Voltar")

            auditoria = int(input("\nEscolha uma opcao: "))

if auditoria == 1:

mostrar_logs()

elif auditoria == 2:
mostrar_protocolos()

elif auditoria == 3:
 print("\nVoltando ao menu principal...")

 else:
  print("\nOpcao invalida.")
#=========REGISTRO DE LOGS==============================
def registrar_log(mensagem):
    horario = datetime.now().strftime("%H:%M:%S")

with open("auditoria_log.txt", "a") as arquivo:
    arquivo.write(f"[{horario}] {mensagem}" + "\n")

    auditoria.append(f"[{horario}] {mensagem}")


#=========MOSTRAR LOGS DE OCORRÊNCIA========    
  def mostrar_logs():

    print("\nAtualizando registros atuais...")

    time.sleep(3)

    print("\n===== LOGS =====")

    try:

        with open("logs.txt", "r", encoding="utf-8") as arquivo:

            logs = arquivo.read()

            if logs == "":
                print("Nenhum log encontrado.")

            else:
                print(logs)

    except FileNotFoundError:

        print("Arquivo de logs nao encontrado.")


#=======ABERTURA=======

registrar_log(
    "ABERTURA: Votação iniciada com sucesso. Total de votos zerado."
)

#========VOTO DUPLO===

registrar_log(
    "ALERTA: Tentativa de voto duplo"
)

#=======ACESSO NEGADO===

registrar_log(
    "ALERTA: Tentativa de acesso negado"
)

# ============ VOTO REALIZADO =============

registrar_log(
    "SUCESSO: Voto realizado com sucesso"
)

#======ENCERRAMENTO DE VOTAÇAO======
registrar_log(
    "ENCERRAMENTO: Votação finalizada com sucesso."
)

menu_principal()
