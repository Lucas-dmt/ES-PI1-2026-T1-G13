from datetime import datetime
import time
import random

import time

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

            # =========================
            # LOGS
            # =========================

            if auditoria == 1:

                print("\nAtualizando registros atuais...")

                time.sleep(2)

                print("\n===== LOGS =====\n")

                try:

                    with open("logs.txt", "r", encoding="utf-8") as arquivo:

                        logs = arquivo.read()

                        if logs == "":

                            print("Nenhum log encontrado.")

                        else:

                            print(logs)

                except:

                    print("Arquivo de logs nao encontrado.")

                print("\nVoce ainda nao votou.")
                print("A votacao acaba em 5 dias.")

            # =========================
            # PROTOCOLOS
            # =========================

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

            # =========================
            # VOLTAR
            # =========================

            elif auditoria == 3:

                print("\nVoltando...")

            else:

                print("\nOpcao invalida.")

    # =========================
    # SAIR
    # =========================

    elif opcao == 4:

        print("\nSaindo do sistema...")

    else:

        print("\nOpcao invalida.")



auditoria = []

arquivo_log = "auditoria_log.txt"

ARQUIVO_PROTOCOLOS = "protocolos.txt"


# =========================
# REGISTRAR LOG
# =========================

def registrar_log(mensagem):

    horario = datetime.now().strftime("%H:%M:%S")

    with open(arquivo_log, "a", encoding="utf-8") as arquivo:

        arquivo.write(f"[{horario}] {mensagem}\n")


# =========================
# ABERTURA
# =========================

registrar_log(
    "ABERTURA: Votação iniciada com sucesso. Total de votos zerado."
)

# =========================
# VOTO DUPLO
# =========================

registrar_log(
    "ALERTA: Tentativa de voto duplo"
)

# =========================
# ACESSO NEGADO
# =========================

registrar_log(
    "ALERTA: Tentativa de acesso negado"
)

# =========================
# VOTO REALIZADO
# =========================

registrar_log(
    "SUCESSO: Voto realizado com sucesso"
)

# =========================
# ENCERRAMENTO
# =========================

registrar_log(
    "ENCERRAMENTO: Votação finalizada com sucesso."
)

# =========================
# MOSTRAR LOGS
# =========================

print("Atualizando registros atuais...")

time.sleep(3)

print("\n===== LOGS =====")

try:

    with open(arquivo_log, "r", encoding="utf-8") as arquivo:

        logs = arquivo.read()

        if logs == "":

            print("Nenhum log encontrado.")

        else:

            print(logs)

except:

    print("Arquivo de logs não encontrado.")

# =========================
# MENSAGEM FINAL
# =========================

dias = 5

print(f"\nVocê ainda não votou.")
print(f"A votação acaba em {dias} dias.")

# =========================
# GERAR PROTOCOLO
# =========================

def gerar_protocolo(candidato):

    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    letra1 = random.choice(letras)
    letra2 = random.choice(letras)

    numeros = random.randint(10000, 99999)

    protocolo = "V" + letra1 + letra2 + "26" + str(candidato) + str(numeros)

    return protocolo


# =========================
# SALVAR PROTOCOLO
# =========================

def salvar_protocolo(protocolo):

    with open(ARQUIVO_PROTOCOLOS, "a", encoding="utf-8") as arquivo:

        arquivo.write(protocolo + "\n")


# =========================
# EXEMPLO
# =========================

protocolo = gerar_protocolo(13)

salvar_protocolo(protocolo)

print("\nProtocolo gerado:")
print(protocolo)
