
import time
# validações de entrada do usuário
from validacoes import validar_titulo
from validacoes import pedir_cpf
from validacoes import verificar_nome
# importações de módulos do sistema
from conexaobd import buscar   
from conexaobd import buscar_tudo
from conexaobd import executar  
# geração de dados de segurança
from chave import gerar_chave 
from chave_protocolo import gerar_protocolo #importa a funcao de geracao de geracao de protocolo em protocolo.py
# auditoria e logs do sistema
from auditoria import mostrar_logs, mostrar_protocolos, registrar_log
#criptografia dos dados sensíveis (cpf, chave etc.)
from criptografia import criptografar_hill
from datetime import datetime

def menu_gerenciamento(): 
    """Interface de terminal para o controle administrativo de eleitores e candidatos.

    Esta função gerencia as operações do módulo administrativo, englobando
    o cadastro, busca, edição e exclusão de dados correspondentes às regras
    de negócio do sistema de votação digital fictício. as funçoes de validação 
    estão no arquivo "validações", e a de criptografia em "criptografia", 
    porém foram chamadas no menu.

    Requisitos Atendidos:
        - RF001: Módulo de Gerenciamento Administrativo.
        - RF001.01, RF001.02, RF001.03, RF001.04: Processo de Cadastro do Eleitor.
        - RF001.05: Edição de dados do Eleitor.
        - RF001.06: Remoção do Eleitor.
        - RF001.07: Busca por Eleitor específico.
        - RF001.08: Listagem de todos os Eleitores.
        - RF001.09 a RF001.14: dados do Candidato.

    Args:
        None

    Returns:
        None
    
    """
    opcao = 0  #comecamos a opcao com 0 so para entrar no menu pela primeira vez
    while opcao !=9: #menu continua abrindo enquanto o usuario nao escolher a opcao de voltar
        print("\n=== MENU GERENCIAMENTO ===")
        print("1 - Cadastrar eleitor")
        print("2 - Buscar eleitor")
        print("3 - Cadastrar candidato")
        print("4 - Buscar candidato")
        print("5 - Criar Partido")
        print("6 - Buscar Partido")
        print("7 - Editar eleitor")
        print("8 - Remover eleitor")
        print("9 - Voltar")
        try: #tenta transformar o que o usuario digitou em numero
            opcao = int(input("Escolha uma opcao: "))
        except ValueError: #se o usuario digitar letra ou algo invalido, a opcao vira 0 (ValueError)
            opcao = 0
        #a partir daqui o programa verifica qual numero foi escolhido   
        match opcao:
            case 1:
                #coleta e validação de dados do eleitor
                nome_completo = input("Digite seu nome completo:")
                verificar_nome(nome_completo)
                titulo_eleitor = input("Digite o Título de Eleitor:")
                validar_titulo(titulo_eleitor)
                cpf = pedir_cpf()
                #cpf é criptografado antes de ir pro banco
                cpf_cifrado = criptografar_hill(cpf)
                prefixo_cpf = cpf[:4] #pega os 4 primeiros dígitos
                # ==== MESÁRIO ====
                mesario = input("Mesário s/n:").lower()
                if mesario == "s":
                    mesario = 1
                else:
                    mesario = 0
                    #geração de chave de acesso do eleitor
                chave = gerar_chave(nome_completo)
                chave_acesso_cifrada = criptografar_hill(chave)
                             # A partir daqui até o print, o CPF é validado antes de ser salvado
                #Inserção de dados no banco
                comando = "INSERT INTO eleitores (nome, titulo_eleitor, prefixo_cpf, cpf, mesario, chave_acesso_cifrada, ja_votou) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                valores = [nome_completo,titulo_eleitor, prefixo_cpf, cpf_cifrado, mesario, chave_acesso_cifrada, 0]
                executar(comando,valores)
                print("Cadastrado.")   
            case 2:
             # ==== BUSCAR ELEITOR ====
                cpf_inserido = input("Digite o seu CPF:")
                cpf_cifrado = criptografar_hill(cpf_inserido)
                comando = "SELECT * FROM eleitores WHERE cpf = %s"
                valores = (cpf_cifrado,)
                eleitor = buscar(comando, valores)
                #Exibe dados se encontrado
                if eleitor:
                    print("\n--- ELEITOR ENCONTRADO ---")
                    print(f"Nome: {eleitor[1]}")
                    print(f"Título de Eleitor: {eleitor[2]}")
                    print(f"CPF: {eleitor[3]}")
                    print("Mesário:", "Sim" if eleitor[5] else "Não")
                    print("Já votou:", "Sim" if eleitor[7] else "Não")
                else:
                    print("\n[!] Erro: Eleitor não cadastrado.")
            case 3:
         # ==== CADASTRO DE CANDIDATO ==== 
                nome_completo_candidato = input("Digite seu nome completo:")
                numero_candidato = int(input("Seu número para votação:"))
                id_partido = int(input("Informe o ID do partido:"))
                comando = "INSERT INTO candidatos (candidato ,numero_votacao ,id_partido) VALUES (%s, %s, %s)"
                valores = [nome_completo_candidato,numero_candidato,id_partido]
                executar(comando,valores)
 
                print("Cadastrado com sucesso!")
            case 4:
             # ==== BUSCA DE CANDIDATO ====
                numero_candidatoB = int(input("Digite o número do candidato:"))
                comando = """
                 SELECT c.candidato, p.partido, p.sigla
                 FROM candidatos c
                 JOIN partidos p ON c.id_partido = p.id_partido
                 WHERE c.numero_votacao = %s
                """
                valores = [numero_candidatoB]
                resultado = buscar(comando, valores)
                if resultado:
                    print("\n--- INFORMAÇÕES DO CANDIDATO ---")
                    print(f"Nome: {resultado[0]}")
                    print(f"Partido: {resultado[1]}")
                    print(f"Sigla: {resultado[2]}")
                else:
                    print("\n[!] Erro: Eleitor não cadastrado.")
            case 5:
             # ==== CRIAÇÃO DE PARTIDO ====
                nome_partido = input("Digite o nome do partido:")
                sigla_partido = input("Digite a sigla do partido:")
                comando = "INSERT INTO partidos (partido, sigla) VALUES (%s, %s)"
                valores = [nome_partido, sigla_partido]
                executar(comando, valores)
                print("Partido cadastrado com sucesso!")
            case 6:
             # ==== BUSCA DE PARTIDO ==== 
                sigla_partidoB = input("Digite a sigla do partido:")
                comando = "SELECT partido FROM partidos WHERE sigla = %s"
                valores = [sigla_partidoB]
                resultado = buscar(comando, valores)
                if resultado:
                    print(f"Partido: {resultado[0]}")
                else:
                    print("\n[!] Erro: Partido não cadastrado.")
            case 7:
                # === EDIÇÃO DE ELEITOR ===
                
                opcao = 0
                while opcao != 6:
                    print("1 - Visualizar id do eleitor")
                    print("2 - Alterar nome")
                    print("3 - Alterar cpf")
                    print("4 - Alterar título")
                    print("5 - Mesário")
                    print("6 - Voltar")
                
                    try:
                        opcao=int(input("Digite um número de 1 a 5:"))
                    except ValueError:
                        opcao = 0
                    match opcao:

                        #=============================================
                        # VISUALIZAR TÍTULO DE ELEITOR
                        #=============================================

                        case 1:
                            # Solicita o CPF do eleitor
                            cpf=pedir_cpf()
                            # Criptografia para buscar no banco
                            cpf_cifrado = criptografar_hill(cpf)
                            comando = "SELECT titulo_eleitor FROM eleitores WHERE cpf = %s"                            
                            valores = [cpf_cifrado,]
                            resultado = buscar(comando, valores)
                            #Exibe o título encontrado
                            print(f"\n\nTitulo do Eleitor: {resultado[0]}")

                        #============================================
                        # ALTERAR O NOME DO ELEITOR
                        #============================================
                        case 2:
                            # Utiliza o título para localizar o eleitor
                            id_eleitor = input("Titulo do Eleitor:")

                            # Novo nome
                            nome_completo=input("nome:")
                            comando="UPDATE eleitores SET nome = %s WHERE titulo_eleitor = %s"
                            valores = [nome_completo, id_eleitor]
                            executar(comando, valores)
                            print("Nome atualizado com sucesso.")

                        #============================================
                        # ALTERAR CPF DO ELEITOR
                        #============================================
                        case 3:
                            id_eleitor = input("Titulo do Eleitor:") 
                            # Solicita novo CPF
                            cpf=pedir_cpf()
                            #Atualiza também o prefixo utilizado no sistema
                            prefixo_cpf = cpf[:4]
                            #Criptografa o novo CPF
                            cpf_cifrado = criptografar_hill(cpf)
                            comando="UPDATE eleitores SET cpf = %s and prefixo_cpf = %s WHERE titulo_eleitor = %s"
                            valores = [cpf_cifrado, prefixo_cpf, id_eleitor]
                            executar(comando, valores)
                            print("CPF atualizado com sucesso.")
                        #============================================
                        # ALTERAR TÍTULO DE ELEITOR
                        #============================================
                                                        
                        case 4:
                            # Solicita novo título
                            titulo_eleitor = input("Digite o Título de Eleitor:")
                            # Valida o formato do título
                            validar_titulo(titulo_eleitor)

                            # Comando que atualiza o titulo de eleitor
                            comando = "UPDATE eleitores SET titulo_eleitor = %s WHERE titulo_eleitor = %s"
                            valores = [titulo_eleitor]
                            executar(comando,valores)
                            print("Título atualizado com sucesso.")  

                        #=============================================
                        # ALTERAR STATUS DE MESÁRIO
                        #=============================================
                        case 5:
                            id_eleitor = input("Titulo do Eleitor:") 
                            # Define se o eleitor é mesário ou não
                            mesario = input("Mesário s/n:").lower()

                            if mesario == "s":
                                mesario = 1
                            else:
                                mesario = 0
                            comando="UPDATE eleitores SET mesario = %s WHERE titulo_eleitor = %s"
                            valores = [mesario, id_eleitor]
                            executar(comando, valores)
                            print("Eleitor atualizado com sucesso.")

                        #============================================
                        # VOLTAR AO MENU PRINCIPAL
                        #============================================
                        case 6:
                            print("voltando ao menu principal")
                               
                        case _:
                            print("opção inválida")
            case 8:
               #=== REMOVER ELEITOR===  
                opcao = 0
                while opcao != 3:
                    print("1 - Visualizar id do eleitor")
                    print("2 - Remover eleitor")
                    print("3 - Voltar")
                    try:
                        opcao=int(input("digite a opção:"))
                        
                    except ValueError:
                        opcao = 0
                        
                    match opcao:
                        case 1: 
                            cpf=pedir_cpf()
                            cpf_cifrado = criptografar_hill(cpf)
                            comando = "SELECT titulo_eleitor FROM eleitores WHERE cpf = %s"                            
                            valores = [cpf_cifrado,]
                            resultado = buscar(comando, valores)
                            print(f"\n\nTitulo do Eleitor: {resultado[0]}")
                        case 2:    
                          
                                id_eleitor=input("Titulo do Eleitor:")
                                validar_titulo(id_eleitor)      
                                #DELETE no banco remove eleitor permanentemente                    
                                comando = "DELETE FROM eleitores WHERE titulo_eleitor = %s"
                                valores = [id_eleitor]
                                executar (comando, valores )
                                print("Eleitor removido com sucesso.")
                                
                        case 3:
                            print("voltando ao menu principal")
                        case _:
                            print("opção inválida")
                print("Voltando ao menu principal...")
                
            case _:
                print("Opcao invalida.")

def menu_encerramento(urna_aberta):
    """
    Interface de terminal para o fechamento controlado da urna eletrônica.

    Esta função gerencia o fluxo de encerramento do evento eleitoral. Ela valida 
    se a urna está ativa, exige a identificação de um eleitor com privilégios de 
    mesário por meio de seus documentos, compara as credenciais e solicita uma 
    confirmação dupla de segurança antes de consolidar o encerramento.

    Requisitos Atendidos:
        - RF002: Integração com o fluxo final do Módulo de Votação.

    Args:
        urna_aberta (bool): Estado atual da urna (True para aberta, False para fechada).

    Returns:
        urna_aberta (bool): O estado atualizado da urna após a execução da função (False se for 
        encerrada com sucesso, ou o estado original caso falhe ou seja cancelada).
    """
    # Se a urna ja estiver fechada, nao faz sentido continuar
    if  urna_aberta == False:
        print("\nA urna já está fechada ou não foi aberta.")
        return urna_aberta
    #controle do loop do menu de encerramento
    executando = True

    while executando == True:
        print("\n=== MENU DE ENCERRAMENTO ===")
        print("1 - Iniciar Protocolo de Fechamento")
        print("2 - Voltar")
        # tratamento de erro para entrada inválida
        try:
            opcao=int(input("digite 1 ou 2: "))
        except ValueError:
            print("Opção inválida. Voltando para o menu de votação...")
            return urna_aberta
    # estrutura principal de decisão do menu
        match opcao:
            case 1:
                try:
                    # ===================================
                    # VALIDAÇÃO DO MESÁRIO
                    # ===================================   
                    titulo = input("digite o título:")
                    prefixo_cpf = input("insira os 4 primeiros dígitos dpo cpf:")
                    chave = input("chave de acesso:")

                    #criptografa a chave para comparar com o banco
                    chave_cifrada = criptografar_hill(chave)

                    #busca no banco apenas mesários autorizados
                    comando = "SELECT chave_acesso_cifrada FROM eleitores WHERE titulo_eleitor = %s AND prefixo_cpf = %s AND mesario = 1 "           
                    valores = [titulo, prefixo_cpf]
                    resultado = buscar(comando, valores)

                    # verifica se encontrou um mesário
                    if resultado != None:
                        #confere se a chave informada está correta
                        if resultado[0] == chave_cifrada: 
                            print("Chave correta!")
                            # ==============================
                            # DUPLA CONFIRMAÇÃO DE SEGURANÇA
                            # ==============================

                            confirmação = input("Deseja realmente encerrar a votação? (1 para sim/2 para não)")
                            if confirmação =='1':

                                # Segunda validação da chave(segurança extra)
                                segunda_chave = input("digite a chave novamente:")  
                                segunda_chave_cifrada = criptografar_hill(segunda_chave)                      
                                if resultado[0] == segunda_chave_cifrada:
                                    # ================================
                                    # ENCERRAMENTO DA URNA
                                    # ================================
                                    print("URNA ENCERRADA")
                                    # Registra evento no log do sistema
                                    registrar_log("ENCERRAMENTO: Votação finalizada com sucesso.")

                                    #atualiza estado da urna
                                    urna_aberta=False
                                    executando = False
                                    #exibe resultados finais automaticamente
                                    menu_resultados()
                                    return urna_aberta
                                else:
                                    print("Erro. a chave está errada")
                                    
                            elif confirmação == '2':
                                print("Operação cancelada.")
                             
                            else:
                                print("Resposta inválida. Operação cancelada.")      
                        else:
                            print("Chave incorreta.") 
               
                    else:
                        print("Mesário não encontrado ou sem permissão.")

                except ValueError:
                     print(f"Erro: Digite apenas números para Título e CPF.")
                #Encerra o loop após tentativa (mesmo que falhe)
                executando = False
            case 2:
                #Usuário desistiu de encerrar a urna
                print("Voltando para o menu de votação...")
                executando = False

            case _:
                #opçao inválida no menu
                print("Opção inválida")
                executando = False
    # Retorna o estado final da urna (aberta ou fechada)
    return urna_aberta
    
def menu_auditoria():
    """
    Interface de terminal para o módulo de auditoria e transparência do sistema.

   gerenciamento do fluxo de verificação e fiscalização pós-votação. Ela 
    permite ao usuário consultar o histórico de eventos críticos do sistema, listar 
    e validar os protocolos emitidos, além de visualizar o relatório final de encerramento de urnas.

    Requisitos Atendidos:
        - RF002.02.01: Permite o acesso à Exibição de Logs de Ocorrências.
        - RF002.02.02: Permite o acesso à Exibição dos Protocolos de Votação.

    Args:
        None

    Returns:
        None
    """
    # opção inicial do menu
    opcao = 0
    # Loop do menu: continua até o usuário escolher "3 - voltar"
    while opcao != 3:

        print("\n=== AUDITORIA DA VOTACAO ===")

        #opções disponíveis no módulo de auditoria
        print("1 - Exibir logs")
        print("2 - Exibir protocolos")
        print("3 - Voltar")
        #entrada do usuário 
        opcao = int(input("\nEscolha uma opcao: "))

        match opcao:
            case 1:
                #exibe o histórico de eventos do sistema (tentivas, votos, erros, etc)
                mostrar_logs()
        
            case 2:
                #exibe os protocolos gerados durante as votações
                mostrar_protocolos()
                
            case 3:
                #Sai do menu auditoria e volta ao menu anterior
                print("\nVoltando ao menu de votacao...")
            
            case _:
                
                print("\n Opçao invalida")
                
def menu_resultados():
    """
    Interface de terminal para o submodulo de relatorios e apuracao de resultados.

    centralização da exibicao das estatisticas da eleicao, permitindo 
    a emissao do boletim de urna, calculos de comparecimento eleitoral, votacao 
    consolidada por legenda partidaria e auditoria de integridade dos dados.

    Requisitos Atendidos:
        - RF002.03.01: Emissao do Boletim de Urna com totalizacao e definicao do vencedor.
        - RF002.03.02: Exibicao da Estatistica de Comparecimento absoluto e percentual.
        - RF002.03.03: Consolidacao e listagem de Votos por Partido.
        - RF002.03.06: Execucao da Validacao de Integridade dos dados de votacao.

    Args:
        None

    Returns:
        None
    """
    opcao = 0
    while opcao != 5:
        print("\n=== RESULTADOS DA VOTACAO ===")
        print("1 - Boletim de urna")
        print("2 - Estatistica de comparecimento")
        print("3 - Votos por partido")
        print("4 - Validacao de Integridade")
        print("5 - Voltar")
        try:
            opcao = int(input("Escolha uma opcao: "))
        except ValueError:
            opcao = 0

        match opcao:
            case 1:

                comando = """
                SELECT 
                    c.candidato, 
                    c.numero_votacao, 
                    p.sigla, 
                    COUNT(v.id_voto) AS votos   
                FROM candidatos c
                JOIN partidos p ON c.id_partido = p.id_partido
                LEFT JOIN votos v ON c.id_candidato = v.id_candidato
                GROUP BY c.id_candidato, c.candidato, c.numero_votacao, p.sigla
                ORDER BY c.candidato ASC;
                """
                # comando busca completa
                resultado = buscar_tudo(comando, [])

                comando2 = """ SELECT COUNT(*) FROM votos WHERE voto_nulo = 1 """
                votos_nulos = buscar(comando2, [])[0]
                
                print("\n=== BOLETIM DE URNA ===")
                print(f"Total de votos nulos: {votos_nulos}")
                print("-" * 50)
                
                vencedor_nome = None
                vencedor_numero = None
                vencedor_sigla = None
                max_votos = -1
                empate = False

                if resultado:

                    for linha in resultado:
                        nome_cand, num_cand, sigla_part, qtd_votos = linha[:4] 
                        print(f"Candidato: {nome_cand:<25} | Número: {num_cand:<5} | Partido: {sigla_part:<6} | Votos: {qtd_votos}")
                        
                        if qtd_votos > max_votos:
                            max_votos = qtd_votos
                            vencedor_nome = nome_cand
                            vencedor_numero = num_cand
                            vencedor_sigla = sigla_part
                            empate = False
                        elif qtd_votos == max_votos and max_votos > 0:
                            empate = True
                    
                    print("-" * 50)
                    
                    if max_votos == 0:
                        print("Eleição encerrada sem votos computados para candidatos.")
                    elif empate:
                        print(f"Empate! Mais de um candidato obteve {max_votos} votos.")
                    else:
                        print("=== VENCEDOR DA ELEIÇÃO ===")
                        time.sleep(5)
                        print(f"Nome: {vencedor_nome}")
                        print(f"Número: {vencedor_numero}")
                        print(f"Partido: {vencedor_sigla}")
                        print(f"Total de Votos: {max_votos}")
                else:
                    print("Nenhum candidato cadastrado no sistema.")
                print("-" * 50)
            case 2:
                def print_suspense(texto, velocidade=0.03): 
                    for letra in texto: 
                        print(letra, end="")
                        time.sleep(velocidade) 
                    print()
            
                # Efeito de carregamento original mantido!
                print("Calculando resultados", end="")
            
                time.sleep(1)  
                print(".", end="")
            
                time.sleep(1)
                print(".", end="")
            
                time.sleep(1)
                print(".")
            
                time.sleep(0.3)
            
                print("\n=== ESTATISTICA DE COMPARECIMENTO ===")
                print("-" * 50)
            
                comando = """
                SELECT
                    (SELECT COUNT(*) FROM eleitores) AS total_eleitores,
                    (SELECT COUNT(*) FROM eleitores WHERE ja_votou = 1) AS total_votos,
                    (SELECT COUNT(*) FROM votos WHERE voto_nulo = 0 AND id_candidato IS NOT NULL) AS votos_candidato,
                    (SELECT COUNT(*) FROM votos WHERE voto_nulo = 1) AS votos_nulos,
                    (SELECT COUNT(*) FROM votos WHERE voto_nulo = 0 AND id_candidato IS NULL) AS votos_brancos
                """
            
                resultado = buscar(comando, ())
            
                if resultado:
                    # Dados extraídos do banco de forma segura
                    total_eleitores = resultado[0]
                    total_votos = resultado[1]
                    votos_candidato = resultado[2]
                    votos_nulos = resultado[3]
                    votos_brancos = resultado[4]
            
                    # Calculo das Estatisticas mantendo a lógica dele
                    if total_eleitores > 0:
                        percentual_comparecimento = (total_votos / total_eleitores) * 100
                        percentual_candidato = (votos_candidato / total_eleitores) * 100
                        percentual_nulos = (votos_nulos / total_eleitores) * 100
                        percentual_brancos = (votos_brancos / total_eleitores) * 100
                        
                        abstencao = total_eleitores - total_votos
                        percentual_abstencao = (abstencao / total_eleitores) * 100
                    else:
                        percentual_comparecimento = 0
                        percentual_candidato = 0
                        percentual_nulos = 0
                        percentual_brancos = 0
                        abstencao = 0
                        percentual_abstencao = 0
            
                    time.sleep(0.1)
            
                    # Exibição com o efeito de suspense original que ele criou!
                    print_suspense(f"Total de eleitores aptos..........: {total_eleitores}")
                    time.sleep(0.4) # Diminuí levemente os sleeps entre linhas pro usuário não cansar de esperar
            
                    print_suspense(f"Quantidade de pessoas que votaram: {total_votos}")
                    time.sleep(0.4)
            
                    print_suspense(f"Quantidade de votos em candidatos: {votos_candidato}")
                    time.sleep(0.4)
            
                    print_suspense(f"Quantidade de votos nulos........: {votos_nulos}")
                    time.sleep(0.4)
                    
                    print_suspense(f"Quantidade de votos em branco....: {votos_brancos}")
                    time.sleep(0.4)
                    print("-" * 50)
            
                    print_suspense(f"Percentual de comparecimento.....: {percentual_comparecimento:.2f}%")
                    time.sleep(0.4)
            
                    print_suspense(f"Percentual de votos candidatos...: {percentual_candidato:.2f}%")
                    time.sleep(0.4)
            
                    print_suspense(f"Percentual de votos nulos........: {percentual_nulos:.2f}%")
                    time.sleep(0.4)
                    
                    print_suspense(f"Percentual de votos em branco....: {percentual_brancos:.2f}%")
                    time.sleep(0.4)
            
                    print_suspense(f"Abstencoes.......................: {abstencao}")
                    time.sleep(0.4)
            
                    print_suspense(f"Percentual de abstencao..........: {percentual_abstencao:.2f}%")
                    print("-" * 50)
            

                else:
                    print("Erro ao gerar estatisticas.")
            case 3:
                comando = """
                SELECT 
                    p.partido, 
                    p.sigla, 
                    COUNT(v.id_voto) AS total_votos
                FROM partidos p
                JOIN candidatos c ON p.id_partido = c.id_partido
                LEFT JOIN votos v ON c.id_candidato = v.id_candidato
                GROUP BY p.id_partido, p.partido, p.sigla
                ORDER BY total_votos DESC;
                """
                # Buscando todos os partidos que possuem candidatos e seus respectivos votos
                resultado = buscar_tudo(comando, [])
                
                print("\n=== VOTOS POR PARTIDO ===")
                print("-" * 50)
                
                if resultado:
                    for linha in resultado:
                        nome_partido, sigla, total_votos = linha[:3]
                        print(f"Partido: {nome_partido:<20} | Sigla: {sigla:<6} | Total de Votos: {total_votos}")
                else:
                    print("Nenhum dado de votação ou partido encontrado.")
                    
                print("-" * 50)
            case 4:
                print("\n=== VALIDACAO DE INTEGRIDADE ===")
                print("=" * 55)
            
                # 1. Total de eleitores aptos
                comando = "SELECT COUNT(*) FROM eleitores"
                total_eleitores = buscar(comando, ())[0]

                # 2. Total de votos registrados
                comando = "SELECT COUNT(*) FROM votos"
                total_votos = buscar(comando, ())[0]
            
                # 3. Pessoas marcadas como ja_votou
                comando = "SELECT COUNT(*) FROM eleitores WHERE ja_votou = 1"
                total_ja_votou = buscar(comando, ())[0]
            
                # 4. Votos com candidato inexistente 
                comando = """
                SELECT COUNT(*)
                FROM votos v
                LEFT JOIN candidatos c ON v.id_candidato = c.id_candidato
                WHERE v.id_candidato IS NOT NULL AND c.id_candidato IS NULL
                """
                votos_invalidos = buscar(comando, ())[0]
            
                # Exibição dos dados na tela
                print(f"Eleitores aptos.............: {total_eleitores}")
                print(f"Votos registrados..........: {total_votos}")
                print(f"Eleitores que ja votaram...: {total_ja_votou}")
                print(f"Votos invalidos............: {votos_invalidos}")
                print("=" * 55)
            
                erro = False
            
                # Teste 1: Confere se tem mais votos do que pessoas cadastradas
                if total_votos > total_eleitores:
                    print("[ERRO] Existem mais votos do que eleitores aptos.")
                    erro = True
            
                # Teste 2: Confere se a quantidade de votos bate com a flag ja_votou dos eleitores
                if total_votos != total_ja_votou:
                    print("[ERRO] Quantidade de votos diferente dos eleitores marcados como votantes.")
                    erro = True
            
                # Teste 3: Confere se há falha de integridade referencial
                if votos_invalidos > 0:
                    print("[ERRO] Existem votos associados a candidatos inexistentes.")
                    erro = True
            
                # Validação final do relatório de auditoria
                if not erro:
                    print("INTEGRIDADE VALIDADA COM SUCESSO.")
                    print("Nenhuma anomalia encontrada nos dados da votação.")
                else:
                    print("\nALERTA: Foram encontradas inconsistencias no sistema!")
            
                print("=" * 55)
def menu_votacao():
    """
    Interface de terminal para o modulo de processamento do evento eleitoral.

    Esta funcao gerencia o ciclo de vida completo da urna eletronica. Ela controla 
    o estado da urna, executa o fluxo sequencial de identificacao do eleitor 
    (CPF, Titulo e Chave de Acesso), processa a computacao de votos nominais ou nulos 
    e direciona para as telas de administracao e auditoria.

    Requisitos Atendidos:
        - RF002: Processamento das etapas do processo eleitoral e controle da urna.
        - RF002.02.01.03: Registro do evento de ABERTURA apos validacao do mesario.
        - RF002.02.01.04: Registro de ALERTA para falhas de identificacao ou acesso negado.
        - RF002.02.01.05: Registro de ALERTA para tentativa de voto duplo.
        - RF002.02.01.06: Registro de SUCESSO no instante da confirmacao do voto.

    Args:
        None

    Returns:
        None
    """
    urna_aberta = False
    opcao = 0
    while opcao != 5:
        print("\n=== MENU VOTACAO ===")
        print("1 - Abrir sistema de votacao")
        print("2 - Auditoria da votacao")
        print("3 - Resultado da votacao")
        print("4 - Voltar")
        # Tenta converter a opção digitada para inteiro
        try:
            opcao = int(input("Escolha uma opcao: "))
        # Verificação qual opção foi escolhida 
        except ValueError:
            opcao = 0

        match opcao:

            case 1:

                #Impede que a urna seja aberta duas vezes
                if urna_aberta:
                    print("A urna ja está aberta.")

                else: 
            #==================================================
            # AUTENTICAÇÃO DO MESÁRIO
            #==================================================

                    titulo = input("Digite o titulo:")

                    #valida formato do título
                    validar_titulo(titulo)

                    #solicita os 4 primeiros dígitos do cpf
                    prefixo_cpf = input("Insira os 4 primeiros digitos do cpf:")

                    #solicita a chave de acesso do mesário
                    chave = input("Digite sua chave de acesso:")

                    #Criptografa a chave para comparação segura
                    chave_cifrada = criptografar_hill(chave)

                    #Busca um mesário que possua todos os dados informados
                    comando = """ SELECT * FROM eleitores WHERE chave_acesso_cifrada = %s AND prefixo_cpf = %s AND titulo_eleitor = %s AND mesario = 1"""
                    valores = [chave_cifrada, prefixo_cpf, titulo]
                    resultado = buscar(comando, valores)

                    #verifica se encontrou um mesário válido
                    if resultado:
                        
                        #Confirma se a chave armazenada é igual à informada
                        if resultado[6] == chave_cifrada:
                            print("mesário autorizado")

                            #======================================================
                            # VERIFICAÇÃO DE INTEGRIDADE
                            #======================================================

                            #Conta quantos eleitores já estão marcados como votantes
                            comando = """ SELECT COUNT(*) FROM eleitores WHERE  ja_votou = 1 """
                            resultado_votos = buscar(comando, [])
                            
                            votos = resultado_votos[0]

                            
                            print(f"Total de votos registrados:{votos}")

                            
                            if votos > 0:
                                print("\nHouve uma anomalia no sistema, a urna não pode ser aberta.")
                            else:

                                #==================================================
                                # ABERTURA OFICIAL DA URNA
                                #==================================================

                                urna_aberta = True
                                registrar_log("ABERTURA: Votação iniciada com sucesso. Total de votos zerado.")
                                print("\nUrna liberada para votação.")

                                #==================================================
                                # MENU INTERNO DA URNA
                                # =================================================

                                opcao = 0
                                while opcao != 2:
                                    print("\n=== Votacao ===")
                                    print("1 - Votar")
                                    print("2 - Encerrar votacao")
                                    try:
                                        opcao = int(input("Escolha uma opcao: "))
                                    except ValueError:
                                        opcao = 0
                                    match opcao:
                                        case 1:
                                            # Inicia o processo completo de votação
                                            votar()
                                        case 2:
                                            # Inicia protocolo de encerramento
                                            menu_encerramento(urna_aberta)
                                
                        else:
                            #Chave não corresponde à armazenada
                            print("Chave incorreta")
                            registrar_log( "Tentativa de Acesso Negado")
                    else:
                        #Nenhum mesário foi encontrado com os dados informados
                        print("Mesário não autorizado")
                        registrar_log("Tentativa de Acesso Negado")
            case 2:
                menu_auditoria()

            case 3:
                menu_resultados()

            case 4:
                menu_principal()
                print("Voltando ao menu principal...")
            case _:
                print("Opcao invalida.")

def votar():
    """
    Executa o fluxo completo de votação e autenticação multifator do eleitor.

    A função valida o acesso em etapas sequenciais consultando o banco de dados: 
    prefixo do CPF (com trava de voto duplo), Título de Eleitor e validação de 
    assinatura criptográfica (Cifra de Hill). Após a liberação, realiza a consulta 
    do candidato, confirmação de voto (nominal ou nulo), gravação dos dados, 
    registro de logs e emissão do protocolo.

    Requisitos Atendidos:
        - RF004.01: Autenticação multifator do eleitor (CPF, Título, Chave Cifrada).
        - RF004.02: Computação, persistência de voto e emissão de protocolo seguro.

    Returns:
        None
    """
    print("\n === VOTAR ===")
    #==============================================
    # VALIDAÇÃO DO CPF DO ELEITOR
    #==============================================
    verificar_cpf = 0

    #continua pedindo o CPF enquanto não encontrar nenhum eleitor válido
    while verificar_cpf == 0:
        cpf =input("Seu primeiros 4 digitos do CPF: ")
        #Busca o eleitor pelo prefixo do CPF
        comando = "SELECT nome, ja_votou FROM eleitores WHERE prefixo_cpf = %s"
        resultado = buscar(comando, [cpf])

        #Caso não encontre o CPF
        if resultado == None:
            registrar_log("ALERTA: Tentativa de Acesso Negado")
            print("CPF não encontrado. Tente novamente.")

        #Caso o eleitor já tenha votado
        elif resultado[1] == 1:
            registrar_log("ALERTA: Tentativa de voto duplo")
            print(f"Eleitor {resultado[0]} já votou. Você não pode votar novamente.")
        
        #CPF válido e eleitor apto pra votar
        else:
            print(f"CPF válido!")
            verificar_cpf = 1
            
    #===============================================
    # VALIDAÇÃO DO TÍTULO DE ELEITOR
    #===============================================

    verificar_titulo = 0

    #Continua solicitando o título até encontrar um correspondente
    while verificar_titulo == 0:

        titulo_eleitor = input("Digite o Título de Eleitor: ")

        #Verifica se o título pertence ao CPF informado anteriormente
        comando = "SELECT nome FROM eleitores WHERE prefixo_cpf = %s AND titulo_eleitor = %s"
        resultado = buscar(comando, [cpf, titulo_eleitor])

        if resultado:
            print(f"Título de Eleitor válido!")
            verificar_titulo = 1

        else:
            print("Título de Eleitor inválido. Tente novamente.")
            registrar_log("ALERTA: Tentativa de Acesso Negado")

    #=================================================
    # VALIDAÇÃO DA CHAVE DE ACESSO
    #=================================================
            
    verificar_chave = 0

    #Continua solicitando a chave até que ela seja validada
    while verificar_chave == 0:

        chave = input("Digite sua chave de acesso: ")

        #Criptografia da chave digitada para comparar com o banco
        chave_cifrada = criptografar_hill(chave)  

        comando = "SELECT nome, chave_acesso_cifrada FROM eleitores WHERE chave_acesso_cifrada = %s"
        resultado = buscar(comando, [chave_cifrada])

        #Confirma se a chave existe no banco
        if resultado[1] == chave_cifrada:
            print(f"Chave correta! Você pode votar, bem vindo {resultado[0]}!")
            verificar_chave = 1
        else:
            print("Chave incorreta. Tente novamente.")
            registrar_log("ALERTA: Tentativa de Acesso Negado")

    #================================
    # PROCESSO DE VOTAÇÃO
    #================================
            
    parte_final = 0

    #Continua até que o voto seja registrado
    while parte_final == 0:
        numero_candidatoB = int(input("Digite o número do candidato:"))

        #Busca informações do candidato digitado
        comando = """
        SELECT c.candidato, p.partido, p.sigla
        FROM candidatos c
        JOIN partidos p ON c.id_partido = p.id_partido
        WHERE c.numero_votacao = %s
        """

        valores = [numero_candidatoB]
        resultado = buscar(comando, valores)

    #======================================
    # CANDIDATO ENCONTRADO
    #======================================
        if resultado:
            print("\n--- INFORMAÇÕES DO CANDIDATO ---")
            print(f"Nome: {resultado[0]}")
            print(f"Partido: {resultado[1]}")
            print(f"Sigla: {resultado[2]}")

            #Confirmação do voto
            confirmacao = input("Deseja confirmar seu voto para este candidato? (1 para Sim/2 para Não)")

            if confirmacao == "1":

                #Marca o eleitor como já votou
                comando = "UPDATE eleitores SET ja_votou = 1 WHERE prefixo_cpf = %s"
                valores = [cpf]
                executar(comando, valores)

                #Gera o protocolo único de votação
                protocolo = gerar_protocolo(numero_candidatoB)
                #Criptografa o protocolo antes de armazenar
                protocolo_cifrado = criptografar_hill(protocolo)
                #Obtém data e hora atual do voto
                horario_voto = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                #Registra o voto no banco
                comando_2 = "INSERT INTO votos (id_candidato, datetime_voto, protocolo_votacao_cifrado) VALUES ((SELECT id_candidato FROM candidatos WHERE numero_votacao = %s), %s, %s)"
                executar(comando_2, [numero_candidatoB, horario_voto, protocolo_cifrado]) 
                print(f"Voto registrado no candidato: {resultado[0]} com sucesso!")

                #Registra o evento na auditoria
                registrar_log(f"SUCESSO: Voto realizado com sucesso")
                #Exibe o protocolo ao eleitor
                print(f"Protocolo de votação: {protocolo}")

                parte_final = 1
            elif confirmacao == "2":
                print("Voto cancelado. Você pode escolher outro candidato.")
        #=====================
        # VOTO NULO
        #=====================

        else:

            confirmacao = input("Candidato nao encontrado, deseja votar nulo? (1 para Sim/2 para Não):")

            if confirmacao == "1":

                #Marca o eleitor como votante 
                comando = "UPDATE eleitores SET ja_votou = 1 WHERE prefixo_cpf = %s"
                valores = [cpf]
                executar(comando, valores)

                #Gera o protocolo para voto nulo
                protocolo = gerar_protocolo("NULO")
                protocolo_cifrado = criptografar_hill(protocolo)

                horario_voto = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                #Salva o voto nulo
                comando_2 = "INSERT INTO votos (voto_nulo, datetime_voto, protocolo_votacao_cifrado) VALUES (1, %s, %s)"
                executar(comando_2, [horario_voto, protocolo_cifrado])
                print("Voto nulo registrado com sucesso!")

                parte_final = 1
                registrar_log("SUCESSO: Voto nulo registrado com sucesso.")
                print(f"Protocolo de votação: {protocolo}")
def menu_principal():
    """
    é o painel de navegação principal.

    Gerencia o fluxo de controle de telas direcionando o usuário para os submenus 
    de gerenciamento e votação.

    Requisitos Atendidos:
        - RF000.01: Painel principal de controle e navegação do sistema.

    Returns:
        None
    """
    opcao = 0
    while opcao != 3:
        print("\n=== SISTEMA LAD.PY ===")
        print("1 - Gerenciamento")
        print("2 - Votacao")
        print("3 - Sair")
        try:
            opcao = int(input("Escolha uma opcao: "))
        except ValueError:
            opcao = 0

        match opcao:
            case 1:
                menu_gerenciamento()
            case 2:
                menu_votacao()
            case 3:
                print("Saindo...")
            case _:
                print("Opcao invalida.")
menu_principal()

    
