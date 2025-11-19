from utils import function_clear, validar_cpf
from services import cadastrar_cliente, procurar_id_cliente, atualizar_endereco
from services import cadastrar_pedido, cardapio, procurar_id_pedido, produtos_pedido, calcular_valor_pedido, mostrar_resumo_pedido, listar_pedidos_pendentes
from services import procurar_produto
import time

def caixa_painel(logged):
    while True:
        try:
            function_clear()
            print("1 - INICIAR PEDIDO \n2 - ALTERAR/ADICIONAR ENDERECO DO CLIENTE \n3 - BUSCAR PRODUTO \n4 - LISTAR PEDIDOS PENDENTES \n5 - SAIR")
            opc = int(input("Digite uma Opção: "))

            if opc == 1:
                function_clear()
                print("-----INICIAR PEDIDO-----")
                sn = int(input("1 - SIM \n2 - NÃO \nPossui Cadastro? "))
                if sn == 1:
                    cpf = validar_cpf()
                    id_cliente = procurar_id_cliente(cpf)
                
                if sn == 2 or not id_cliente:
                    print("-----CADASTRO DE CLIENTE-----")
                    nome = input("Nome: ")
                    cpf = validar_cpf()
                    opcao = int(input("1 - SIM \n2 - NÃO \nDeseja cadastrar endereço? "))
                    if opcao == 1:
                        endereco = input("Endereço: ")
                        cadastrar_cliente(nome, cpf, endereco)
                    else:
                        cadastrar_cliente(nome, cpf)
                    
                    id_cliente = procurar_id_cliente(cpf)
                
                id_funcionario_responsavel = logged[0]
                modalidade = input("L - LOCAL \nE - ENTREGA \nDigite: ").upper()

                cadastrar_pedido(id_cliente, id_funcionario_responsavel, modalidade)
                id_pedido = procurar_id_pedido(cpf)
                cardapio()
                
                if id_pedido:
                    pedidos_produtos = True

                    while pedidos_produtos:
                        item = int(input("Digite o Número do Item Para Inserir no Pedido ou 0 Para Finalizar: "))
                        if item == 0: pedidos_produtos = False
                        qnt = int(input("Quantidade: "))
                        obs = input("PRESSIONE ENTER SE NÃO HOUVER OBSERVAÇÃO \nObservação: ")
                        produtos_pedido(id_pedido, item, qnt, obs)
                        finalizar = int(input("1 - SIM \n2 - NÃO \nDeseja Inserir mais Itens no Pedido?: "))
                        if finalizar == 2: pedidos_produtos = False
                        elif finalizar == 1: pedidos_produtos = True 

                    valor_total = calcular_valor_pedido(id_pedido)
                    resumo_pedido = mostrar_resumo_pedido(id_cliente, id_pedido)
                    #[]
                    for nome, quantidade, valorTotal in resumo_pedido:
                        print(f"{nome} ----- x{quantidade} - R${valorTotal:.2f}")
                    print(f"Valor Total do Pedido: {valor_total:.2f}")

            elif opc == 2:
                function_clear()
                print("-----ENDEREÇO-----")
                cpf = validar_cpf()
                id = procurar_id_cliente(cpf)
                endereco = input("Endereço: ")
                atualizar_endereco(id, endereco)

            elif opc == 3:
                function_clear()
                print("-----BUSCAR PRODUTO-----")
                nome = input("Digite o Nome do Produto: ")
                resultado = procurar_produto(nome)
                if not resultado:
                    print("Nenhum Produto Encontrado!")
                else:
                    for id, nome, valor in resultado:
                        print(f"{nome} - R${valor:.2f}")

            elif opc == 4:
                print("-----LISTANDO PEDIDOS PENDENTES-----")
                pedidos = listar_pedidos_pendentes()
                for id, cliente, valor, modalidade in pedidos:
                    print(f"{id} - CPF CLIENTE: {cliente} - R${valor:.2f}")

            elif opc == 5:
                function_clear()
                break

            else:
                print("Digite uma Opção Válida")
                time.sleep(3)
        except ValueError:
            print("Opção Inválida, Digite um Número")
            time.sleep(3)
