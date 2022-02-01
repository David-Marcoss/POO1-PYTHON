def primo(n):
    for i in range(2,n):
        if(n%i == 0):
            return False

    return True

n = int(input('digite um numero:'))
p = int(input('digite um numero:'))
aux = 0
if(p>n):
    while(n<=p):
        if( primo(n) == True):
            print(n)
            aux =1
        n+=1
else:
    while (n>=p):
        if (primo(p) == True):
            print(p)
            aux = 1
        p += 1

if(aux)==0:
    print('Nao existe nenhum número primo dentro desse intervalo.')
