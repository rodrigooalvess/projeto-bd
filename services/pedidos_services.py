from config.database import conectar_banco
import time

def cadastrar_pedido(id_cliente: int, id_funcionario: int, modalidade: str):
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

def pagamento_pedido(modo_de_pagamento, id_pedido):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "UPDATE PEDIDOS SET pagamento = (%s) WHERE id_pedido = %s"
        cursor.execute(sql, (modo_de_pagamento, id_pedido))
        con.commit()

        print("Pagamento Realizado Com Sucesso!")

        time.sleep(3)
    except Exception as erro:
        print(f"Erro: {erro}")
        con.rollback()
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

def produtos_pedido(id_pedido, id_produto, quantidade, obs = ""):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "INSERT INTO PRODUTOS_PEDIDOS (id_pedido, id_produto, quantidade, observacao) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (id_pedido, id_produto, quantidade, obs))
        con.commit()

    except Exception as erro:
        con.rollback()
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

def procurar_id_pedido(cpf):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "SELECT p.id_pedido FROM PEDIDOS p INNER JOIN CLIENTES c on p.id_cliente = c.id_cliente WHERE c.cpf_cliente = %s and p.status = 'P'"
        cursor.execute(sql, (cpf,))
        id_pedido_encontrado = cursor.fetchone()[0]

        if id_pedido_encontrado:
            return id_pedido_encontrado
        else:
            print("Pedido Não Encontrado!")
            return None
    except Exception as erro:
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

def mostrar_resumo_pedido(id_pedido):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "SELECT pr.nome_produto, pp.quantidade, (pp.quantidade*pr.valor_produto) as total_item FROM PRODUTOS pr INNER JOIN PRODUTOS_PEDIDOS pp ON pr.id_produto = pp.id_produto WHERE pp.id_pedido = %s"
        cursor.execute(sql, (id_pedido,))
        resumo = cursor.fetchall()
        return resumo

    except Exception as erro:
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

def calcular_valor_pedido(id_pedido):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "SELECT SUM(pr.valor_produto * pp.quantidade) AS total FROM PRODUTOS_PEDIDOS pp INNER JOIN PRODUTOS pr ON pr.id_produto = pp.id_produto WHERE pp.id_pedido = %s"
        cursor.execute(sql, (id_pedido,))

        total = cursor.fetchone()[0] # pega o valor da primeira coluna no cso a coluna 0

        sql_update_pedido = "UPDATE PEDIDOS SET valor_pedido = %s WHERE id_pedido = %s"
        cursor.execute(sql_update_pedido, (total, id_pedido))
        con.commit()

        return total

    except Exception as erro:
        con.rollback()
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

def listar_pedidos_pendentes():
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "SELECT p.id_pedido, c.cpf_cliente, p.valor_pedido, p.modalidade FROM PEDIDOS p INNER JOIN CLIENTES c ON p.id_cliente = c.id_cliente WHERE p.status = 'P' ORDER BY p.hora_pedido"
        cursor.execute(sql)
        pedidos = cursor.fetchall()
        return pedidos

    except Exception as erro:
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

def listar_pedidos_entregar():
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "SELECT p.id_pedido, c.cpf_cliente, p.valor_pedido, c.endereco FROM PEDIDOS p INNER JOIN CLIENTES c ON p.id_cliente = c.id_cliente WHERE p.satus = 'P' and p.modalidade = 'E' ORDER BY p.hora_pedido"
        cursor.execute(sql)
        pedidos = cursor.fetchall()
        return pedidos

    except Exception as erro:
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

def associar_pedido_delivery(id_pedido):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "INSERT INTO DELIVERY (id_pedido) VALUES (%s)"
        cursor.execute(sql, (id_pedido,))
        con.commit()

    except Exception as erro:
        con.rollback()
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

def associar_pedido_entregador(id_pedido, id_entregador):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "UPDATE DELIVERY SET id_funcionario = %s WHERE id_pedido = %s"
        cursor.execute(sql, (id_entregador, id_pedido))
        con.commit()

    except Exception as erro:
        con.rollback()
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

def buscar_pedido(id_cliente):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql1 = "SELECT id_pedido FROM PEDIDOS WHERE id_cliente = %s and status = 'P'"
        cursor.execute(sql1, (id_cliente,))
        id_pedido = cursor.fetchone()
        if not id_pedido: return None

        sql = "SELECT pp.id_pedido, pr.nome_produto, pp.quantidade, (pp.quantidade*pr.valor_produto) as total_item FROM PRODUTOS pr INNER JOIN PRODUTOS_PEDIDOS pp ON pr.id_produto = pp.id_produto WHERE pp.id_pedido = %s AND pp.id_cliente = %s"
        cursor.execute(sql, (id_pedido, id_cliente))
        resumo = cursor.fetchall()
        return resumo

    except Exception as erro:
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

def cancelar_pedido(id_pedido, id_cliente):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "UPDATE PEDIDOS SET status = 'X' WHERE id_pedido = %s AND status != 'C' AND id_cliente = %s"
        cursor.execute(sql, (id_pedido, id_cliente))
        con.commit()

        print(f"Pedido#{id_pedido} CANCELADO!")
        time.sleep(3)

    except Exception as erro:
        con.rollback()
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

def finalizar_pedido(id_pedido):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "UPDATE PEDIDOS SET status = 'C' WHERE id_pedido = %s AND status != 'X'"
        cursor.execute(sql, (id_pedido,))
        con.commit()

        print(f"Pedido#{id_pedido} FINALIZADO!")
        time.sleep(3)

    except Exception as erro:
        con.rollback()
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()