import time
import random

def gerar_chave(nome):
    """
    Gera uma chave de acesso alfanumérica única baseada no nome do eleitor.

    A função extrai as primeiras letras do nome e sobrenome, converte para caixa alta 
    e concatena com um sufixo numérico aleatório de quatro dígitos. Na sequência, 
    fornece uma interface de redirecionamento para os módulos de votação ou gerenciamento.

    Requisitos Atendidos:
        - RF008.01: Módulo de Acesso - Geração de credencial de identificação.

    Args:
        nome (str): O nome completo do eleitor cadastrado.

    Returns:
        str: A chave de acesso gerada pelo sistema.
    """

    print("\nCadastro de título e CPF registrado")
    print("Estamos gerando sua chave...")

    time.sleep(5)

    letras = nome[0] + nome[1]# as 2 primeiras letras do nome

    for i in range(len(nome)):
        if nome[i] == " ":
            letras += nome[i + 1]# soma as 2 primeiras letras,pula o espaço e junta a primeira letra do sobrenome depois do i espaço
            break
     
    chave = letras.upper() + f"{random.randint(1000, 9999)}"

    print("Sua chave é:", chave)

    x = 0

    while x != 2 and x != 11:
        x = int(input("\nDigite 2 para votação ou 11 para gerenciamento: "))

        if x == 2:
            print("Indo para votação...")
            menu_votacao()

        elif x == 11:
            print("Voltando ao gerenciamento...")
            menu_gerenciamento()

        else:
            print("Opção inválida\n")

    return chave

def menu_votacao():
    print("Menu votação")

def menu_gerenciamento():
    """
    Provê o painel de navegação e as opções de administração e gerenciamento do sistema.

    Requisitos Atendidos:
        - RF008.03: Módulo de Acesso - Interface do menu de gerenciamento.

    Returns:
        None
    """
    print("Menu gerenciamento")
