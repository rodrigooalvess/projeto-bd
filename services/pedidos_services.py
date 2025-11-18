from config.database import conectar_banco
import time

def cadastrar_pedido(id_cliente, id_funcionario, modalidade):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "INSERT INTO PEDIDOS (id_cliente, id_funcionario, modalidade) values (%s, %s, %s)"
        cursor.execute(sql, (id_cliente, id_funcionario, modalidade))
        con.commit()

        print("Pedido Criado com Sucesso!")

        time.sleep(3)
    except Exception as erro:
        print(f"Erro: {erro}")
        con.rollback()
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

def produtos_pedido():
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "INSERT INTO PRODUTOS_PEDIDOS (id_pedido, id_produto, quantidade, observacao) VALUES (%s, %s, %s, %s)"

    except Exception:
        print("teste")
    finally:
        cursor.close()
        con.close()

def procurar_pedido(cpf):
    pass