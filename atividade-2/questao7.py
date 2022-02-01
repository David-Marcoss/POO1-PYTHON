def leia(lista):
    for i in range(0,10):
        lista.append(int(input("digite um valor: ")))

    return lista

l1 = []
l2 = []
l3 = []

leia(l1)
leia(l2)

for i in range(0,10):
    l3.append(l1[i]*l2[i])

print(l3)