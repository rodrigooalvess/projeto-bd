from config.database import conectar_banco
from psycopg2.errors import UniqueViolation

def cadastrar_cliente(nome: str, cpf: str, endereco: str = "Sem Endereço"):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "INSERT INTO CLIENTES (nome_cliente, cpf_cliente, endereco) values (%s, %s, %s)"
        cursor.execute(sql, (nome, cpf, endereco))
        con.commit()

        print(f"Cliente {cpf} cadastrado com sucesso!")
    except UniqueViolation:
        print(f"Cliente {cpf} já cadastrado")
    except Exception as erro:
        print(f"Erro ao cadastrar cliente: {erro}")
    finally:
        cursor.close()
        con.close()

def atualizar_endereco(id_cliente: int, endereco: str):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "UPDATE CLIENTES SET endereco = %s WHERE id_cliente = %s"
        cursor.execute(sql, (endereco, id_cliente))
        con.commit()

        print(f"Endereço atualizado com sucesso!")
    except Exception as erro:
        print(f"Erro ao atualizar dados do cliente: {erro}")
    finally:
        cursor.close()
        con.close()