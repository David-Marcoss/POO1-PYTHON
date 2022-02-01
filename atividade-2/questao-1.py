def tam (str):
    cont = 0
    for i in str:
        cont+=1

    return cont




palavra = str(input("digite uma palavra:"))

print(" palavra {} tem {} letras ".format(palavra,tam(palavra)))
