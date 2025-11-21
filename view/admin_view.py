from utils import function_clear, validar_cpf
from services import cadastro_funcionario, listar_funcionarios, desativar_funcionario, reativar_funcionario
from services import cadastrar_produto, listar_produtos_ativos, listar_produtos_inativos, alterar_valor_produto, desativar_produto, reativar_produto
import time
import pwinput

def admin_painel(logged):
    while True:
        try:
            function_clear()
            print("1 - CADASTRAR FUNCIONARIO \n2 - LISTAR FUNCIONARIOS \n3 - ATIVAR/DESATIVAR FUNCIONARIOS \n4 - CADASTRAR PRODUTO \n5 - ALTERAR VALOR DO PRODUTO \n6 - DESATIVAR/REATIVAR PRODUTO \n7 - SAIR")
            opc = int(input("Digite uma Opção: "))
            if opc == 1:
                function_clear()
                print("-----CADASTRO DE FUNCIONÁRIO-----")
                nome = input("Nome: ").strip()
                cpf = validar_cpf()
                cargo = input("A - ADMIN \nC - CAIXA \nE - ENTREGADOR \nCargo: ").upper().strip()
                while True:
                    senha = pwinput.pwinput(prompt="Cadastre Sua Senha: ", mask="*").strip()
                    confirmacao = pwinput.pwinput(prompt="Digite Novamente Sua Senha: ", mask="*").strip()

                    if senha == confirmacao: 
                        cadastro_funcionario(nome, cpf, cargo, senha)
                        break
                    else:
                        print("Senhas Não Coincidem!")
            elif opc == 2:
                function_clear()
                listar_funcionarios()
            elif opc == 3:
                function_clear()
                print("-----ATIVAR/DESATIVAR FUNCIONÁRIO-----")
                alt = int(input("1 - DESATIVAR FUNCIONÁRIO \n2 - REATIVAR FUNCIONÁRIO \nDigite: "))
                if alt == 1:
                    cpf = input("Digite o CPF do Funcionário: ").strip()
                    desativar_funcionario(cpf)
                elif alt == 2:
                    cpf = input("Digite o CPF do Funcionário: ").strip()
                    reativar_funcionario(cpf)
            elif opc == 4:
                function_clear()
                print("-----CADASTRAR PRODUTOS-----")
                nome = input("Nome: ").upper().strip()
                categoria = input("C - CAFÉS \nB - BEBIDAS \nS - SALGADOS \nD - DOCES \nDIGITE UMA CATEGORIA: ").upper().strip()
                valor = float(input("Valor: "))
                cadastrar_produto(nome, categoria, valor)
            elif opc == 5:
                function_clear()
                print("-----ALTERAR VALOR DO PRODUTO-----")
                listar_produtos_ativos()
                id = int(input("Digite o Número do Produto: "))
                valor_novo = float(input("Digite o Novo Valor: "))
                alterar_valor_produto(id, valor_novo)
            elif opc == 6:
                function_clear()
                alt = int(input("1 - DESATIVAR PRODUTO \n2 - REATIVAR PRODUTO \n Digite a Opção: "))
                if alt == 1:
                    function_clear()
                    listar_produtos_ativos()
                    idp = int(input("Digite o Número do Produto: "))
                    desativar_produto(idp)
                    time.sleep(3)
                elif alt == 2:
                    function_clear()
                    listar_produtos_inativos()
                    idp = int(input("Digite o Número do Produto: "))
                    reativar_produto(idp)
                    time.sleep(3)
            elif opc == 7:
                break
            else:
                print("Digite uma Opção Válida")
                time.sleep(3)
        except ValueError:
            print("Opção Inválida, Digite um Número")
            time.sleep(3)