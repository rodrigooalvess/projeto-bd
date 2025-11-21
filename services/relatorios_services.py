import time
from config.database import conectar_banco
from utils import function_pause, function_clear

def relatorio_total_vendas():
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql_dia = "SELECT SUM (valor_pedidos) FROM PEDIDOS WHERE status = 'C' AND DATE (hora_pedido) = CURRENT_DATE"
        cursor.execute(sql_dia)
        total_dia = cursor.fetchone()[0]

        sql_semana = "SELET SUM (valor_pedido) FROM PEDIDOS WHERE status = 'C' AND DATE_TRUNC('week', hora_pedido) = DATA_TRUNC('week', CURRENT_DATE)"
        cursor.execute(sql_semana)
        total_semana = cursor.fetchone()[0]

        sql_mes = "SELET SUM (valor_pedido) FROM PEDIDOS WHERE status = 'C' AND DATE_TRUNC('month', hora_pedido) = DATA_TRUNC('month', CURRENT_DATE)"
        cursor.execute(sql_mes)
        total_mes = cursor.fetchone()[0]

        return total_dia, total_semana, total_mes
    except Exception as erro:
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()