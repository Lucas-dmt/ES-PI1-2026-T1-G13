import random

def gerar_protocolo(candidato):
    """
    Gera um código de protocolo de votação alfanumérico único para o eleitor.

    A função monta uma estrutura de recibo segura combinando o caractere fixo 'V', 
    duas letras aleatórias em caixa alta, o sufixo numérico do ano corrente, o 
    número identificador do candidato formatado com dois dígitos (ou '00' para nulo) 
    e um sufixo numérico aleatório de cinco dígitos.

    Requisitos Atendidos:
        - RF004.03: Geração de recibo e identificador único de votação.

    Args:
        candidato (str/int): O número de votação do candidato escolhido ou a string 'NULO'.

    Returns:
        protocolo(str): O código de protocolo gerado pelo sistema.
    """

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
