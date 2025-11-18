from services import desativar_funcionario, reativar_funcionario, alterar_produto, cadastrar_cliente, validar_cpf, atualizar_endereco, procurar_cliente, cadastro_funcionario, listar_funcionarios, clear, cadastrar_produto, listar_produtos_ativos, listar_produtos_inativos, desativar_produto, reativar_produto
import time

def admin_painel(logged):
    while True:
        try:
            clear()
            print("1 - CADASTRAR FUNCIONARIO \n2 - LISTAR FUNCIONARIOS \n3 - ATUALIZAR FUNCIONARIOS \n4 - CADASTRAR PRODUTO \n5 - ALTERAR VALOR DO PRODUTO \n6 - DESATIVAR/REATIVAR PRODUTO \n7 - SAIR")
            opc = int(input("Digite uma Opção: "))
            if opc == 1:
                clear()
                print("-----CADASTRO DE FUNCIONÁRIO-----")
                nome = input("Nome: ")
                cpf = validar_cpf()
                cargo = input("Cargo: ").lower()
                senha = input("Senha: ")
                cadastro_funcionario(nome, cpf, cargo, senha)
            elif opc == 2:
                clear()
                listar_funcionarios()
            elif opc == 3:
                clear()
                print("-----ATUALIZAR FUNCIONÁRIO-----")
                alt = int(input("1 - DESATIVAR FUNCIONÁRIO \n2 - REATIVAR FUNCIONÁRIO \nDigite: "))
                if alt == 1:
                    cpf = input("Digite o CPF do Funcionário: ")
                    desativar_funcionario(cpf)
                elif alt == 2:
                    cpf = input("Digite o CPF do Funcionário: ")
                    reativar_funcionario(cpf)
            elif opc == 4:
                clear()
                print("-----CADASTRAR PRODUTOS-----")
                nome = input("Nome: ").upper()
                categoria = input("A - ALIMENTOS \nC - CAFÉS \nB - BEBIDAS \nDIGITE UMA CATEGORIA: ").upper()
                valor = float(input("Valor: "))
                cadastrar_produto(nome, categoria, valor)
            elif opc == 5:
                clear()
                print("-----ALTERAR VALOR DO PRODUTO-----")
                listar_produtos_ativos()
                id = int(input("Digite o Número do Produto: "))
                valor_novo = float(input("Digite o Novo Valor: "))
                alterar_produto(id, valor_novo)
            elif opc == 6:
                clear()
                alt = int(input("1 - DESATIVAR PRODUTO \n 2 - REATIVAR PRODUTO"))
                if alt == 1:
                    listar_produtos_ativos()
                    idp = int(input("Digite o Número do Produto: "))
                    desativar_produto(idp)
                elif alt == 2:
                    listar_produtos_inativos()
                    idp = int(input("Digite o Número do Produto: "))
                    reativar_produto(idp)
            elif opc == 7:
                break
            else:
                print("Digite uma Opção Válida")
                time.sleep(3)
        except ValueError:
            print("Opção Inválida, Digite um Número")
            time.sleep(3)

def caixa_painel(logged):
    while True:
        try:
            clear()
            print("1 - CADASTRAR CLIENTE \n2 - ALTERAR/ADICIONAR ENDERECO DO CLIENTE \n3 - INICIAR COMPRA \n4 - SAIR")
            opc = int(input("Digite uma Opção: "))

            if opc == 1:
                clear()
                print("-----CADASTRO DE CLIENTE-----")
                nome = input("Nome: ")
                cpf = validar_cpf()
                opcao = int(input("1 - SIM \n2 - NÃO \nDeseja cadastrar endereço? "))
                if opcao == 1:
                    endereco = input("Endereço: ")
                    cadastrar_cliente(nome, cpf, endereco)
                else:
                    cadastrar_cliente(nome, cpf)
            elif opc == 2:
                clear()
                print("-----ENDEREÇO-----")
                cpf = validar_cpf()
                id = procurar_cliente(cpf)
                endereco = input("Endereço: ")
                atualizar_endereco(id, endereco)
            elif opc == 3:
                clear()
                cpf = validar_cpf()
                id_cliente = procurar_cliente(cpf)
                id_funcionario_responsavel = logged[0]
                modalidade = input("L - LOCAL \n E - ENTREGA \nDigite: ")
                listar_produtos_ativos()

            elif opc == 4:
                clear()
                break
            else:
                print("Digite uma Opção Válida")
                time.sleep(3)
        except ValueError:
            print("Opção Inválida, Digite um Número")
            time.sleep(3)

def entregador_painel(logeed):
    pass