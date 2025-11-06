import os
from services import login
from view import caixa_painel

def main():
    while True: 
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("1 - LOGIN \n2 - SAIR")
            opc = int(input("Digite uma Opção: "))

            if opc == 1:
                print("-----LOGIN-----")
                usuario = input("Usuário (CPF): ")
                senha = input("Senha: ")
                logged = login(usuario, senha)
                if logged:
                    print(f"Seja Bem-Vindo {usuario}")
                    caixa_painel()
            elif opc == 2:
                break
        except TypeError:
            print("Opção Inválida, Digite um Número!")

if __name__ == "__main__":
    main()