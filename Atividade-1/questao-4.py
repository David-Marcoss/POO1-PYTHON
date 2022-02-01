def fatorial(n):
    fat =1
    for i in range(2,n+1):
        fat*= i

    return fat

def fatorial2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fatorial2(n - 1) * n

n = int(input('digite um valor: '))

print('fatorial iterativo {} = {}'.format(n,fatorial(n)))
print('fatorial recursivo {} = {}'.format(n,fatorial2(n)))