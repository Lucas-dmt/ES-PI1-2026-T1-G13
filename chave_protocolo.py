import random

def gerar_protocolo(candidato):

    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    protocolo = "V"

    for i in range(2):
        protocolo += letras[random.randint(0, 25)]

    protocolo += "26"

    if candidato == "NULO":
        protocolo += "00"
    else:
        candidato = str(candidato)

        if len(candidato) == 1:
            protocolo += "0" + candidato
        else:
            protocolo += candidato

    protocolo += str(random.randint(10000, 99999))

    return protocolo
