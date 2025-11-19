from utils import function_clear, validar_cpf
from services import cadastrar_cliente, procurar_cliente, atualizar_endereco
from services import cadastrar_pedido, cardapio, procurar_id_pedido, produtos_pedido, calcular_valor_pedido
import time

def caixa_painel(logged):
    while True:
        try:
            function_clear()
            print("1 - CADASTRAR CLIENTE \n2 - ALTERAR/ADICIONAR ENDERECO DO CLIENTE \n3 - INICIAR COMPRA \n4 - SAIR")
            opc = int(input("Digite uma Opção: "))

            if opc == 1:
                function_clear()
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
                function_clear()
                print("-----ENDEREÇO-----")
                cpf = validar_cpf()
                id = procurar_cliente(cpf)
                endereco = input("Endereço: ")
                atualizar_endereco(id, endereco)
            elif opc == 3:
                function_clear()
                print("-----INICIAR PEDIDO-----")
                cpf = validar_cpf()
                id_cliente = procurar_cliente(cpf)
                id_funcionario_responsavel = logged[0]
                modalidade = input("L - LOCAL \n E - ENTREGA \nDigite: ")
                cadastrar_pedido(id_cliente, id_funcionario_responsavel, modalidade)
                cardapio()
                id_pedido = procurar_id_pedido(cpf)
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
                    print(f"Valor Total do Pedido: {valor_total:.2f}")
                    
                nota = int(input("Deseja Nota Fiscal?"))


            elif opc == 4:
                function_clear()
                break
            else:
                print("Digite uma Opção Válida")
                time.sleep(3)
        except ValueError:
            print("Opção Inválida, Digite um Número")
            time.sleep(3)
