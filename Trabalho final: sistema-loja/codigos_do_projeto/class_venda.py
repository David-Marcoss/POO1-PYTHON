
from datetime import date

class venda:
    """
    classe venda responsavel por realizar a venda de um produto
    recebe como parametro um pedido que é um discionario onde cada
    chave possui uma lista contendo o produto e a quantidade que deseja ser
    comprada pelo cliente
    recebe tambem o funcionario que realiza a venda
    o cliente que compra o produto
    e o cod do pedido
    """
    def __init__(self,pedido,funcionario,cliente,cod_pedido):
        self.pedido = pedido
        self.funcionario = funcionario
        self.cliente = cliente
        self.cod_pedido = cod_pedido
        self.data_pedido = date.today().strftime('%d/%m/%Y')

    def dados_venda(self):
        print('\n')
        print("---" * 20)
        print(" Detalhes do pedido: ")
        print("---" * 20)
        print(f" numero do pedido: {self.cod_pedido}            Data pedido {self.data_pedido}")
        #print(f" Data pedido {self.data_pedido}")
        print(f" Cliente: {self.cliente.nome}")
        print(f" Vendedor: {self.funcionario.nome}")
        print("---"*20)
        print(" Produtos: ")
        for i in self.pedido.values():
            print(f" produto: {i[0].nome_produto} quatidade: {i[1]} valor produto: R$ {i[0].preco:.2f} X{i[1]}")
            print("---" * 20)
        print(f" valor total pedido: {self.valor_total_pedido():.2f}")
        print("---" * 20)

    def valor_total_pedido(self):
        valor_total = 0

        for i in self.pedido.values():
            valor_total += i[0].preco * i[1]

        return valor_total


    def concluir_pedido(self,pagamento):
        self.funcionario.quant_vendas+= 1

        for i in self.pedido.values():
             i[0].quantidade -= i[1]

        self.dados_venda()
        print(f"valor pagamento: {pagamento}")
        print(f"Troco: {pagamento - self.valor_total_pedido():.2f}")
        print("---" * 20)

