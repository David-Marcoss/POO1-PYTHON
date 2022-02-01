from classes import cliente,conta,ContaCorrente,ContaPoupanca, AtualizadorDeContas

david = cliente("david","marcos","076.629.493-54")
joao = cliente( 'Joao',"francisco","333.222.444-76")
maria = cliente('Maria', "eduarda","444.555.888-33")

c1 = ContaPoupanca(maria,'123-4', 1000.0)
c2 = ContaCorrente(joao,'123-5', 1000.0)

c3 = conta(david,123,5000)

c1.atualiza(0.01)
c2.atualiza(0.01)
c3.atualiza(0.01)

print(c1.saldo)
print(c2.saldo)
print(c3.saldo)

c1.__str__()
c2.__str__()
c3.__str__()

adc = AtualizadorDeContas(0.01)

adc.roda(c1)
adc.roda(c2)
adc.roda(c3)

print(f"Saldo total : {adc.saldo_total}")

