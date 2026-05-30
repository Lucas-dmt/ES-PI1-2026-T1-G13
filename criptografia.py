#Conjunto de caracteres permitidos na criptografia
#26 letras + 10 números = 36 caracteres
conjunto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

#Matriz de criptografia
# | 4 3 |
# | 1 2 |
k11 = 4
k12 = 3
k21 = 1
k22 = 2

#Matriz inversa utilizada na descriptografia
# | 22 21 |
# |  7  8 |
ki11 = 22
ki12 = 21
ki21 = 7
ki22 = 8

def converter_texto_numero(texto):
    """
    Converte uma cadeia de caracteres em uma lista de índices numéricos baseados no alfabeto definido.

    Parte integrante do processo de preparação de dados para operações matemáticas. 
    Trata os caracteres em caixa alta e filtra apenas as entradas contidas no conjunto permitido.

    Requisitos Atendidos:
        - RF005.01: Módulo Criptográfico - Codificação de caracteres em índices numéricos.

    Args:
        texto (str): O texto ou sequência a ser convertida.

    Returns:
        numeros (list): Lista de inteiros representando as posições dos caracteres no conjunto.
    """
    numeros = []
    #Percorre cada caractere do texto 
    for letra in texto:
        #Padroniza para maiúsculo 
        letra = letra.upper()
        #Verifica se o caractere existe no conjunto permitido
        if letra in conjunto:
            #Saçva a posição do caractere
            numeros.append(conjunto.index(letra))
    return numeros

def converter_numero_texto(numeros):
    """
    Reverte uma lista de índices numéricos de volta para uma cadeia de caracteres de texto.

    Aplica a operação aritmética de módulo com base no tamanho do alfabeto para garantir 
    que o índice calculado mapeie corretamente um caractere válido do conjunto.

    Requisitos Atendidos:
        - RF005.02: Módulo Criptográfico - Decodificação de índices numéricos para texto.

    Args:
        numeros (list): Lista de inteiros contendo os índices a serem decodificados.

    Returns:
        texto (str): Cadeia de caracteres gerada a partir dos índices numéricos.
    """
    texto = ""
    #Percorre cada número recebido
    for numero in numeros:
        #Converte o índice novamente para caractere
        texto += conjunto[numero % len(conjunto)]
    return texto

def criptografar_hill(texto):
    """
    Aplica o algoritmo da Cifra de Hill para criptografar uma string de texto puro.

    Converte o texto em blocos numéricos pareados (tamanho 2) e realiza a multiplicação 
    vetorial-matriz utilizando os coeficientes de criptografia estabelecidos (k11, k12, k21, k22) 
    sob aritmética modular de base 36. Caso a cadeia possua comprimento ímpar, realiza o ajuste (padding).

    Requisitos Atendidos:
        - RF005.03: Módulo Criptográfico - Ofuscação de dados e segurança da informação.

    Args:
        texto (str): O texto original a ser cifrado.

    Returns:
        "converter_numero_texto(resultado)" (str): Texto cifrado resultante da transformação matricial.
    """
    #Converte texto em números
    numeros = converter_texto_numero(texto)
    # Se a quantidade de caracteres for ímpar,
    # adiciona um caractere de preenchimento
    if len(numeros) % 2 != 0:
        numeros.append(0)

    resultado = []
    # Processa os números em blocos de 2
    for i in range (0, len(numeros), 2):

        x = numeros[i]
        y = numeros[i + 1]
        # Multiplicação da matriz de criptografia
        novo1 = (k11 * x + k12 * y) % 36
        novo2 = (k21 * x + k22 * y) % 36
 
        resultado.append(novo1)
        resultado.append(novo2)
      # Converte os números criptografados para texto
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
    # Converte texto cifrado para números
    numeros = converter_texto_numero(texto_criptografado)
    
    resultado = []
    # Processa em blocos de 2 caracteres
    for i in range (0, len(numeros), 2):

        x = numeros[i]
        y = numeros[i + 1]
        # Multiplicação pela matriz inversa
        original1 = (ki11 * x + ki12 * y) % 36
        original2 = (ki21 * x + ki22 * y) % 36
 
        resultado.append(original1)
        resultado.append(original2)
        
    # Reconstrói o texto original
    return converter_numero_texto(resultado)
