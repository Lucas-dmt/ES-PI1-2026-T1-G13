### VALIDAÇÃO DO CPF ###
def validar_cpf(cpf):
    """
    Executa a validação estrutural e matemática de um número de CPF.

    A função valida a string de entrada verificando se ela possui exatamente 
    11 dígitos numéricos, descarta sequências de números repetidos e calcula 
    os dois dígitos verificadores (DV) por meio de somatórios ponderados e 
    operação de resto de divisão por 11 (Módulo 11).

    Requisitos Atendidos:
        - RF001.02: Validação matemática do CPF aceitando apenas números reais.

    Args:
        cpf : Cadeia de caracteres contendo o CPF a ser validado.

    Returns:
        bool: True se o CPF for matematicamente válido, False caso contrário.
        0 ou first verify: decide o primeiro dígito verificador
        0 ou second_verify: decide o segundo dígito verificador
    """
    cont = 0
    # aqui ele verifica se todos os caracteres são números, 11 dígitos
    for k in range(len(cpf)):
        if cpf[k].isdigit():
            cont += 1

    if len(cpf) != 11 and cont < len(cpf):
        print("O cpf precisa ter 11 dígitos e conter apenas números reais")
        return False
    elif len(cpf) != 11:
        print("O cpf precisa ter 11 dígitos")
        return False
    elif cont != 11:
        print("Utilize apenas números reais")
        return False
    else:
        iguais = 0                                             # a partir desse "else", acontece a verificação matemática.
        for k in range(len(cpf)):                              # em primeiro lugar, verifica-se se o cpf não possui todos os dígitos iguais.
            if cpf[k] == cpf[0]:                               # em segundo lugar, é verificado o primeiro dígito de verificação.
                iguais += 1                                    # em terceiro lugar, é verificado o segundo dígito de verificação.
                                                               # depois, os dígitos verificadores são comparados e então validados.  
        if iguais == 11:
            print("CPF inválido: números repetidos")
            return False
    def dv1_cpf(cpf):
     """Calcula o primeiro dígito verificador do CPF.
    
        Parte integrante do requisito de validação matemática do sistema. Multiplica 
        os 9 primeiros dígitos por pesos decrescentes de 10 a 2, soma os resultados 
        e aplica a operação de resto da divisão por 11.
    
        Args:
            cpf: String contendo os dígitos do CPF.
    
        Returns:
            O valor inteiro do primeiro dígito verificador - first_verify(int), ou o valor 0(int).
            
        Atende ao requisito:
            RF001.02 (Validação matemática do CPF via Anexo B).
        """
        soma1 = 0
        multiplicacao1 = 10
        for i in range(9):
            soma1 += int(cpf[i]) * multiplicacao1             # nesta linha, a string "cpf" é convertida em número inteiro,
            multiplicacao1 -= 1                               # para que possa ser multiplicada como um número.    

        resto1 = soma1 % 11
        if resto1 < 2:
            return 0
        else:
            first_verify = 11 - resto1
            if first_verify >= 10:
                return 0
            else:
                return first_verify
    
    def dv2_cpf(cpf, first_verify):
    """Calcula o segundo dígito verificador do CPF.

    Parte integrante do requisito de validação matemática do sistema. Multiplica 
    os 9 primeiros dígitos por pesos decrescentes de 11 a 3, soma ao produto do 
    primeiro dígito verificador por 2 e aplica o módulo 11.

    Args:
        cpf: String contendo os dígitos do CPF é transformada em int.
        first_verify (int): O primeiro dígito verificador já calculado.

    Returns:
        O valor inteiro do segundo dígito verificador, first_verify (int), ou o valor 0 (int).
        
    Atende ao requisito:
        RF001.02 (Validação matemática do CPF via Anexo B).
    """
        soma2 = 0
        multiplicacao2 = 11
        for i in range(9):
            soma2 += int(cpf[i]) * multiplicacao2
            multiplicacao2 -= 1

        soma2 += first_verify * 2
        resto2 = soma2 % 11
        if resto2 < 2:
            return 0
        else:
            second_verify = 11 - resto2
            if second_verify >= 10:
                return 0
            else:
                return second_verify
    
    digito1 = dv1_cpf(cpf)
    digito2 = dv2_cpf(cpf, digito1)

    if digito1 == int(cpf[9]) and digito2 == int(cpf[10]):
        print("CPF válido!")
        return True
    else:
        print("CPF inválido: erro nos dígitos verificadores.")
        return False
    
def pedir_cpf():
     """
    Interface de entrada de dados para captura e validação contínua do CPF.

    A função inicia um laço de repetição (while) que solicita ao usuário a 
    digitação do CPF via terminal. O laço só é interrompido quando a função 
    'validar_cpf' retorna True, garantindo que o programa avance apenas 
    com um dado válido.

    Requisitos Atendidos:
        - RF001.01: Captura de dados cadastrais via entrada padrão.

    Args:
        None
        
    Returns:
        cpf (str): Cadeia de caracteres contendo o CPF validado (apenas números).
    """
     valido = False
     while not valido:
        cpf = input("Digite seu CPF:")
        
        valido = validar_cpf(cpf)
     return cpf 
    
# ==== VALIDAÇÃO DO TÍTULO ====
# Função que verifica se o campo está vazio ou só tem espaço
def campo_vazio(texto):
    
    """
    Verifica se a string informada está vazia ou contém apenas espaços.

    Requisitos Atendidos:
        - Regra de Negócio Geral (Módulo Gerenciamento): Validação e consistência 
          de dados para impedir o salvamento de campos nulos no terminal.
        - RF003.01: Validação geral de preenchimento obrigatório de campos.

    Args:
        texto (str): A cadeia de caracteres a ser analisada.

    Returns:
        bool: True se estiver vazia ou com apenas espaços, False caso contrário.
    """
    if texto == "":
        return True
    for c in texto:
        if c != " ":
            return False
    return True
                # Função que verifica se todos os caracteres são números
def apenas_numeros(texto):
    """
    Verifica se a string é composta exclusivamente por caracteres numéricos.

    Requisitos Atendidos:
        - RF001.02: Validação de CPF e Título aceitando apenas números reais.

    Args:
        texto (str): A cadeia de caracteres a ser analisada.

    Returns:
        bool: True se contiver apenas dígitos de 0 a 9, False caso contrário.
    """
    for c in texto:
        if c < "0" or c > "9":
            return False
    return True
                # Função que verifica se todos os dígitos são iguais (ex: 111111111111)
def todos_iguais(texto):
    """
    Identifica se todos os caracteres da string são idênticos entre si.

    Requisitos Atendidos:
        - Regra de Negócio Geral (Módulo Gerenciamento): Detecção de fraudes ou 
          padrões inválidos em preenchimentos sequenciais idênticos (ex: 111111).
        - RF003.02: Validação geral contra sequências de caracteres repetidos.
    Args:
        texto (str): A cadeia de caracteres a ser analisada.

    Returns:
        bool: True se todos os caracteres forem repetidos, False caso contrário.
    """
    if texto == "":
        return False
    return all(c == texto[0] for c in texto)
                # Função que verifica se é uma sequência crescente (ex: 123456...)  
def sequencia_crescente(texto):
    """
    Verifica se os dígitos da string formam uma sequência matemática estritamente crescente.

    Requisitos Atendidos:
        - Regra de Negócio Geral (Módulo Gerenciamento): Bloqueio de inserções estruturais 
          falsas no terminal (ex: sequências óbvias como 123456).
         - RF003.03: Validação geral contra preenchimentos em sequência consecutiva linear.
    Args:
        texto (str): A cadeia de caracteres numéricos a ser analisada.

    Returns:
        bool: True se for uma sequência consecutiva, False caso contrário.
    """
    for i in range(len(texto) - 1):
        if int(texto[i]) + 1 != int(texto[i + 1]):
            return False
    return True

def validar_titulo(titulo_eleitor):
    """
    Executa a validação estrutural e matemática de um número de Título de Eleitor.

    A função valida a string de entrada verificando se ela cumpre as etapas de 
    consistência do formulário (vazio, tipo de dado, tamanho e UF) em um laço contínuo. 
    Se aprovada nas validações, realiza o cálculo dos dois dígitos verificadores (DV) 
    por meio de somatórios ponderados e operação de resto de divisão por 11.

    Requisitos Atendidos:
        - RF002.01: Interface de entrada e consistência de dados do Título.
        - RF002.02: Validação matemática do Título de Eleitor.

    Args:
        titulo_eleitor (str): Cadeia de caracteres contendo o título a ser validado.

    Returns:
        titulo_eleitor (str): O número do Título de Eleitor validado e confirmado pelo sistema.
    """
 # Variável de controle do loop
 titulo_valido = False
 # Loop que só para quando o título for válido
 while not titulo_valido:
# Verifica se está vazio
    if campo_vazio(titulo_eleitor):
        print("Erro: campo vazio.\n")
        titulo_eleitor = input("Tente novamente:")
 # Verifica se só tem números
    elif not apenas_numeros(titulo_eleitor):
        print("Erro: o título deve conter apenas números.\n")
        titulo_eleitor = input("Tente novamente:")
# Verifica tamanho correto (12 dígitos)
    elif len(titulo_eleitor) != 12:
        print("Erro: precisa ter exatamente 12 dígitos.\n")
        titulo_eleitor = input("Tente novamente:")
# Verifica sequência crescente inválida
    elif sequencia_crescente(titulo_eleitor):
        print("Erro: sequência inválida.\n")
        titulo_eleitor = input("Tente novamente:")
    # Mudamos de 'else:' para um 'elif' que testa a UF antes de qualquer cálculo:
    elif int(titulo_eleitor[8:10]) < 1 or int(titulo_eleitor[8:10]) > 28:
         print("Erro: UF inválida.\n")
         titulo_eleitor = input("Tente novamente:")
         # O 'continue' antigo que ficava aqui FOI REMOVIDO.

    else:
        # Este novo 'else' só executa se o título passou em TODAS as validações acima.
        # Agora a extração da UF e dos dígitos é 100% segura.
         uf = int(titulo_eleitor[8:10])
         numero = titulo_eleitor[:8]
         digitos = titulo_eleitor[10:12]
         pesos1 = [2, 3, 4, 5, 6, 7, 8, 9]
         soma = 0
         for i in range(8):
            soma += int(numero[i]) * pesos1[i]
         resto = soma % 11
         dv1 = 0 if resto == 10 else resto
         soma2 = (int(titulo_eleitor[8]) * 7) + (int(titulo_eleitor[9]) * 8) + (dv1 * 9)
         resto2 = soma2 % 11
         dv2 = 0 if resto2 == 10 else resto2
            
         if digitos == str(dv1) + str(dv2):
            print("Título válido")
            titulo_valido = True
            return titulo_eleitor # Adicionado para retornar o valor limpo ao final
         else:
            # Pequeno ajuste aqui: se os dígitos falharem, precisamos pedir o input 
            # de novo, senão ele travaria no while com o mesmo número incorreto.
            print("Título inválido: dígitos não conferem.\n")
            titulo_eleitor = input("Tente novamente: ")

        
# === VERIFICAÇÃO DO NOME COMPLETO ===
def verificar_nome(nome_completo):
    """
    Valida se a entrada de texto corresponde a um nome completo estruturado.

    Requisitos Atendidos:
        - RF001.01: Cadastramento de novos eleitores, solicitando obrigatoriamente o nome completo.

    Args:
        nome_completo (str): A string do nome digitada no terminal.

    Returns:
        None
    """
    valido = False

    while not valido:
        for i in range(len(nome_completo)):
            if nome_completo[i] ==" " and i != 0 and i != len(nome_completo) - 1:
                valido = True
                break
        
        if valido:
            print("Nome completo válido!")
        else:
            print("ERRO! Digite seu nome e sobrenome:")
            nome_completo = input("Tente novamente:")
        
