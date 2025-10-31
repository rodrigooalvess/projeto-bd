import psycopg2

#configuração de conexão

def conectar_banco():
    
    try:
        conn = psycopg2.connect(
            host = 'localhost',
            dbname = 'flowcoffee',
            user = 'postgres',
            password = '26172107',
            port = '5432'
        )
        print('Banco de dados conectado com sucesso!')
        return conn
    
    except psycopg2.Error as erro:
        print(f'Erro ao conectar banco de dados: {erro}')
        return None