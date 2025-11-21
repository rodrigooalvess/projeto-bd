from config.database import conectar_banco
from psycopg2.errors import UniqueViolation
import time
from utils import function_pause


def cadastrar_cliente(nome: str, cpf: str, endereco: str = "Sem Endereço"):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "INSERT INTO CLIENTES (nome_cliente, cpf_cliente, endereco) values (%s, %s, %s)"
        cursor.execute(sql, (nome, cpf, endereco))
        con.commit()

        print(f"Cliente {cpf} cadastrado com sucesso!")
        time.sleep(3)
    except UniqueViolation:
        con.rollback()
        print(f"Cliente {cpf} já cadastrado")
        time.sleep(3)
    except Exception as erro:
        print(f"Erro ao cadastrar cliente: {erro}")
        time.sleep(3)
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
        time.sleep(3)
    except Exception as erro:
        con.rollback()
        print(f"Erro ao atualizar endereço do cliente: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

def procurar_id_cliente(cpf):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "SELECT id_cliente FROM CLIENTES WHERE cpf_cliente = %s"
        cursor.execute(sql, (cpf,))

        id_cliente = cursor.fetchone()[0]
        
        if id_cliente:
            return id_cliente
        else:
            return None
    except Exception as erro:
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

def listar_clientes():
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "SELECT id_cliente, nome_cliente, cpf_cliente FROM CLIENTES ORDER BY id_cliente"
        cursor.execute(sql)
        users = cursor.fetchall()
        #[(id1, nome1, cpf1), (id2, nome2, cpf2), ...]
        if users:
            print("-----LISTANDO CLIENTES-----")
            for id, nome, cpf in users:
                print(f"{id} - {nome} - {cpf}")
            function_pause()
        elif not users:
            print("Nenhum Cliente Cadastrado")
            time.sleep(3)
    except Exception as erro:
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()
