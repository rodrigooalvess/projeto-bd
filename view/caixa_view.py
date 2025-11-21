from utils import function_clear, validar_cpf, function_pause
from services import cadastrar_cliente, procurar_id_cliente, atualizar_endereco
from services import cadastrar_pedido, cardapio, procurar_id_pedido, produtos_pedido, calcular_valor_pedido, mostrar_resumo_pedido, listar_pedidos_pendentes, associar_pedido_delivery, buscar_pedido, pagamento_pedido, cancelar_pedido
from services import procurar_produto
import time

def caixa_painel(logged):
    while True:
        try:
            function_clear()
            print("1 - INICIAR PEDIDO \n2 - FINALIZAR/CANCELAR PEDIDO \n3 - ALTERAR/ADICIONAR ENDERECO DO CLIENTE \n4 - BUSCAR PRODUTO \n5 - LISTAR PEDIDOS PENDENTES \n6 - BUSCAR PEDIDO \n7 - SAIR")
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
                if modalidade == 'E': associar_pedido_delivery(id_pedido)
                cardapio()
                
                if id_pedido:
                    pedidos_produtos = True

                    while pedidos_produtos:
                        item = int(input("Digite o Número do Item Para Inserir no Pedido ou 0 Para Finalizar: "))
                        if item == 0: break
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
                    function_pause()

            elif opc == 2:
                print("-----CANCELAR/FINALIZAR PEDIDO-----")
                opcc = int(input("1 - CANCELAR PEDIDO \n2 - FINALIZAR PEDIDO \nDigite: "))
                if opcc == 1:
                    cpf = validar_cpf()
                    id_cliente = procurar_id_cliente(cpf)
                    id_pedido = procurar_id_pedido(cpf)
                    if pedido:
                        cancelar_pedido(id_pedido, id_cliente)
                    elif not pedido:
                        print("Nenhum Pedido Encontrado!")
                elif opcc == 2:
                    cpf = validar_cpf()
                    id_cliente = procurar_id_cliente(cpf)
                    id_pedido = procurar_id_pedido(cpf)
                    resumo = mostrar_resumo_pedido(id_cliente, id_pedido)
                    if resumo:
                        total = 0
                        print(f"PEDIDO#{id_pedido}")
                        for nome, quantidade, valor in resumo:
                            print(f"{nome} x{quantidade} - R${valor:.2f}")
                            total += valor
                        print(f"Valor Total: R${total:.2f}")
                    
                        metodo = input("\nP - PIX \nC - CARTÃO DÉBITO/CRÉDITO \nD - DINHEIRO \nMétodo de Pagamento: ").upper().strip()
                        while metodo not in ("P", "C", "D"):
                                metodo = input("\nDigite um Método Válido \nP - PIX \nC - CARTÃO DÉBITO/CRÉDITO \nD - DINHEIRO \nMétodo de Pagamento: ").upper().strip()
                        pagamento_pedido(metodo)
                    elif not resumo:
                        print("Nenhum Pedido Encontrado!")

            elif opc == 3:
                function_clear()
                print("-----ENDEREÇO-----")
                cpf = validar_cpf()
                id = procurar_id_cliente(cpf)[0]
                endereco = input("Endereço: ")
                atualizar_endereco(id, endereco)

            elif opc == 4:
                function_clear()
                print("-----BUSCAR PRODUTO-----")
                nome = input("Digite o Nome do Produto: ")
                resultado = procurar_produto(nome)
                if not resultado:
                    print("Nenhum Produto Encontrado!")
                else:
                    for id, nome, valor in resultado:
                        print(f"{nome} - R${valor:.2f}")

            elif opc == 5:
                print("-----LISTANDO PEDIDOS PENDENTES-----")
                pedidos = listar_pedidos_pendentes()
                for id, cliente, valor, modalidade in pedidos:
                    print(f"{id} - CPF CLIENTE: {cliente} - R${valor:.2f}")

            elif opc == 6:
                print("-----DETALHES DE UM PEDIDO / BUSCA DE PEDIDO-----")
                cpf = validar_cpf()
                id_cliente = procurar_id_cliente(cpf)
                pedido = buscar_pedido(cpf)
                if pedido:
                    total = 0
                    print(f"#PEDIDO{pedido[0]}")
                    for id, nome_produto, quantidade, valor in pedido:
                        total += valor
                        print(f"{nome_produto} x{quantidade} - R${valor:.2f}")
                    print(f"Valor Total: R${total:.2f}")
                elif not pedido:
                    print("Nenhum Pedido Encontrado!")

            elif opc == 7:
                function_clear()
                break

            else:
                print("Digite uma Opção Válida")
                time.sleep(3)
        except ValueError:
            print("Opção Inválida, Digite um Número")
            time.sleep(3)
