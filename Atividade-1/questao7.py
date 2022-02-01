def binario(n):
    num = []
    while(n>1):
        if(n==2 or n==3):
            resto = n % 2
            n //= 2
            num.append(resto)
            num.append(n)
        else:
            resto = n % 2
            n //= 2
            num.append(resto)

    return num



n = int(input('digite um numero: '))
num = []
bin = 0
if(n > 1):
    num = binario(n)

    i = len(num)-1

    while(i>-1):
        bin+= num[i]*10**i
        i-=1
else:
    bin = n

print('numero: {} em binario = {}'.format(n,bin))