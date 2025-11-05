from psycopg2.errors import UniqueViolation
from config.database import conectar_banco

def cadastro_funcionario(nome: str, cpf: str, cargo: str):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "INSERT INTO FUNCIONARIOS (nome_funcionario, cpf_funcionario, cargo) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, cpf, cargo))
        con.commit()
        print(f"Usuário {cpf} cadastrado com sucesso !")

    except UniqueViolation:
        print(f"Erro: CPF {cpf} já cadstrado")
        con.rollback() #desfaz tudo que estava sendo feito na transação atual (commit) e retorna ao estado antes dela começar.
    except Exception as erro:
        print(f"Erro: {erro}")
    finally:
        cursor.close()
        con.close()