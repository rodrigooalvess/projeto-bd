import bcrypt

def criptografar_senha(senha):
    senha_bytes = senha.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(senha_bytes, salt)

    return hashed 

def verificar_senha(senha, hashed):
    senha_bytes = senha.encode("utf-8")
    return bcrypt.checkpw(senha_bytes, hashed)