def ordena(palavra):
    palavra =list(palavra)
    i=0
    j=0
    for i in range(0,len(palavra)):
        for j in range(i+1,len(palavra)):
            if (palavra[i] > palavra[j]):
                aux = palavra[i]
                palavra[i] = palavra[j]
                palavra[j] = aux


    return palavra

palavra = str(input("digite uma palvra: "))

palavra = palavra.lower()

palavra = ''.join(ordena(palavra))

print(palavra)
