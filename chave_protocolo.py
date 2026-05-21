import random

def gerar_protocolo(candidato):
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    protocolo = "V"

    for i in range(2):
        protocolo += letras[random.randint(0, 25)]

    protocolo += "26"
    protocolo += str(candidato)
    protocolo += str(random.randint(10000, 99999))

    return protocolo