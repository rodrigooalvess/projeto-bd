import os
from services import cadastro_funcionario, login, validar_cpf, cadastrar_cliente

def main():
    while True: 
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("1 - LOGIN \n2 - CADASTRO \n3 - SAIR")
            opc = int(input("Digite uma Opção: "))

            if opc == 1:
                print("-----LOGIN-----")
                usuario = input("Usuário (CPF): ")
                senha = input("Senha: ")
                logged = login(usuario, senha)
                if logged:
                    print(f"Seja Bem-Vindo {usuario}")
            elif opc == 2:
                print("-----CADASTRO-----")
                nome = input("Nome: ")
                cpf = validar_cpf()
                cargo = input("Cargo: ").lower()
                senha = input("Senha: ")
                cadastro_funcionario(nome, cpf, cargo, senha)
            elif opc == 3:
                break
        except TypeError:
            print("Opção Inválida, Digite um Número!")

if __name__ == "__main__":
    main()