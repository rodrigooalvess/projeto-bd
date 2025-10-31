from config.database import conectar_banco

def cadastrar_cliente(nome, cpf, endereco = 'Sem Endereço'):
    conn = conectar_banco()
    try:
        cursor = conn.cursor()
        query = 'INSERT INTO CLIENTES (nome_cliente, cpf_cliente, endereco) values (%s, %s, %s)'
        cursor.execute(query, (nome, cpf, endereco))
        conn.commit()
        print('Cliente cadastrado com sucesso!')
    except Exception as erro:
        print(f'Erro ao cadastrar cliente: {erro}')
    finally:
        cursor.close()
        conn.close()
        