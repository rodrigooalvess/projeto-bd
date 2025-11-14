from config.database import conectar_banco
import time

def cadastrar_pedido():
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "INSERT INTO PRODUTOS (nome_produto, categoria, valor_produto) values (%s, %s, %s)"
        cursor.execute(sql, (nome, categoria, valor))
        con.commit()

        time.sleep(3)
    except Exception:
        print("Erro, Produto Já Cadastrado")
        con.rollback()
        time.sleep(3)
    finally:
        cursor.close()
        con.close() 