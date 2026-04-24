import mysql.connector
def testar_conexao():
    try:
        conexao = mysql.connector.connect(
            host="localhost", #sua hospedagem de rede (localhost ou 127.0.0.1 por padrão)
            user="root", #seu usuario no mysql server (root é o padrão por maquina, se nunca utilizou mysql server antes, deixe do jeito que está)
            password="senha", #sua senha
            database="lad_py" #não alterar, nome da database de banco.sql
        )
        if conexao.is_connected():
            print("Conexao com o banco realizada com sucesso.")
            conexao.close()
        else:
            print("Nao foi possivel conectar com o banco.")

    except mysql.connector.Error as erro:
        print("Erro ao conectar com o banco:", erro)
def executar(comando,valores):
    # Cria conexão com o banco, necessária para usar o cursor e executar SQL
    conexao = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="senha", 
            database="lad_py" 
        )
    cursor=conexao.cursor() #cria um cursor para executar comandos SQL no banco
    cursor.execute=(comando,valores) #executa o comando SQL usando os valores informados
    conexao.commit() #salva as alterações no banco de dados
    cursor.close() #fecha o cursor após executar as operações no banco

