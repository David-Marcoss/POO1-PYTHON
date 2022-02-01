from classes_pessoa import funcionario,cliente
from classes_conta import ContaPoupanca,ContaCorrente,Tributacao,SeguroDeVida,Tributavel


def menu():
    print("\nSistema bancario: ")
    print("\n[1] - cadrastar funcionario")
    print("[2] - cadrastar cliente")
    print("[3] - criar conta corrente")
    print("[4] - criar conta poupança")
    print("[5] - criar seguro de vida")
    print("[6] - Acessar conta ")
    print("[7] - Exibir informacoes do banco")
    print("[8] - sair\n")

    op = int(input("escolha opcao: "))

    while(op < 1 or op> 8):
        op = int(input("escolha opcao valida: "))

    return op

def menu_conta():
    print("\nMenu Contas:")
    print("\n[1] - mostrar extrato")
    print("[2] - cobrar tributacao")
    print("[3] - sacar dinheiro")
    print("[4] - depositar dinheiro")
    print("[5] - fazer transferencia")
    print("[6] - imprimir historico da conta")
    print("[7] - sair\n")

    op = int(input("escolha opcao: "))

    return op


def ler_funcionario():
    nome = str(input("digite o nome: "))
    cpf = str(input("digite o cpf: "))
    data = str(input("digite a data de nascimento: "))
    salario = float(input("digite o salario: "))

    fun = funcionario(nome,cpf,data,salario)

    return fun


def ler_cliente(clientes):
    nome = str(input("digite o nome: "))
    cpf = str(input("digite o cpf: "))
    if cliente_existe(clientes,cpf):
       return False
    else:
        data = str(input("digite a data de nascimento: "))
        profissao = str(input("digite a profissao: "))
        renda = float(input("digite a renda: "))

        c = cliente(nome, cpf, data, profissao,renda)

        clientes[cpf] = c
        return True


def ler_dados_corrente():

    num = int(input("digite o numero da conta: "))
    saldo = float(input("digite o saldo: "))
    limite = float(input("digite o limite: "))


    conta = ContaCorrente(num,saldo,limite)

    return conta


def ler_dados_poupanca():
    num = int(input("digite o numero da conta: "))
    saldo = float(input("digite o saldo: "))

    conta = ContaPoupanca(num, saldo)

    return conta

def ler_dados_seguro():
    num = float(input("digite o valor mensal seguro: "))
    saldo = float(input("digite o valor total do seguro: "))

    conta = SeguroDeVida(num, saldo)

    return conta


def cliente_existe(clientes,cpf):

    if cpf in clientes.keys():
        return True
    else:
        return False

def criar_poupanca(cliente):

    if(len(cliente.contas) < 2):
        c = ler_dados_poupanca()
        cliente.criar_conta(c)
        return True
    else:
        return False


def criar_corrente(cliente):

    if (len(cliente.contas) < 2):
        c = ler_dados_corrente()
        cliente.criar_conta(c)
        return True
    else:
        return False

def criar_seguro(cliente):
    c = ler_dados_seguro()
    cliente.criar_seguro(c)

def acessar_conta(cliente):
    op = 1
    tributacao = Tributacao()
    flag = 0

    while (op != 7):
        op = menu_conta()

        if (op == 1):

            if len(cliente.contas) > 1:
                print("\n1-corrente\n2- poupanca")
                aux = int(input("escolha qual conta voce deseja  ver o extrato: "))

                if aux == 1:
                    for i in cliente.contas:
                        if i.tipo == "corrente":
                            print("\nextrato conta corrente: ")
                            i.extrato()
                elif aux == 2:
                    for i in cliente.contas:
                        if i.tipo == "poupanca":
                            print("\nextrato conta poupanca: ")
                            i.extrato()
                else:
                    print("\nOpcao invalida!!\n")
            else:
                print(f"\nextrato conta:{cliente.contas[0].tipo} ")
                cliente.contas[0].extrato()

        elif(op == 2):

            for i in cliente.contas:
                if (isinstance(i, Tributavel)):
                    imposto = i.get_valor_imposto()
                    tributacao.cobrar_tributacao(imposto)
                    print(f"\nTributacao em cima da conta corrente: {imposto}")
                    flag = 1
                    if len(cliente.seguro_vida) > 0:
                        for i in cliente.seguro_vida:
                            if (isinstance(i, Tributavel)):
                                imposto = i.get_valor_imposto()
                                tributacao.cobrar_tributacao(imposto)
                                print(f"\nTributacao em cima do seguro de vida: {imposto}")
                                flag = 1

            if flag == 0:
                print("\nEsse cliente nao possui contas tributaveis!\n")
            else:
                print("historico de Tributacao da conta: ")
                tributacao.imprimir_historico()


        elif (op == 3):

            if len(cliente.contas) > 1:
                print("1-corrente\n2- poupanca")
                aux = int(input("escolha qual conta voce deseja realizar saque:"))
                valor = float(input("\ndigite o valor para saque: "))

                if aux == 1:
                    for i in cliente.contas:
                        if i.tipo == "corrente":
                            if i.sacar(valor):
                                print("\nSaque feito com sucesso!\n")

                            else:
                                print("\nvalor de saque invalido!!\n")
                elif aux == 2:
                    for i in cliente.contas:
                        if i.tipo == "poupanca":
                            if i.sacar(valor):
                                print("\nSaque feito com sucesso!\n")

                            else:
                                print("\nvalor de saque invalido!!\n")
                else:
                    print("\nOpcao invalida!!\n")
            else:
                valor = float(input("\ndigite o valor para saque: "))

                if cliente.contas[0].sacar(valor):
                    print("\nSaque feito com sucesso!\n")

                else:
                    print("\nvalor de saque invalido!!\n")


        elif (op == 4):

            if len(cliente.contas) > 1:
                print("\n1-corrente\n2- poupanca")
                aux = int(input("escolha qual conta voce deseja realizar o deposito:"))
                valor = float(input("\ndigite o valor para deposito: "))

                if aux == 1:
                    for i in cliente.contas:
                        if i.tipo == "corrente":
                            if i.depositar(valor):
                                print("\nDeposito feito com sucesso!\n")

                            else:
                                print("\nvalor de Deposito invalido!!\n")
                elif aux == 2:
                    for i in cliente.contas:
                        if i.tipo == "poupanca":
                            if i.depositar(valor):
                                print("\nDeposito feito com sucesso!\n")

                            else:
                                print("\nvalor de Deposito invalido!!\n")
                else:
                    print("\nOpcao invalida!!\n")
            else:
                valor = float(input("\ndigite o valor para Deposito: "))

                if cliente.contas[0].depositar(valor):
                    print("\nDeposito feito com sucesso!\n")

                else:
                    print("\nvalor de Deposito invalido!!\n")


        elif (op == 5):
            """
            if len(cliente.contas) > 1:
                print("\n1-corrente\n2- poupanca")
                aux = int(input("escolha qual conta voce deseja realizar a transferencia:"))
                valor = float(input("\ndigite o valor para trasnferencia: "))

                if aux == 1:
                    for i in cliente.contas:
                        if i.tipo == "corrente":
                            if i.depositar(valor):
                                print("\nDeposito feito com sucesso!\n")
                                print(f"saldo: {i.saldo}")
                            else:
                                print("\nvalor de Deposito invalido!!\n")
                elif aux == 2:
                    for i in cliente.contas:
                        if i.tipo == "poupanca":
                            if i.depositar(valor):
                                print("\nDeposito feito com sucesso!\n")
                                print(f"saldo: {i.saldo}")
                            else:
                                print("\nvalor de Deposito invalido!!\n")
                else:
                    print("\nOpcao invalida!!\n")
            else:
                valor = float(input("\ndigite o valor para Deposito: "))

                if cliente.contas[0].depositar(valor):
                    print("\nDeposito feito com sucesso!\n")
                    print(f"saldo: {cliente.contas[0].saldo}")
                else:
                    print("\nvalor de Deposito invalido!!\n")

            """
            print("\nNAO É POSSIVEL REALIAZAR ESTA OPERACAO !OPCAO AINDA EM DESENVOLVIMENTO\n")


        elif (op == 6):

            if len(cliente.contas) > 1:
                print("\n1-corrente\n2- poupanca")
                aux = int(input("escolha qual conta voce deseja realizar imprimir historico: "))

                if aux == 1:
                    for i in cliente.contas:
                        if i.tipo == "corrente":
                            print("\nHistorico da conta: ")
                            i.imprimir_historico()
                elif aux == 2:
                    for i in cliente.contas:
                        if i.tipo == "poupanca":
                            print("\nHistorico da conta: ")
                            i.imprimir_historico()
                else:
                    print("\nOpcao invalida!!\n")
            else:
                print("\nHistorico da conta: ")
                cliente.contas[0].imprimir_historico()

        elif (op == 7):
            pass
        elif (op == 8):
            print("\nSaindo...\n")

        else:
            print("\nopcao invalida!!\n")


def conta_contas(clientes):
    total = 0
    for i in clientes.values():
        total+= len(i.contas)

    return total

def mostrar_clientes(clientes):
    for i in clientes.values():
        print("---"*20)
        print(f"cliente: {i.nome} possui {len(i.contas)} contas e {len(i.seguro_vida)} seguros de vida")

def tem_conta(cliente):

    if len(cliente.contas) != 0:
        return True
    else:
        return False
