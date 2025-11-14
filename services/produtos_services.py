import time
from psycopg2.errors import UniqueViolation
from config.database import conectar_banco
from services import pause

def cadastrar_produto(nome: str, categoria: str, valor: float):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "INSERT INTO PRODUTOS (nome_produto, categoria, valor_produto) values (%s, %s, %s)"
        cursor.execute(sql, (nome, categoria, valor))
        con.commit()

        print(f"{nome} cadastrado com sucesso")
        time.sleep(3)
    except UniqueViolation:
        print("Erro, Produto Já Cadastrado")
        con.rollback()
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

