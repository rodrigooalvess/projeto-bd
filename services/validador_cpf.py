import os
from services import clear

def validar_cpf():
    cpf = input("CPF: ")
    if len(cpf) != 11:
        while True:
            clear()
            cpf = input("CPF Inválido, Digite Novamente: ")
            if len(cpf) == 11:
                return cpf
    else:
        return cpf