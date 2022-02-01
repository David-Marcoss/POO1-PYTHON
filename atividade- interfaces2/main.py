from funcoes import menu,ler_cliente,ler_funcionario,conta_contas,mostrar_clientes,tem_conta
from funcoes import criar_seguro,criar_corrente,criar_poupanca,cliente_existe,acessar_conta

op = 1
funcionarios = []
clientes = {}

while( op != 8):

    op = menu()

    if(op == 1):
        fun = ler_funcionario()
        funcionarios.append(fun)
        print("\nFuncionario cadrastado!!\n")

    elif(op == 2):

        if ler_cliente(clientes):
            print("\ncliente cadrastado com sucesso!\n")
        else:
            print("\nCpf invalido !cliente ja esta cadrastado!\n")

    elif(op == 3):
        cpf = str(input("digite seu cpf: "))

        if cliente_existe(clientes,cpf):
            if(criar_corrente(clientes[cpf])):
                print("\nconta cadrastada com sucesso!!\n")
            else:
                print("\nO cliente ja possui duas contas! Nao e possivel criar mais contas\n")


        else:
            print("\nNao é possivel criar conta para um cliente nao cadrastado!\n")

    elif (op == 4):
        cpf = str(input("digite seu cpf: "))

        if cliente_existe(clientes, cpf):
            if (criar_poupanca(clientes[cpf])):
                print("\nconta cadrastada com sucesso!!\n")
            else:
                print("\nO cliente ja possui duas contas! Nao e possivel criar mais contas\n")


        else:
            print("\nNao é possivel criar conta para um cliente nao cadrastado!\n")

    elif (op == 5):
        cpf = str(input("digite seu cpf: "))

        if cliente_existe(clientes, cpf):
             criar_seguro(clientes[cpf])
        else:
            print("\nNao é possivel criar conta para um cliente nao cadrastado!\n")

    elif (op == 6):
        cpf = str(input("digite seu cpf para acessar a conta: "))

        if cliente_existe(clientes, cpf):
            if(tem_conta(clientes[cpf])):
                acessar_conta(clientes[cpf])
            else:
                print("\nCliente nao possui conta cadrastada!\n")
        else:
            print("\nNao é possivel acessar conta de um cliente nao cadrastado!\n")

    elif (op == 7):

        if(len(clientes) != 0):
            print("Dados banco: ")
            total = conta_contas(clientes)

            if(total!= 0):
                print(f"\ntotal de contas cadrastadas no banco: {total}")
            else:
                print("\nNao a contas cadrastadas!\n")

            mostrar_clientes(clientes)
        else:
            print("\nNao ha clientes cadrstados!\n")

    else:
        print("\nSaindo...\n")




