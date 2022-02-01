op =1
print('1- triangulo')
print('2- quadrado')
print('3-circulo')
print('4- sair')

while(op!=4):
    op = int(input('digite a opcao:'))

    if(op==1):
        h =float(input('digite a altura:'))
        b = float(input('digite a base:'))
        print('Area do triangulo: {}\n'.format(h*b/2))

    if(op==2):
        b = float(input('digite a medida so lado:'))
        print('Area do triangulo: {}\n'.format(b*b))

    if(op==3):
        n = 3.14159
        b = float(input('digite o raio do circulo:'))
        print('Area do triangulo: {}\n'.format(n*(b**2)))

    elif(op<1 or op>4):
        print('valor invalido!')