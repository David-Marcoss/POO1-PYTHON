from classes import ContaCorrente,ContaPoupanca , ContaInvestimento

c1 = ContaCorrente('123',"david",500,5000)
c2 = ContaPoupanca('123',"marcos")
c3 = ContaInvestimento('3',"Joaozin",500)

c1.deposita(100)
c1.extrato()
c1.sacar(200)
c1.atualiza(0.01)
print(c1)

c2.deposita(100)
c2.extrato()
c2.sacar(50)
c2.atualiza(0.01)
print(c2)

c3.deposita(1500)
c3.extrato()
c3.sacar(50)
c3.atualiza(0.01)
print(c3)





