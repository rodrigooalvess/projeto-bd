import os

def validar_cpf():
    cpf = input("CPF: ")
    if len(cpf) != 11:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            cpf = input("CPF Inválido, Digite Novamente: ")
            if len(cpf) == 11:
                return cpf
    else:
        return cpf