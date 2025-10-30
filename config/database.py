import psycopg2

#configuração de conexão

def conectar_banco():
    
    try:
        conexao = psycopg2.connect(
            host = 'localhost',
            database = 'flowcoffee',
            user = 'postgres',
            password = '26172107'
        )
        print('Banco de dados conectado com sucesso!')
        return conexao
    
    except psycopg2.Error as erro:
        print(f'Erro ao conectar banco de dados: {erro}')
        return None