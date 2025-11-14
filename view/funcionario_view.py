from services import cadastrar_cliente, validar_cpf, atualizar_endereco, procurar_cliente, cadastro_funcionario, listar_funcionarios, clear, cadastrar_produto
import time

def admin_painel():
    while True:
        try:
            clear()
            print("1 - CADASTRAR FUNCIONARIO \n2 - LISTAR FUNCIONARIOS \n3 - REMOVER FUNCIONARIO \n4 - CADASTRAR PRODUTO \n5 - LISTAR PEDIDOS \n6 - SAIR")
            opc = int(input("Digite uma Opção: "))
            if opc == 1:
                clear()
                print("-----CADASTRO-----")
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
                print("-----EXCLUIR FUNCIONÁRIO-----")
            elif opc == 4:
                clear()
                print("-----CADASTRAR PRODUTOS-----")
                nome = input("Nome: ").upper()
                categoria = input("A - ALIMENTOS \nC - CAFÉS \nB - BEBIDAS \nDIGITE UMA CATEGORIA: ").upper()
                valor = float(input("Valor: "))
                cadastrar_produto(nome, categoria, valor)
            elif opc == 6:
                clear()
                break
            else:
                print("Digite uma Opção Válida")
                time.sleep(3)
        except ValueError:
            print("Opção Inválida, Digite um Número")
            time.sleep(3)

def caixa_painel():
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
                pass
            elif opc == 4:
                clear()
                break
            else:
                print("Digite uma Opção Válida")
                time.sleep(3)
        except ValueError:
            print("Opção Inválida, Digite um Número")
            time.sleep(3)

def entregador_painel():
    pass