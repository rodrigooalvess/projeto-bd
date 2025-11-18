import time
import getpass
from services import login, clear
from view import caixa_painel, admin_painel, entregador_painel

def main():
    rodando = True
    while rodando: 
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
                    time.sleep(3)
                    if logged.lower() == "admin" or logged.lower() == "chefe":
                        admin_painel()
                    elif logged.lower() == "caixa":
                        caixa_painel()
                    elif logged.lower() == "entregador":
                        entregador_painel()
                elif not logged:
                    print("Usuário ou Senha Incorretos!")
            elif opc == 2:
                rodando = False
        except ValueError:
            print("Opção Inválida, Digite um Número!")
            time.sleep(3)

if __name__ == "__main__":
    main()