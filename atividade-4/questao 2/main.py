from classes import biblioteca

def menu():
    print("\n1-Inserir livros")
    print("2- Exibir livros")
    print("3-sair ")
    op = int(input("\ndigite a opcao: "))
    return op

def ler(biblioteca):
    titulo = str(input("\ndigite o titulo do livro: "))
    autor = str(input("digite o nome do autor: "))
    data = str(input("digite a data de publicação no formato (dia/mes/ano): "))
    preco = float(input("digite o preco alvo do livro: "))

    biblioteca.inserir_livros(titulo, autor, data, preco)


Biblioteca = biblioteca()

quant = int(input("digite a quntidade de livros que voce deseja inserir: "))
aux = 1
for i in range(0,quant):
    ler(Biblioteca)

while(aux != 0):
    Biblioteca.imprimir_livros()
    aux = int(input("\ndigite 1 se deseja continuar esta operacao ou digite 0 para sair: "))



