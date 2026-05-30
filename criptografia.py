conjunto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
k11 = 4
k12 = 3
k21 = 1
k22 = 2


ki11 = 22
ki12 = 21
ki21 = 7
ki22 = 8

def converter_texto_numero(texto):
    numeros = []
    for letra in texto:
        letra = letra.upper()
        if letra in conjunto:
            numeros.append(conjunto.index(letra))
    return numeros

def converter_numero_texto(numeros):
    texto = ""
    for numero in numeros:
        texto += conjunto[numero % len(conjunto)]
    return texto

def criptografar_hill(texto):

    numeros = converter_texto_numero(texto)
    if len(numeros) % 2 != 0:
        numeros.append(0)

    resultado = []
    for i in range (0, len(numeros), 2):
        x = numeros[i]
        y = numeros[i + 1]

        novo1 = (k11 * x + k12 * y) % 36
        novo2 = (k21 * x + k22 * y) % 36
 
        resultado.append(novo1)
        resultado.append(novo2)

    return converter_numero_texto(resultado)


def descriptografar_hill(texto_criptografado):
    """
    Reverte a Cifra de Hill aplicando a matriz inversa para restaurar o texto original.

    Consome o texto cifrado e aplica a multiplicação matricial sobre os blocos numéricos 
    utilizando os coeficientes inversos pré-calculados (ki11, ki12, ki21, ki22) sob 
    aritmética modular de base 36 para descriptografar os dados de forma precisa.

    Requisitos Atendidos:
        - RF005.04: Módulo Criptográfico - Engenharia reversa autorizada e decifração de dados.

    Args:
        texto_criptografado (str): O texto cifrado que será revertido.

    Returns:
        "converter_numero_texto(resultado)" (str): O texto original recuperado.
    """
    numeros = converter_texto_numero(texto_criptografado)
    
    resultado = []
    for i in range (0, len(numeros), 2):
        x = numeros[i]
        y = numeros[i + 1]

        original1 = (ki11 * x + ki12 * y) % 36
        original2 = (ki21 * x + ki22 * y) % 36
 
        resultado.append(original1)
        resultado.append(original2)

    return converter_numero_texto(resultado)
