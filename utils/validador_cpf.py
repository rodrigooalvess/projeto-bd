from utils import function_clear

def validar_cpf():
    cpf = input("CPF: ").strip()
    if len(cpf) != 11:
        while True:
            function_clear()
            cpf = input("CPF Inválido, Digite Novamente: ")
            if len(cpf) == 11:
                return cpf
    else:
        return cpf