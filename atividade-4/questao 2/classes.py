class livro:
    def __init__(self, titulo, autor, data, preco):
        self.titulo = titulo
        self.autor = autor
        self.data = data
        self.preco = preco

    def imprimir(self):
        print(f"\nAutor do livro: {self.autor} ")
        print(f"Data de  publicacao: {self.data} ")
        print(f"Preco alvo: {self.preco} \n")

class biblioteca:
    def __init__(self):
        self.BB = {}

    def inserir_livros(self,titulo, autor, data, preco):
        L = livro(titulo, autor, data, preco)
        self.BB[titulo] = L

    def imprimir_livros(self):

        for v in self.BB.values():
            print(f"\nTitulo do livro: {v.titulo}")
            N = int(input("\ndigite 1 para  exibir  informacoes  detalhadas  sobre  o  livro  selecionado: "))
            if(N == 1):
                v.imprimir()




