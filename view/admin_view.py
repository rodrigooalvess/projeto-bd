from utils import function_clear, validar_cpf, function_pause
from services import cadastro_funcionario, listar_funcionarios, desativar_funcionario, reativar_funcionario
from services import cadastrar_produto, listar_produtos_ativos, listar_produtos_inativos, alterar_valor_produto, desativar_produto, reativar_produto
from services import listar_clientes
from services import relatorio_total_vendas
import time
import pwinput

def admin_painel(logged):
    while True:
        try:
            function_clear()
            print("1 - CADASTRAR FUNCIONARIO \n2 - LISTAR FUNCIONARIOS \n3 - ATIVAR/DESATIVAR FUNCIONARIOS \n4 - LISTAR CLIENTES \n5 - CADASTRAR PRODUTO \n6 - ALTERAR VALOR DO PRODUTO \n7 - DESATIVAR/REATIVAR PRODUTO \n8 - RELATORIOS \n9 - SAIR")
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
                    time.sleep(3)
                elif alt == 2:
                    cpf = input("Digite o CPF do Funcionário: ").strip()
                    reativar_funcionario(cpf)
                    time.sleep(3)
            elif opc == 4:
                function_clear()
                listar_clientes()
            elif opc == 5:
                function_clear()
                print("-----CADASTRAR PRODUTOS-----")
                nome = input("Nome: ").upper().strip()
                categoria = input("C - CAFÉS \nB - BEBIDAS \nS - SALGADOS \nD - DOCES \nDIGITE UMA CATEGORIA: ").upper().strip()
                valor = float(input("Valor: "))
                descricao = input("Digite uma Descrição do Produto ou Pressione ENTER: ")
                cadastrar_produto(nome, categoria, valor, descricao)
            elif opc == 6:
                function_clear()
                print("-----ALTERAR VALOR DO PRODUTO-----")
                listar_produtos_ativos()
                id = int(input("Digite o Número do Produto: "))
                valor_novo = float(input("Digite o Novo Valor: "))
                alterar_valor_produto(id, valor_novo)
            elif opc == 7:
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
            elif opc == 8:
                function_clear()
                resumo_faturamento = relatorio_total_vendas()
                print("-----RELATÓRIO DE VENDAS/FATURAMENTO-----")
                if resumo_faturamento:
                    tipo = int(input("1 - RELATÓRIO DIÁRIO \n2 - RELATÓRIO SEMANAL \n3 - RELATÓRIO MENSAL \nSELECIONE: "))
                    if tipo == 1:
                        print(f"FATURAMENTO DIÁRIO - R${resumo_faturamento[0]:.2f}")
                        function_pause()
                    if tipo == 2:
                        print(f"FATURAMENTO SEMANAL - R${resumo_faturamento[1]:.2f}")
                        function_pause()
                    if tipo == 3:
                        print(f"FATURAMENTO MENSAL - R${resumo_faturamento[2]:.2f}")
                        function_pause()
                if not resumo_faturamento:
                    print("Nenhum Pedido Finalizado nesse Periodo!")
            elif opc == 9:
                break
            else:
                print("Digite uma Opção Válida")
                time.sleep(3)
        except ValueError:
            print("Opção Inválida, Digite um Número")
            time.sleep(3)