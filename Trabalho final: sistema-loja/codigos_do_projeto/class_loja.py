from classes_pessoa import cliente,funcionario,autentivcavel
from class_produto import produto
from class_venda import venda

from time import sleep

class loja:

    def __init__(self,gerente):
        self._funcionarios = {}
        self._clientes = {}
        self._estoque_produtos = {}
        self._historico_vendas = {}
        self._saldo_loja = 0
        self.gerente = gerente


    def cadrastar_funcionario(self,funcionario):
        """
         funcionarios sao cadrastados no discionario de funcionarios
         onde a chave para busca é o cod de indentificação do funcionario
        """
        self._funcionarios[funcionario.cod_indentificacao] = funcionario

    def cadrastar_cliente(self,cliente):
        """
         clente sao cadrastados no discionario de clientes
         onde a chave para busca é o cpf do clientes
        """
        self._clientes[cliente.cpf] = cliente

    def cadrastar_produto(self,produto):
        """
         produtos sao cadrastados no discionario de estoques_produtos
         onde a chave para busca é o codigo do produto
        """
        self._estoque_produtos[produto.cod_produto] = produto


    def mostrar_funcionarios(self):

        print("---" * 30)

        if(len(self._funcionarios) > 0):
            print("Funcionarios da loja: ")
            for i in self._funcionarios.values():
                i.imprimir_dados()
                sleep(1)

            return True
        else:
            return False

    def mostrar_clientes(self):

        print("---" * 30)

        if (len(self._clientes) > 0):
            print("Clientes cadrastados no sistema: ")

            for i in self._clientes.values():
                i.imprimir_dados()
                sleep(1)

            return True
        else:
            return False

    def mostrar_produtos(self):

        print("---" * 30)

        if (len(self._estoque_produtos) > 0):
            print("Produtos em estoque: ")

            for i in self._estoque_produtos.values():
                i.imprimir_dados()
                sleep(1)

            return True

        else:
            return False

    def busca_funcionario(self,cod_indentificacao):

        if cod_indentificacao in self._funcionarios.keys():

            return self._funcionarios[cod_indentificacao]
        else:
            return None

    def busca_cliente(self,cpf):

        if cpf in self._clientes.keys():
            return self._clientes[cpf]
        else:
            return None

    def busca_produto(self,cod_produto):

        if cod_produto in self._estoque_produtos.keys():
            return self._estoque_produtos[cod_produto]
        else:
            return None

    def busca_produto_tipo(self,tipo):
        flag = False

        for i in self._estoque_produtos.values():

            if(i.tipo == tipo):
                i.imprimir_dados()
                flag = True

        return flag

    def busca_produto_marca(self,marca):
        flag = False

        for i in self._estoque_produtos.values():

            if(i.marca == marca):
                i.imprimir_dados()
                flag = True

        return flag



    def remover_funcionario(self,cod_indentificacao):

        if cod_indentificacao in self._funcionarios.keys():
            self._funcionarios.pop(cod_indentificacao)

            return True
        else:
            return False


    def remover_cliente(self,cpf):

        if cpf in self._clientes.keys():
            self._clientes.pop(cpf)

            return True
        else:
            return False

    def remover_produto(self,cod_produto):

        if cod_produto in self._estoque_produtos.keys():
            self._estoque_produtos.pop(cod_produto)

            return True
        else:
            return False

    def mostrar_saldo_vendas(self):
        print("---" * 30)
        print(f" saldo obtido com a venda de produtos da loja: R$ {self._saldo_loja}\n")

    def armazenar_venda(self,pedido):
        self._historico_vendas[pedido.cod_pedido] = pedido

    def mostra_historico_de_vendas(self):
        print("---" * 30)
        print("Historico de vendas: ")
        for i in self._historico_vendas.values():
            i.dados_venda()

    def mostar_quantidade_vendas_funcionarios(self):
        print("---" * 30)
        print("Desempenho de vendas dos funcionarios: ")
        print("---" * 30)
        for i in self._funcionarios.values():
            i.imprimir_quantidade_de_vendas()

    def alterar_gerente(self,gerente):

        #so pode ser alterado o gerentes se ele seguir a Interface altenticavel
        if isinstance(gerente,autentivcavel):
            self.gerente = gerente

            return True
        else:
            return False

    @property
    def saldo_loja(self):
        return self._saldo_loja

    @saldo_loja.setter
    def saldo_loja(self,valor):
        if valor > 0:
            self._saldo_loja = valor

            return True
        else:
            return False

    @property
    def funcionarios(self):
        return self._funcionarios

    @property
    def clientes(self):
        return self._clientes

    @property
    def estoque_produtos(self):
        return self._estoque_produtos

    @property
    def historico_vendas(self):
        return self._historico_vendas



