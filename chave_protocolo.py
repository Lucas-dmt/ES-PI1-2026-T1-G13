import random
import time


def gerar_protocolo(candidato):

    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    protocolo = "V"

    # Gera 2 letras aleatórias
    for i in range(2):
        protocolo += letras[random.randint(0, 25)]

    # Adiciona Ano 26
    protocolo += "26"

    # Adiciona número do candidato
    protocolo += str(candidato)

    # Adiciona números aleatórios de 5 digitos
    protocolo += str(random.randint(10000, 99999))

    return protocolo


candidato = int(input("Digite o numero do candidato: "))

print("Confirmando voto...")

time.sleep(5)

protocolo = gerar_protocolo(candidato)

print("Voto realizado com sucesso!")
print("Seu protocolo é:", protocolo)
