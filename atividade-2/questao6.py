def troca( lista):
    j = len(lista)-1

    for i in range(0,len(lista) // 2):
        aux = lista[i]
        lista[i] = lista[j]
        lista[j] = aux
        j -= 1

    return lista


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,12]

print(lista)
print(troca(lista))
