import os
import time
import getpass
from services import login, clear
from view import caixa_painel, admin_painel, entregador_painel

def main():
    while True: 
        try:
            clear()
            print("1 - LOGIN \n2 - SAIR")
            opc = int(input("Digite uma Opção: "))

            if opc == 1:
                clear()
                print("-----LOGIN-----")
                usuario = input("Usuário (CPF): ")
                senha = getpass.getpass("Senha: ")
                logged = login(usuario, senha)
                if logged:
                    clear()
                    print(f"Seja Bem-Vindo {usuario}\n")
                    if logged[3].lower() == "admin" or logged[3].lower() == "chefe":
                        admin_painel()
                    elif logged[3].lower() == "caixa":
                        caixa_painel()
                    elif logged[3].lower() == "entregador":
                        entregador_painel()
            elif opc == 2:
                break
        except ValueError:
            print("Opção Inválida, Digite um Número!")
            time.sleep(3)

if __name__ == "__main__":
    main()