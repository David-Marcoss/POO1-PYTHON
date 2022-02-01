from funçoes import *
from classes_pessoa import *
from class_produto import produto
from class_venda import venda
from class_loja import loja
from acesso_loja import acessar_loja

# FUNÇÕES

def estoque():

    op = 1

    while (op != 7):
        op = menu_estoque()

        if op == 1:
            spaco2()
            traco()
            print("Preencha os dados solicitados para cadastro do produto: ")
            traco()
            cod = ler_int("digite o codigo do produto: ")

            while (loja.busca_produto(cod) or cod < 0):
                print("\nNao e possivel cadrastar produto com codigo ja cadrastado, ou codigo negativo!!")
                cod = ler_int("digite um codigo valido: ")

            produto = ler_produto(cod)

            loja.cadrastar_produto(produto)

            traco()
            print("\nProduto cadrastado no estoque com sucesso!!\n")
            traco()
            spaco()

        if op == 2:
            spaco2()
            traco()
            print("Buscar Produto: ")
            traco()
            cod = ler_int("digite o codigo do produto: ")

            produto = loja.busca_produto(cod)

            if (produto):
                produto.imprimir_dados()
            else:
                print("Produto nao cadastrado no sistema!\n")

            traco()
            spaco()

        if op == 3:
            spaco2()
            traco()
            print("Buscar Produto por tipo: ")
            traco()
            cod = ler_str("digite o tipo do produto buscado: ")

            if (loja.busca_produto_tipo(cod) == False):
                print("Nao ha produtos do tipo buscado cadastrado no sistema!\n")

            traco()
            spaco()

        if op == 4:

            spaco2()
            traco()
            print("Buscar Produto por Marca: ")
            traco()
            cod = ler_str("digite a marca buscada: ")

            if (loja.busca_produto_marca(cod) == False):
                print("Nao ha produtos da marca buscada cadastrado no sistema!\n")

            traco()
            spaco()

        if op == 5:
            spaco2()

            if (loja.mostrar_produtos() == False):
                print(" Nao ha produtos cadastrados no estoque!!")

            traco()
            spaco()

        if op == 6:
            spaco2()
            traco()
            print("Remover Produto do estoque: ")
            traco()
            cod = ler_int("digite o codigo do produto: ")

            produto = loja.busca_produto(cod)

            if (produto):
                produto.imprimir_dados()

                aux = ler_int("Digite 1 para remover produto ou 0 para concelar: ")

                while( aux < 0 or aux > 1):
                    print("digite uma opcao valida!!")
                    aux = ler_int("Digite 1 para remover produto ou 0 para concelar: ")

                if(aux == 1):
                    loja.remover_produto(cod)
                    print("\n Produto removido com sucesso!!")
                else:
                    print("\n Operacao cancelada!!")

            else:
                print("Produto nao cadastrado no sistema!\n")

            traco()
            spaco()

        if op == 7:
            spaco2()

def ler_pedido():
    flag = 0
    pedido = {}  #armazena todos os produtos que o cliente deseja comprar
    num = 0

    while (flag != 1 and flag !=3 ):
        aux = []      #armazena o produto que o cliente deseja comprar e a quantidade do produto comprada

        cod = ler_int('\ndigite o codigo do produto: ')

        produto = loja.busca_produto(cod)

        if (produto):
            aux.append(produto)

            if(produto.quantidade == 0):
                print("\nNo momento nao ha unidades desse produto disponiveis para a venda!! \n")

            else:
                quant = ler_int('\ndigite a quantidade: ')

                while(quant <=0 or quant > produto.quantidade):
                    print(f"\nproduto possui {produto.quantidade} unidades disponiveis no estoque ")
                    quant = ler_int('digite a quantidade valida: ')

                aux.append(quant)
                pedido[num] = aux
                num += 1

        else:
            print("\nProduto nao encontrado no sistema!\n")



        flag = ler_int('\ndigite 1 para finalizar pedido ou  2 para adicionar mais produtos: ou 3 para cancelar pedido: ')

        while(flag < 1 or flag > 3):
            print("\ndigite uma opcao valida!!")
            flag = ler_int('\ndigite 1 para finalizar pedido ou  2 para adicionar mais produtos: ou 3 para cancelar pedido: ')

    if flag == 1:
        return pedido

    elif flag == 3 or len(pedido) == 0:
        return None

def venda_produto(num_pedidos):

    cod = ler_int("digite o codigo do vendedor que efetuara a venda: ")

    funcionario = loja.busca_funcionario(cod)

    if(funcionario == None):
        print("\ncodigo do vendedor nao encontrado no sistema!!")
        print("Nao é possivel realizar a venda!!\n")
    else:
        cpf = ler_str("digite o cpf do cliente que efetuara a compra: ")

        cliente = loja.busca_cliente(cpf)

        if (cliente):
            pedido = ler_pedido()

            if(pedido):
                vender = venda(pedido,funcionario,cliente,num_pedidos+1)
                spaco2()
                vender.dados_venda()

                aux = ler_int("\ndigite 1 para concluir venda e 0 para cancelar: ")

                while(aux < 0 or aux > 1 ):
                    print("\ndigite uma opcao valida!!")
                    aux = ler_int("digite 1 para concluir venda ou 0 para cancelar: ")

                if(aux == 1):
                    pagamento = ler_int("\ndigite o valor do pagamento: ")
                    valor_pedido = vender.valor_total_pedido()

                    while(pagamento < valor_pedido):
                        print(f"\nO valor do pedido e de {valor_pedido}, o pagamento nao pode ser menor que esse valor !! ")
                        pagamento = ler_int("digite o valor do pagamento valido: ")

                    vender.concluir_pedido(pagamento)

                    loja.saldo_loja += valor_pedido  #incrementa o valor obitido com a venda no saldo da loja
                    loja.armazenar_venda(vender)     #armazena a venda concluida
                    num_pedidos +=1

                    print("\nVenda concluida com sucesso!!")

                else:
                    print("\nVenda cancelada!!")

            else:
                print("\nVenda cancelada!!")
        else:
            print("\nCliente nao cadastrado no sistema!")
            print("Cadastre o cliente no sistema para realizar a venda\n")

    traco()
    spaco()


# MAIN

autentivcavel.register(gerente)

traco()
print("Para iniciar o sistema primeiro cadastre um gerente/administrador para loja:")

print("\nDigite os dados solicitados: \n")

gerente = ler_gerente()

traco()
print("Gerente cadastrado com sucesso!!")
traco()

print("Inicializando Sistema....")
sleep(1)
spaco2()



loja = loja(gerente)

op = 1
num_pedidos = 0




while(op != 7):

    op = menu1()

    if (op == 1):
        spaco2()
        traco()
        print("Preencha os dados solicitados para cadastro do cliente: ")
        traco()
        cpf = ler_str("digite o cpf do cliente: ")

        if(loja.busca_cliente(cpf)):
            print("\nCliente ja cadrastado no sistema!!")

        else:
            cliente = ler_cliente(cpf)

            loja.cadrastar_cliente(cliente)
            traco()
            print("\nCliente cadrastado com sucesso!!\n")

        traco()
        spaco()


    elif (op == 2):
        spaco2()
        traco()
        print("Buscar Cliente: ")
        traco()
        cpf = ler_str("digite o cpf do cliente: ")

        cliente = loja.busca_cliente(cpf)
        if (cliente):
            cliente.imprimir_dados()
        else:
            print("Cliente nao cadastrado no sistema!\n")

        traco()
        spaco()

    elif (op == 3):
        spaco2()

        if(loja.mostrar_clientes() == False):
            print(" Nao ha clientes cadastrados no sistema!!")



        traco()
        spaco()

    elif (op == 4):
        spaco2()
        estoque()

    elif (op == 5):
        spaco2()
        traco()

        if( len(loja.funcionarios) > 0 and len(loja.clientes) > 0 and len(loja.estoque_produtos) > 0 ):
            """
            a operação de venda so é feita se ao menos um funcionario um cliente e um produto cadastrado no sistema
            a venda é feita por um funcionario para um cliente e o cliente pode comprar mais de um produto da loja
            
            """
            print("Vender produto: ")

            venda_produto(num_pedidos)
            num_pedidos += 1
        else:
            print("\nNo momento nao e possivel realizar esta operacao")
            print("verifique se ah clientes, funcionarios e produtos cadastrado no sistema !!")
            traco()
            spaco()





    elif (op == 6):
       """
        o acesso as informaçoes e operaçoes da loja
        so pode ser feito pelo gerente da loja o acesso
        é feito pela senha e cod de indentificação do gerente 
       """
       traco()

       print("Digite os dodos para acessar sistema interno da loja: ")
       traco()
       cod = ler_int("digite o codigo de indentificacao: ")
       senha = ler_str("senha: ")

       if (loja.gerente.autentica(senha,cod)):
            spaco2()
            acessar_loja(loja)
       else:
           print("Cod de indentificacao ou Senha invalida!!\n")

       traco()
       spaco2()


    elif (op == 7):
        print("Saindo......")
        traco()