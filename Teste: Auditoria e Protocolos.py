from datetime import datetime
import time import random

auditoria = []
arquivo_log = "auditoria_log.txt"

def registrar_log(mensagem):
    horario = datetime.now().strftime("%H:%M:%S")
    auditoria.append(f"[{horario}] {mensagem}")


#============================CASE 1:LOGS========================

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


# MENSAGEM FINAL

dias = 5

print(f"\nVocê ainda não votou.")
print(f"A votação acaba em {dias} dias.")




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

#=====VOTO REALIZADO COM SUCESSO===



#======ENCERRAMENTO DE VOTAÇAO======
registrar_log(
    "ENCERRAMENTO: Votação finalizada com sucesso."
)


#===============MANIPULACAO DE ARQUIVO=================

with open("auditoria_log.txt", "a") as arquivo:
    arquivo.write(f"[{horario}] {msg}" + "\n")

#===MANIPULACAO DE ARQUIVO PARA SALVAR PROTOCOLO===

def salvar_protocolo(protocolo):

    with open(ARQUIVO_PROTOCOLOS, "a", encoding="utf-8") as arquivo:
        arquivo.write(protocolo + "\n")



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

#=================OCORRÊNCIA DOS LOGS===========================

def exibir_logs():

    try:
        with open("logs.txt", "r", encoding="utf-8") as arquivo:

            print("\n===== LOGS DE OCORRÊNCIAS =====\n")
            if protocolos == []:

                    print("Nenhum protocolo encontrado.")

                else:

                    protocolos.sort()

                    for protocolo in protocolos:

                        print(protocolo.strip())

    except FileNotFoundError:
        print("Nenhum log encontrado.")

elif opcao == 3:

        print("\nVoltando ao menu principal...")

    else:

        print("\nOpcao invalida.")

