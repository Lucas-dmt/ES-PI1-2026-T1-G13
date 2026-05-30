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
    #Conjunto de letras que serão usadas na geração aleatória
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #Todo o protocolo começa com a letra V(votação)
    protocolo = "V"

    #Adiciona duas letras aleatórias ao protoclo
    for i in range(2):
        protocolo += letras[random.randint(0, 25)]

    #Adiciona o ano dde eleição (2026 -> "26")
    protocolo += "26"

    #Verifica se o voto foi NULO    
    if candidato == "NULO":
        #Votos nulos recebem código "00"
        protocolo += "00"

    else:
        #Converte o número do candidato para texto
        candidato = str(candidato)
        #Garante que o número tenha 2 dígitos 
        #Exemplo: 5 -> 05
        if len(candidato) == 1:
            protocolo += "0" + candidato
        else:
            protocolo += candidato

    #Adiciona um número aleatório de 5 dígitos
    #Para aumentar a unicidade do protocolo
    protocolo += str(random.randint(10000, 99999))

    # retorna o protocolo completo
    return protocolo
