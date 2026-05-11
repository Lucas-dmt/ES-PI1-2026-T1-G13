from datetime import datetime
import time import random

auditoria = []
arquivo_log = "auditoria_log.txt"
ARQUIVO_PROTOCOLOS = "protocolos.txt"

#===============MANIPULACAO DE ARQUIVO=================

with open("auditoria_log.txt", "a") as arquivo:
    arquivo.write(f"[{horario}] {msg}" + "\n")

#===MANIPULACAO DE ARQUIVO PARA SALVAR PROTOCOLO===

def salvar_protocolo(protocolo):

    with open(ARQUIVO_PROTOCOLOS, "a", encoding="utf-8") as arquivo:
        arquivo.write(protocolo + "\n")


opcao = 0

while opcao != 4:

    print("\n===== SISTEMA DE VOTACAO =====")

    print("1 - Votar")
    print("2 - Resultado")
    print("3 - Auditoria")
    print("4 - Sair")

    opcao = int(input("\nEscolha: "))

    elif opcao == 3:

        auditoria = 0

        while auditoria != 3:

            print("\n=== AUDITORIA DA VOTACAO ===")

            print("1 - Exibir logs")
            print("2 - Exibir protocolos")
            print("3 - Voltar")

            auditoria = int(input("\nEscolha uma opcao: "))


#============================CASE 1:LOGS========================

if auditoria == 1:
    print("Atualizando registros atuais...")

# Espera 3 segundos
time.sleep(3)

print("\n===== LOGS =====")
try:

    with open("logs.txt", "r", encoding="utf-8") as arquivo:

        logs = arquivo.read()

        if logs == "":
            print("Nenhum log encontrado.")

        else:
            print(logs)

except:

    print("Arquivo de logs não encontrado.")

dias = 5

print(f"\nAVISO: Você ainda não votou, restam {dias} dias para a votação acabar.")



#=========REGISTRO DE LOGS==============================
def registrar_log(mensagem):
    horario = datetime.now().strftime("%H:%M:%S")
    auditoria.append(f"[{horario}] {mensagem}")

#=======ABERTURA=======

from auditoria import registrar_log

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

#======ENCERRAMENTO DE VOTAÇAO======
registrar_log(
    "ENCERRAMENTO: Votação finalizada com sucesso."
)

# ================PROTOCOLOS========================

 elif auditoria == 2:

                print("\nVerificando protocolos oficiais...")

                time.sleep(2)

                print("\n===== PROTOCOLOS =====\n")

                try:

                    with open("protocolos.txt", "r", encoding="utf-8") as arquivo:

                        protocolos = arquivo.readlines()

                        if protocolos == []:

                            print("Nenhum protocolo encontrado.")

                        else:

                            protocolos.sort()

                            for protocolo in protocolos:

                                print(protocolo.strip())

                except:

                    print("Arquivo de protocolos nao encontrado.")


#=========GERAR PROTOCOLO DEPOIS DE VOTAR=================


def gerar_protocolo(candidato):

    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    letra1 = random.choice(letras)
    letra2 = random.choice(letras)

    numeros = random.randint(10000, 99999)

    protocolo = "V" + letra1 + letra2 + "26" + str(candidato) + str(numeros)

    return protocolo


# EXEMPLO

print(gerar_protocolo(13))


elif opcao == 3:

        print("\nVoltando ao menu principal...")

    else:

        print("\nOpcao invalida.")

