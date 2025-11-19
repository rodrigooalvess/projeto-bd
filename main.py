import time
import getpass
from services import login
from utils import function_clear
from view import caixa_painel, admin_painel, entregador_painel

def main():
    rodando = True
    while rodando: 
        try:
            function_clear()
            print("1 - LOGIN \n2 - SAIR")
            opc = int(input("Digite uma Opção: "))

            if opc == 1:
                function_clear()
                print("-----LOGIN-----")
                usuario = input("Usuário (CPF): ")
                senha = getpass.getpass("Senha: ")
                logged = login(usuario, senha)
                if logged:
                    function_clear()
                    print(f"Seja Bem-Vindo {usuario}\n")
                    time.sleep(3)
                    if logged[3] == "A":
                        admin_painel(logged)
                    elif logged[3]== "C":
                        caixa_painel(logged)
                    elif logged[3] == "E":
                        entregador_painel(logged)
                elif not logged:
                    print("Usuário ou Senha Incorretos!")
            elif opc == 2:
                rodando = False
        except ValueError:
            print("Opção Inválida, Digite um Número!")
            time.sleep(3)

if __name__ == "__main__":
    main()