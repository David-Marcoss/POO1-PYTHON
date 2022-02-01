def retorna(lista):
    lista2 = []
    for i in range(0, len(lista)):
        if type(lista[i]) != list:
            lista2.append(lista[i])
        else:
            lista2.extend(lista[i])
    return lista2

def testa(lista):
    for i in range (0,len(lista)):
        if type(lista[i]) == list:
            return 1
    return 0

def imprime(lista):
    for i in lista:
        print("{}".format(i),end=",")



lista = [0,1,"oi",True,[0,"alo",["eae","yo"]],[3,4,5]]
lista2 = [1,[2,[3,[4,[5,[6]]]]]]

while(testa(lista2)==1):
    lista2 =retorna(lista2)


imprime(lista2)

