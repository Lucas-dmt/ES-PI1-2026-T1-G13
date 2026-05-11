from datetime import datetime
import time
import random

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
