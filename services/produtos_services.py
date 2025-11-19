import time
from psycopg2.errors import UniqueViolation
from config.database import conectar_banco

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

def alterar_valor_produto(id: int, valor_novo: float):
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

def desativar_produto(id: int):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "UPDATE PRODUTOS SET ativo = false WHERE id_produto = %s"
        cursor.execute(sql, (id,))
        con.commit()
        if cursor.rowcount > 0: # rowcount conta quantas linhas foram alteradas no update
            print("Produto desativado com sucesso!")
        else:
            print("Nenhum Produto Encontrado!")
    except Exception as erro:
        con.rollback()
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

def reativar_produto(id: int):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "UPDATE PRODUTOS SET ativo = true WHERE id_produto = %s"
        cursor.execute(sql, (id,))
        con.commit()
        if cursor.rowcount > 0: # rowcount conta quantas linhas foram alteradas no update
            print("Produto reativado com sucesso!")
        else:
            print("Nenhum Produto Encontrado!")
    except Exception as erro:
        con.rollback()
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

def procurar_produto(nome):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "SELECT id_produto, nome_produto, valor_produto FROM PRODUTOS WHERE nome_produto ILIKE %s"
        nome = f"%{nome}"
        cursor.execute(sql, (nome,))
        busca_resultado = cursor.fetchall() #[(id1, nome1, ...)...]
        return busca_resultado
    except Exception as erro:
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

#ESTUDAR POIS GPT QUE FEZ
def cardapio():
    
    RESET = "\033[0m"
    BOLD = "\033[1m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    BLUE = "\033[94m"

    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "SELECT id_produto, nome_produto, descricao, valor_produto, categoria FROM PRODUTOS WHERE ativo = true ORDER BY categoria, nome_produto"
        cursor.execute(sql)
        produtos = cursor.fetchall()
        categorias = {
            "C": (f"{CYAN}{BOLD}☕ CAFÉS{RESET}", []),
            "B": (f"{BLUE}{BOLD}🥤 BEBIDAS{RESET}", []),
            "D": (f"{MAGENTA}{BOLD}🍰 DOCES{RESET}", []),
            "S": (f"{YELLOW}{BOLD}🥪 SALGADOS{RESET}", []),
        }
        for p in produtos:
            categorias[p[4]][1].append(p)
        
        print("\n" + "=" * 60)
        print(f"{GREEN}{BOLD}{'CARDÁPIO DA CAFETERIA':^60}{RESET}")
        print("=" * 60)

        for cat, (titulo, items) in categorias.items():
            if not items:
                continue

            print(f"\n{titulo}")
            print("-" * 60)

            for idp, nome, desc, preco, categoria in items:
                print(f"{BOLD}{nome.upper()}{RESET}  -  R$ {preco:.2f}")
                print(f"   {desc}\n")

        print("=" * 60)
    except Exception as erro:
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

# def cardapio():
    
#     try:
#         con = conectar_banco()
#         cursor = con.cursor()

#         sql = "SELECT id_produto, nome_produto, descricao, valor_produto, categoria FROM PRODUTOS WHERE ativo = true ORDER BY categoria, nome_produto"
#         cursor.execute(sql)
#         produtos = cursor.fetchall()
#         #[(idp1, nomep1, descp1, valorp1, categoriap1), (p2)...]
#         print("---CAFÉS---")
#         for id, nome, desc, valor, categoria in produtos:
#             if categoria == 'C':
#                 print(f"{id} - {nome} - R${valor:.2f}\n{desc}")
#         print("---BEBIDAS---")
#         for id, nome, desc, valor, categoria in produtos:
#             if categoria == 'B':
#                 print(f"{id} - {nome} - R${valor:.2f}")
#         print("---SALGADOS---")
#         for id, nome, desc, valor, categoria in produtos:
#             if categoria == 'S':
#                 print(f"{id} - {nome} - R${valor:.2f}\n{desc}")
#         print("---DOCES---")
#         for id, nome, desc, valor, categoria in produtos:
#             if categoria == 'D':
#                 print(f"{id} - {nome} - R${valor:.2f}\n{desc}")
#     except Exception as erro:
#         print(f"Erro: {erro}")
#     finally:
#         cursor.close()
#         con.close()
   