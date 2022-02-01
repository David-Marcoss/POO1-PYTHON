from class_loja import loja
from classes_pessoa import cliente,funcionario
from class_produto import produto
from class_venda import venda



loja = loja()

prod1 = produto(1,"iphone 10","celular","apple",5500.56,5)
prod2 = produto(2,"s10 lite","celular","samsung",1500.56,3)
prod3 = produto(3,"macbook","notebook","apple",10500.55,3)
prod4 = produto(4,"dell aspire","notebook","dell",2500.56,3)
prod5 = produto(5,"headset power","fones de ouvido","headragon",500.66,13)
prod6 = produto(6,"headset max","fones de ouvido","headragon",150.66,10)

p1 = cliente('davi','123',99999393,'14/03/2001')
p2 = cliente('jaiara','123.333.44-55',89999393,'12/04/2001')
p3 = cliente('carlos','765.345.142-90',99359393,'12/05/1999')
p4 = cliente('maria','444.555.423-32',99293393,'31/04/2000')

f1 = funcionario("joao","673.234.456-34",99934231,"24/01/2001",10,1000)
f2 = funcionario("sabrina","123.234.456-34",99934451,"04/01/2000",11,1000)
f3 = funcionario("angela","623.734.456-34",81934231,"24/01/1998",12,1000)
f4 = funcionario("fernanda","173.284.456-34",94934231,"24/01/2001",13,1000)

loja.cadrastar_funcionario(f1)
loja.cadrastar_funcionario(f2)
loja.cadrastar_funcionario(f3)
loja.cadrastar_funcionario(f4)

loja.cadrastar_cliente(p1)
loja.cadrastar_cliente(p2)
loja.cadrastar_cliente(p3)
loja.cadrastar_cliente(p4)

loja.cadrastar_produto(prod1)
loja.cadrastar_produto(prod2)
loja.cadrastar_produto(prod3)
loja.cadrastar_produto(prod4)
loja.cadrastar_produto(prod5)
loja.cadrastar_produto(prod6)

#loja.mostrar_funcionarios()
#loja.mostrar_clientes()
#loja.mostrar_produtos()
"""
loja.busca_funcionario(12)
loja.busca_cliente('123')
loja.busca_produto(1)
loja.busca_produto_tipo('notebook')
loja.busca_produto_marca('headragon')

loja.remover_funcionario(12)
loja.remover_cliente('765.345.142-90')
loja.remover_produto(1)

#loja.mostrar_produtos()

loja.mostrar_saldo_vendas()

v = venda(loja.estoque_produtos[3],loja.funcionarios[13])

v.vender()
v.dados_venda()

loja.busca_produto(3)
loja.busca_funcionario(13)

flag = 0
pedido = {}

while(flag != 1):
    cod = int(input('digite o codigo do produto: '))
    quant = int(input('digite a quantidade: '))

    aux = []

    aux.append(loja.estoque_produtos[cod])
    aux.append(quant)

    pedido[cod] = aux

    flag = int(input('1 para finalizar e 0 para continuar: '))

v = venda(pedido,loja.funcionarios[13],loja.clientes['123'],1)

v.dados_venda()
v.concluir_pedido(12000)

loja.armazenar_venda(v)

loja.mostra_historico_de_vendas()
loja.mostar_quantidade_vendas_funcionarios()

"""

prod = loja.busca_cliente('1234')
if prod:
    prod.imprimir_dados()
else:
    print("nao encontrado")

loja.saldo_loja += 1000

loja.mostrar_saldo_vendas()
