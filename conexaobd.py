import mysql.connector

def testar_conexao():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ademir",
            database="lad_py",
            auth_plugin='mysql_native_password'
        )
        if conexao.is_connected():
            print("Conexao com o banco realizada com sucesso.")
            conexao.close()
        else:
            print("Nao foi possivel conectar com o banco.")
    except mysql.connector.Error as erro:
        print("Erro ao conectar com o banco:", erro)

def executar(comando, valores):
    conexao = mysql.connector.connect(
        host="localhost", 
        user="root", 
        password="ademir",
        database="lad_py",
        auth_plugin='mysql_native_password'
    )
    cursor = conexao.cursor()
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def buscar(comando, valores):
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ademir",
        database="lad_py",
        auth_plugin='mysql_native_password'
    )
    cursor = conexao.cursor()
    cursor.execute(comando, valores)
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado