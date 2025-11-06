from config.database import conectar_banco


def login(cpf, senha):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        sql = "SELECT * FROM FUNCIONARIOS WHERE cpf_funcionario = %s and senha = %s"
        cursor.execute(sql, (cpf, senha))
        user = cursor.fetchone()
        #[id, nome, cpf, cargo, senha]
        return user 
    except Exception as erro:
        print(f"Erro: {erro}")
    finally:
        cursor.close()
        con.close()

