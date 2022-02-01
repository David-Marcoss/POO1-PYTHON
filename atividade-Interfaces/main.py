from classes import ContaCorrente,Tributavel,SeguroDeVida,ManipuladorDeTributaveis,ContaPoupanca

#help(Tributavel)

c1 = ContaCorrente('123',"david",1000,5000)
c2 = ContaPoupanca('124',"maria",1000,5000)

seguro = SeguroDeVida(100.0, 'José', '345-77')

Tributavel.register(ContaCorrente)
Tributavel.register(SeguroDeVida)

print(f"impostos conta corrente: {c1.get_valor_imposto()}")
print(f"imposto conta seguro de vida: {seguro.get_valor_imposto()}")

lista_tributaveis = []

lista_tributaveis.append(c1)
lista_tributaveis.append(seguro)
lista_tributaveis.append(c2)

mt = ManipuladorDeTributaveis()

total = mt.calcula_impostos(lista_tributaveis)

print(f"total de imposto cobrado: {total}")

