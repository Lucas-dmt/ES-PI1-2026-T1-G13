from datetime import datetime
import time
import random


auditoria = []
arquivo_log = "auditoria_log.txt"
ARQUIVO_PROTOCOLOS = "protocolos.txt"


#=========GERAR PROTOCOLO DEPOIS DE VOTAR=================


def gerar_protocolo(candidato):

    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    letra1 = random.choice(letras) # Gera letra Ateatoria
    letra2 = random.choice(letras) # Gera letra Ateatoria

    numeros = random.randint(10000, 99999)

    protocolo = "V" + letra1 + letra2 + "26" + str(candidato) + str(numeros)

    return protocolo

#===MANIPULACAO DE ARQUIVO PARA SALVAR PROTOCOLO===

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

                print("\n===== PROTOCOLOS =====\n")

                try:

                    with open("protocolos.txt", "r", encoding="utf-8") as arquivo:

                        protocolos = arquivo.readlines() 

                        print(protocolos)

                        if protocolos == []: #Le todas as linhas do arquivo e guardar em uma lista.


                            print("Nenhum protocolo encontrado.")

                        else:
                              
                            protocolos.sort() #Ordena a ordem do protocolo 

                            for protocolo in protocolos: #Percorre linha por linha.

                                print(protocolo.replace("\n", "")) #Remove apenas a quebra de linha:

                except FileNotFoundError:
                    print("Arquivo de protocolos nao encontrado.")



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

#=========REGISTRO DE LOGS==============================
def registrar_log(mensagem):
    horario = datetime.now().strftime("%H:%M:%S")

with open("auditoria_log.txt", "a") as arquivo:
    arquivo.write(f"[{horario}] {msg}" + "\n")

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

# ============ VOTO REALIZADO =============

registrar_log(
    "SUCESSO: Voto realizado com sucesso"
)

#======ENCERRAMENTO DE VOTAÇAO======
registrar_log(
    "ENCERRAMENTO: Votação finalizada com sucesso."
)


elif opcao == 3:

        print("\nVoltando ao menu principal...")

menu_principal()

    else:

        print("\nOpcao invalida.")

