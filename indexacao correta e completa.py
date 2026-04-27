 import random
 import time
def gerar_chave():
    return f"{random.randint(0,999999):06}"
def menu_gerenciamento(): 
    """
    gerenciamento de eleitores e candidatos
    args:
        none
    returns:
        none
    """
    opcao = 0  #comecamos a opcao com 0 so para entrar no menu pela primeira vez
    while opcao !=11: #menu continua abrindo enquanto o usuario nao escolher a opcao de voltar
        print("\n=== MENU GERENCIAMENTO ===")
        print("1 - Cadastrar eleitor")
 
        print("2 - Listar eleitores")
        print("3 - Buscar eleitor")
        print("4 - Editar eleitor")
        print("5 - Remover eleitor")
        print("6 - Cadastrar candidato")
        print("7 - Listar candidatos")
        print("8 - Buscar candidato")
        print("9 - Editar candidato")
        print("10 - Remover candidato")
        print("11 - Voltar")

        try: #tenta transformar o que o usuario digitou em numero
            opcao = int(input("Escolha uma opcao: "))
        except ValueError: #se o usuario digitar letra ou algo invalido, a opcao vira 0 (ValueError)
            opcao = 0

        #a partir daqui o programa verifica qual numero foi escolhido   
        from conexaobd import executar  #importa a função de execução da conexaobd
        match opcao:
            case 1:
                nome_completo = input("Digite seu nome completo:")
                titulo_eleitor = int(input("Digite o número do título:"))
                cpf = input("Digite seu CPF:")
                prefixo_cpf = cpf[:4] #pega os 4 primeiros dígitos
             # ==== MESÁRIO ====
                mesario = input("Mesário s/n:").lower()
                if mesario == "s":
                    mesario = 1
                else:
                    mesario = 0
#=============== VALIDAÇÃO DO TITULO DE ELEITOR ========== 
def campo_vazio(texto):
    return texto == ""

def apenas_numeros(texto):
    for c in texto:
        if c < "0" or c > "9":
            return False
    return True


def todos_iguais(texto):
    return all(c == texto[0] for c in texto)


def sequencia_crescente(texto):
    for i in range(len(texto) - 1):
        if int(texto[i]) + 1 != int(texto[i + 1]):
            return False
    return True


titulo_valido = False

while not titulo_valido:

    # 1. tamanho
    if len(titulo_eleitor) != 12:
        print("Erro: precisa ter exatamente 12 dígitos.\n")
        continue

    # 2. apenas números 
    if not apenas_numeros(titulo_eleitor):
        print("Erro: o título deve conter apenas números.\n")
        continue

    # 3. não pode ser tudo igual (ex: 111111111111)
    if todos_iguais(titulo_eleitor):
        print("Erro: número inválido (todos os dígitos são iguais).\n")
        continue

    # 4. não pode ser sequência óbvia (123456789012)
    if sequencia_crescente(titulo_eleitor):
        print("Erro: número inválido (sequência crescente).\n")
        continue

    # 5. UF do título: posições 9 e 10
    uf = int(titulo_eleitor[8:10])
    if uf < 1 or uf > 28:
        print("Erro: código de estado inválido no título.\n")
        continue
    #6. não pode ter campo vazio
    if campo_vazio(titulo_eleitor):
            print("Erro: o título não pode estar vazio.\n")
            continue
 
    # Verifica se o campo foi validado
    if titulo_valido:
          print("\nTítulo válido com sucesso!")
          print(cpf)

    else:

        titulo_valido = True

        for c in titulo_eleitor:
            if c < "0" or c > "9":
                titulo_valido = False

        if not titulo_valido:
            print("Título inválido: só pode conter números")

        else:

            numero = titulo_eleitor[:8] # 8 primeiros digitos
            uf = titulo_eleitor[8:10] # codigo do estado com 2 digitos
            digitos = titulo_eleitor[10:12] #ultimos 2 digitos (verificadores)

             #============ CALCULO DO PRIMEIRO DIGITO ========
            pesos1 = [2, 3, 4, 5, 6, 7, 8, 9]

            soma = 0
            for i in range(8):
                soma += int(numero[i]) * pesos1[i]

            resto = soma % 11
            dv1 = 0 if resto == 10 else resto

             #============ CALCULO DO SEGUNDO DIGITO ========
            soma2 = (int(uf[0]) * 7) + (int(uf[1]) * 8) + (dv1 * 9)

            resto2 = soma2 % 11
            dv2 = 0 if resto2 == 10 else resto2
             #============= VALIDAÇÃO FINAL =========
            if digitos == str(dv1) + str(dv2):
                print("Título válido")
                titulo_valido = True
            else:
                print("Título inválido: dígitos não conferem")
                titulo_valido = False
