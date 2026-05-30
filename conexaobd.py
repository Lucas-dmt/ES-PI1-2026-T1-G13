import mysql.connector
def testar_conexao():
    """
    Realiza um teste de comunicação imediato com o servidor MySQL.

    Tenta abrir e fechar uma conexão curta utilizando as credenciais definidas. 
    Serve como diagnóstico inicial para verificar se o serviço de banco de dados 
    está ativo antes de liberar a execução do resto do programa.

    Requisitos Atendidos:
        - RF006.01: Módulo de Banco de Dados - Homologação de conectividade com o servidor.

    Returns:
        None
    """
    try:
        conexao = mysql.connector.connect(
            host="localhost", #sua hospedagem de rede (localhost ou 127.0.0.1 por padrão)
            user="root", #seu usuario no mysql server (root é o padrão por maquina, se nunca utilizou mysql server antes, deixe do jeito que está)
            password="ademir", #sua senha
            database="lad_py", #não alterar, nome da database de banco.sql
            auth_plugin='mysql_native_password'
        )
        if conexao.is_connected():
            print("Conexao com o banco realizada com sucesso.")
            conexao.close()
        else:
            print("Nao foi possivel conectar com o banco.")

    except mysql.connector.Error as erro:
        print("Erro ao conectar com o banco:", erro)
def executar(comando,valores):
    """
    Executa comandos SQL de mutação de dados (INSERT, UPDATE, DELETE) no banco de dados.

    Abre uma conexão temporária, inicializa um cursor do driver e aplica os valores 
    parametrizados para evitar injeção de SQL. Efetua a gravação permanente das 
    alterações por meio de uma operação de commit.

    Requisitos Atendidos:
        - RF006.02: Módulo de Banco de Dados - Persistência, atualização e mutação de registros.

    Args:
        comando (str): Instrução SQL de escrita a ser enviada ao servidor.
        valores (lista): Dados que preencherão os marcadores parametrizados (%s).

    Returns:
        None
    """
    # Cria conexão com o banco, necessária para usar o cursor e executar SQL
    conexao = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="ademir",
            database="lad_py",
            auth_plugin='mysql_native_password'
        )
    cursor=conexao.cursor() #cria um cursor para executar comandos SQL no banco
    cursor.execute(comando,valores) #executa o comando SQL usando os valores informados
    conexao.commit() #salva as alterações no banco de dados
    cursor.close() #fecha o cursor após executar as operações no banco

def buscar(comando, valores):
     """
     Executa uma consulta SQL projetada para extrair apenas um único registro (linha) do banco.

     Estabelece o canal de comunicação, alimenta os parâmetros e utiliza o método fetchone 
     para recuperar a primeira ocorrência compatível, fechando todos os recursos na sequência.

     Requisitos Atendidos:
         - RF006.03: Módulo de Banco de Dados - Consulta pontual e verificação de registro único.

     Args:
         comando (str): Instrução SQL de consulta (SELECT).
         valores (list/tuple): Parâmetros para os filtros da cláusula WHERE.

     Returns:
         resultado: Uma tupla contendo as colunas recuperadas ou None se nada for localizado.
     """
     conexao = mysql.connector.connect(
            host="localhost", #sua hospedagem de rede (localhost ou 127.0.0.1 por padrão)
            user="root", #seu usuario no mysql server (root é o padrão por maquina, se nunca utilizou mysql server antes, deixe do jeito que está)
            password="ademir", #sua senha
            database="lad_py", #não alterar, nome da database de banco.sql
            auth_plugin='mysql_native_password'
        )
     cursor=conexao.cursor()
     cursor.execute(comando, valores)
     resultado = cursor.fetchone()
     cursor.close()
     conexao.close()
     return resultado

def buscar_tudo(comando, valores=[]):
    """
    Executa uma consulta SQL projetada para extrair coleções completas de dados.

    Funciona de forma similar à busca unitária, porém emprega o método fetchall para colher 
    e construir uma lista matricial contendo todas as linhas compatíveis com os filtros.

    Requisitos Atendidos:
        - RF006.04: Módulo de Banco de Dados - Consulta em lote e listagem de múltiplos registros.

    Args:
        comando (str): Instrução SQL de listagem (SELECT).
        valores (lista): Parâmetros estruturais de filtragem. Padrão é [].

    Returns:
        resultado: Lista contendo tuplas de dados correspondentes aos registros retornados.
    """
    conexao = mysql.connector.connect(
        host="localhost", 
        user="root", 
        password="ademir", 
        database="lad_py", 
        auth_plugin='mysql_native_password'
    )
    cursor = conexao.cursor()
    cursor.execute(comando, valores)
    resultado = cursor.fetchall()  # Captura todas as linhas da consulta
    cursor.close()
    conexao.close()
    return resultado
