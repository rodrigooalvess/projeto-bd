import os
from services import cadastrar_cliente, validar_cpf, atualizar_endereco, procurar_cliente

def caixa_painel(funcionario):
    while True:
        try:
            print("1 - CADASTRAR CLIENTE \n2 - ALTERAR/ADICIONAR ENDERECO DO CLIENTE \n3 - INICIAR COMPRA \n4 - SAIR")
            opc = int(input("Digite uma Opção: "))

            if opc == 1:
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
                print("-----ENDEREÇO-----")
                cpf = validar_cpf()
                id = procurar_cliente(cpf)
                endereco = input("Endereço: ")
                atualizar_endereco(id, endereco)
            elif opc == 3:
                pass
            elif opc == 4:
                break
            else:
                print("Digite uma Opção Válida")
        except TypeError:
            print("Opção Inválida, Digite um Número")