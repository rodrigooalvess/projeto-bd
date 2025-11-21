from utils import function_clear
from services import associar_pedido_entregador, listar_pedidos_entregar, finalizar_pedido
import time

def entregador_painel(logged):
    while True:
        try:
            function_clear()
            print("1 - SELECIONAR PEDIDO PARA ENTREGA \n2 - SAIR")
            opc = int(input("Digite uma Opção: "))

            if opc == 1:
                print("-----SELECIONAR PEDIDO PARA ENTREGA-----")
                pedidos = listar_pedidos_entregar()

                for id, cliente, valor, endereco in pedidos:
                    print(f"ID {id} - CPF CLIENTE: {cliente} - ENDEREÇO: {endereco} - R${valor:.2f}")
                
                id_pedido = int(input("Digite o ID do Pedido que Deseja Entregar: "))
                id_funcionario = logged[0]

                associar_pedido_entregador(id_pedido, id_funcionario)
                finalizar_pedido(id_pedido)

            elif opc == 2:
                function_clear()
                break
            else:
                print("Digite uma Opção Válida")
                time.sleep(3)
        except ValueError:
            print("Opção Inválida, Digite um Número")
            time.sleep(3)
