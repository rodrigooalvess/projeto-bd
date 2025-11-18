import time
from psycopg2.errors import UniqueViolation
from config.database import conectar_banco
from services import pause

def login(cpf, senha):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "SELECT cargo FROM FUNCIONARIOS WHERE cpf_funcionario = %s and senha = %s"
        cursor.execute(sql, (cpf, senha))
        user = cursor.fetchone()
        #[id, nome, cpf, cargo, senha] or None
        return user
    except Exception as erro:
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

def cadastro_funcionario(nome: str, cpf: str, cargo: str, senha: str):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "INSERT INTO FUNCIONARIOS (nome_funcionario, cpf_funcionario, senha, cargo) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nome, cpf, senha, cargo))
        con.commit()
        print(f"Usuário {cpf} cadastrado com sucesso !")

    except UniqueViolation:
        print(f"Erro: CPF {cpf} já cadstrado")
        con.rollback() #desfaz tudo que estava sendo feito na transação atual (commit) e retorna ao estado antes dela começar.
        time.sleep(3)
    except Exception as erro:
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

def listar_funcionarios():
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "SELECT id_funcionario, nome_funcionario FROM FUNCIONARIOS ORDER BY cargo"
        cursor.execute(sql)
        users = cursor.fetchall()
        #[(id1, nome1), (id2,nome2), ...]
        if users:
            print("-----LISTANDO FUNCIONARIOS-----")
            for id, nome in users:
                print(f"{id} - {nome}")
            pause()
        elif not users:
            print("Nenhum Funcionário Cadastrado")
            time.sleep(3)
    except Exception as erro:
        print(f"Erro: {erro}")
        time.sleep(3)
    finally:
        cursor.close()
        con.close()

#def excluir_funcionario():
#    try:
#        con = conectar_banco()
#        cursor = con.cursor()
#
#       sql = "DELET FROM FUNCIONARIOS WHERE cpf_funcionario = %s"
#        cursor.execute(sql)
#        users = cursor.fetchall()
#        #[(id1, nome1), (id2,nome2), ...]
#        if users:
#            for id, nome in users:
#                print(f"{id} - {nome}")
#        elif not users:
#            print("Nenhum Funcionário Cadastrado")
#    except Exception as erro:
#        print(f"Erro: {erro}")
#    finally:
#        cursor.close()
#        con.close()