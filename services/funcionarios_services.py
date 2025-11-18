import time
from psycopg2.errors import UniqueViolation
from config.database import conectar_banco
from services import pause

def login(cpf, senha):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "SELECT * FROM FUNCIONARIOS WHERE cpf_funcionario = %s and senha = %s and ativo = true"
        cursor.execute(sql, (cpf, senha))
        user = cursor.fetchone() # retorna somente um
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
        con.rollback()
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

def desativar_funcionario(cpf):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "UPDATE FUNCIONARIOS SET ativo = false WHERE cpf_funcionario = %s"
        cursor.execute(sql, (cpf,)) # tem que ter , pra ser enviado com tupla
        con.commit()
        if cursor.rowcount > 0: # rowcount conta quantas linhas foram alteradas no update
            print(f"Funcionário {cpf} desativado com sucesso!")
        else:
            print("Nenhum Funcionário Encontrado")
    except Exception as erro:
        con.rollback()
        print(f"Erro: {erro}")
    finally:
        cursor.close()
        con.close()

def reativar_funcionario(cpf):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "UPDATE FUNCIONARIOS SET ativo = true WHERE cpf_funcionario = %s"
        cursor.execute(sql, (cpf,))
        con.commit()
        if cursor.rowcount > 0:
            print(f"Funcionário {cpf} reativado com sucesso!")
        else:
            print("Nenhum Funcionário Encontrado")     
    except Exception as erro:
        con.rollback()
        print(f"Erro: {erro}")
    finally:
        cursor.close()
        con.close()