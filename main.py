import time
import pwinput
from services import login
from utils import function_clear
from view import caixa_painel, admin_painel, entregador_painel
from services import cadastro_funcionario

def main():
    rodando = True
    while rodando: 
        try:
            function_clear()
            print("1 - LOGIN \n2 - CADASTRO \n3 - SAIR")
            opc = int(input("Digite uma Opção: "))

            if opc == 1:
                function_clear()
                print("-----LOGIN-----")
                usuario = input("Usuário (CPF): ")
                senha = pwinput.pwinput(prompt="Senha: ", mask="*")
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
                function_clear()
                print("-----CADASTRO-----")
                nome = input("Nome: ")
                cpf = input("CPF: ").strip()
                cargo = input("A - ADMIN \nC - CAIXA \nE - ENTREGADOR \nCargo: ").strip().upper()
                while True:
                    senha = pwinput.pwinput(prompt="Cadastre Sua Senha: ", mask="*").strip()
                    confirmacao = pwinput.pwinput(prompt="Digite Novamente Sua Senha: ", mask="*").strip()

                    if senha == confirmacao: 
                        cadastro_funcionario(nome, cpf, cargo, senha)
                        break
                    else:
                        print("Senhas Não Coincidem!")
                time.sleep(3)

            elif opc == 3:
                rodando = False
        except ValueError:
            print("Opção Inválida, Digite um Número!")
            time.sleep(3)

if __name__ == "__main__":
    main()