from funçoes import *
from class_loja import loja

def menu_interno():
    print("---" * 20)
    print("Sistema Interno loja: ")
    print("---" * 20)
    print("[1] - Cadrastar Funcionario")
    print("[2] - Buscar Funcionario (pelo codigo)")
    print("[3] - Mostrar funcionario da loja")
    print("[4] - Mostrar quantidade vendas efetuadas pelos funcionarios")
    print("[5] - Mostrar Saldo de vendas da loja")
    print("[6] - Mostrar historico de vendas concluidas ")
    print("[7] - Remover cliente")
    print("[8] - Remover Funcionario")
    print("[9] - Alterar gerente")
    print("[10] - Voltar para o menu principal")
    print("---" * 20)

    op = ler_int("Escolha opcao: ")

    while (op < 1 or op > 10):
        print("Opcao invalida!!")
        op = ler_int("\nEscolha uma opcao valida: ")

    return op


def acessar_loja(loja):

    op = 1

    while (op != 10):

        op = menu_interno()

        if (op == 1):
            spaco2()
            traco()
            print("Preencha os dados solicitados para cadastro do funcionario: ")
            traco()
            cod = ler_int("Escolha codigo de indentificacao do funcionario: ")

            while (loja.busca_funcionario(cod) or cod < 0):
                print("Nao e possivel cadrastar funcionario com codigo ja cadrastado nem codigo negativo!!")
                cod = ler_int("digite um codigo valido: ")

            funcionario = ler_funcionario(cod)

            loja.cadrastar_funcionario(funcionario)

            traco()
            print("\nFuncionario cadrastado com sucesso!!\n")
            traco()
            spaco()

        elif (op == 2):

            spaco2()
            traco()
            print("Buscar funcionario: ")
            traco()

            cod = ler_int("digite o codigo do vendedor: ")

            funcionario = loja.busca_funcionario(cod)

            if (funcionario):
                funcionario.imprimir_dados()

            else:
                print("\nvendedor nao encontrado no sistema!!")

            traco()
            spaco()




        elif (op == 3):

            spaco2()

            if (loja.mostrar_funcionarios() == False):
                print("\nNao ha funcionarios cadastrados no sistema!!\n")

            traco()
            spaco()


        elif (op == 4):

            spaco2()
            if (len(loja.funcionarios) > 0):
                loja.mostar_quantidade_vendas_funcionarios()
            else:
                print("\nNao ha funcionarios cadastrados no sistema!!\n")
            traco()
            spaco()


        elif (op == 5):
            spaco2()
            loja.mostrar_saldo_vendas()
            traco()
            spaco()

        elif (op == 6):

            spaco2()

            if (len(loja.historico_vendas) > 0):
                loja.mostra_historico_de_vendas()
            else:
                traco()
                print("\nNao ha vendas concluidas!!\n")
            traco()
            spaco()


        elif (op == 7):
            spaco2()
            traco()
            print("Remover cliente da loja: ")
            traco()
            cod = ler_str("digite o cpf do cliente: ")

            cliente = loja.busca_cliente(cod)

            if (cliente):
                cliente.imprimir_dados()

                aux = ler_int("\nDigite 1 para remover cliente ou 0 para concelar: ")

                while (aux < 0 or aux > 1):
                    print("\ndigite uma opcao valida!!")
                    aux = ler_int("Digite 1 para remover cliente ou 0 para concelar: ")

                if (aux == 1):
                    loja.remover_cliente(cod)
                    print("\ncliente removido com sucesso!!")
                else:
                    print("\nOperacao cancelada!!")

            else:
                print("Cliente nao cadastrado no sistema!\n")

            traco()
            spaco()

        elif (op == 8):
            spaco2()
            traco()
            print("Remover Funcionario da loja: ")
            traco()
            cod = ler_int("digite o codigo do funcionario: ")

            funcionario = loja.busca_funcionario(cod)

            if (funcionario):
                funcionario.imprimir_dados()

                aux = ler_int("\nDigite 1 para remover funcionario ou 0 para concelar: ")

                while (aux < 0 or aux > 1):
                    print("\ndigite uma opcao valida!!")
                    aux = ler_int("Digite 1 para remover funcionario ou 0 para concelar: ")

                if (aux == 1):
                    loja.remover_funcionario(cod)
                    print("\nfuncionario removido com sucesso!!")
                else:
                    print("\nOperacao cancelada!!")

            else:
                print("Funcionario nao cadastrado no sistema!\n")

            traco()
            spaco()

        elif(op == 9):
            traco()
            print("Digite os dados do novo gerente: ")
            traco()
            gerente = ler_gerente()

            loja.alterar_gerente(gerente)

            print("\n Gerente alterado com sucesso !!")

    spaco2()

