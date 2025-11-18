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

def listar_produtos_ativos():
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "SELECT id_produto, nome_produto, valor_produto FROM PRODUTOS WHERE ativo = true ORDER BY categoria"
        cursor.execute(sql)
        produtos = cursor.fetchall()
        for id, nome, valor in produtos:
            print(f"{id} - {nome} - R${valor:.2f}")
    except Exception as erro:
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

def alterar_produto(id, valor_novo):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "UPDATE PRODUTOS SET valor_produto = %s WHERE id_produto =%s"
        cursor.execute(sql, (valor_novo, id))
        con.commit()

        print("Valor atualizado com sucesso")
        time.sleep(3)
    except Exception as erro:
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

def listar_produtos_inativos():
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "SELECT id_produto, nome_produto, valor_produto FROM PRODUTOS WHERE ativo = false ORDER BY categoria"
        cursor.execute(sql)
        produtos = cursor.fetchall()
        for id, nome, valor in produtos:
            print(f"{id} - {nome} - R${valor:.2f}")
    except Exception as erro:
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

def desativar_produto(id):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "UPDATE PRODUTOS SET ativo = false WHERE id_produto = %s"
        cursor.execute(sql, (id))
        con.commit()
        if cursor.rowcount > 0: # rowcount conta quantas linhas foram alteradas no update
            print("Produto desativado com sucesso!")
        else:
            print("Nenhum Produto Encontrado!")
    except Exception as erro:
        con.rollback()
        print(f"Erro: {erro}")
    finally:
        cursor.close()
        con.close()

def reativar_produto(id):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "UPDATE PRODUTOS SET ativo = true WHERE id_produto = %s"
        cursor.execute(sql, (id))
        con.commit()
        if cursor.rowcount > 0: # rowcount conta quantas linhas foram alteradas no update
            print("Produto reativado com sucesso!")
        else:
            print("Nenhum Produto Encontrado!")
    except Exception as erro:
        con.rollback()
        print(f"Erro: {erro}")
    finally:
        cursor.close()
        con.close()