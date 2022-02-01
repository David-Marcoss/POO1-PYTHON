from datetime import date
from classes_pessoa import cliente,funcionario,gerente
from class_produto import produto
from time import sleep

def traco():
    print("---" * 30)

def spaco():
    input("Digite enter para voltar ao menu:  ")
    print("\n\n"*25)

def spaco2():
    print("\n\n" * 25)

def ler_int(msg):
    try:
        op = int(input(f"{msg}"))
    except ValueError:
        print("Entrada invalida!! digite um valor inteiro\n")
        return ler_int(msg)

    else:
        return op

def ler_float(msg):
    try:
        op = float(input(f"{msg}"))
    except ValueError:
        print("Entrada invalida!! digite um valor ponto flutuante\n")
        return ler_float(msg)

    else:
        return op

def ler_str(msg):
    return str(input(msg))

def ler_data_nascimento():
    print("digite sua data de nascimento: ")
    dia = ler_int("Dia: ")
    while(dia > 31 or dia < 1):
        dia = ler_int("digite um dia valido: ")

    mes = ler_int("Mes: ")
    while (mes > 12 or mes < 1):
        mes = ler_int("digite um mes valido: ")

    ano = ler_int("Ano:")
    while (ano > date.today().year or ano < 1900):
        ano = ler_int("digite um ano valido: ")

    return f"{dia}/{mes}/{ano}"


def ler_funcionario(cod):

    nome = ler_str("nome: ")
    cpf = ler_str("cpf: ")
    contato = ler_int("numero de contato: ")
    data = ler_data_nascimento()
    salario = ler_float("valor salario: ")

    while(salario < 1):
        salario = ler_float("digite um salario valido: ")

    return funcionario(nome, cpf, contato, data, cod,salario)

def ler_gerente():

    cod = ler_int("codigo de indentificacao: ")
    nome = ler_str("nome: ")
    cpf = ler_str("cpf: ")
    contato = ler_int("numero de contato: ")
    data = ler_data_nascimento()
    salario = ler_float("valor salario: ")

    while(salario < 1):
        salario = ler_float("digite um salario valido: ")

    senha = ler_str("digite uma senha para acesso ao sistema: ")

    return gerente(nome, cpf, contato, data, cod,salario,senha)

def ler_cliente(cpf):

    nome = ler_str("nome: ")
    contato = ler_int("numero de contato: ")
    data = ler_data_nascimento()

    return cliente(nome,cpf,contato,data)

def ler_produto(cod):

    nome = ler_str("Nome produto: ")
    tipo = ler_str("Tipo do produto: ")
    marca = ler_str("Marca: ")
    preco = ler_float("Preco do produto: ")
    while(preco<=0):
        preco = ler_float("digite um preco valido: ")

    quauntidade = ler_int("quantidade do produto: ")
    while (quauntidade <= 0):
        quauntidade = ler_int("digite um quantidade valida: ")

    return produto(cod,nome,tipo,marca,preco,quauntidade)


def menu1():
    print("---" * 20)
    print("Sistema Loja BestCell: ")
    print("---" * 20)
    print("[1] - Cadrastar cliente")
    print("[2] - Buscar cliente")
    print("[3] - Mostrar clientes cadastrados no sistema")
    print("[4] - Assessar Estoque")
    print("[5] - Fazer venda produto")
    print("[6] - Acessar informacoes da loja")
    print("[7] - sair")
    print("---" * 20)

    op = ler_int("Escolha opcao: ")

    while(op < 1 or op > 8):
        print("Opcao invalida!!" )
        op = ler_int("\nEscolha uma opcao valida: ")

    return op

def menu_estoque():
    print("---" * 20)
    print("Sistema de Estoque produtos: ")
    print("---" * 20)
    print("[1] - Cadrastar Produto")
    print("[2] - Buscar produto (pelo codigo)")
    print("[3] - Buscar produtos por Tipo")
    print("[4] - Buscar produtos por Marca")
    print("[5] - Mostar os produtos em Estoque")
    print("[6] - Remover produto do estoque")
    print("[7] - Voltar para o menu principal")
    print("---" * 20)

    op = ler_int("Escolha opcao: ")

    while (op < 1 or op > 7):
        print("Opcao invalida!!")
        op = ler_int("\nEscolha uma opcao valida: ")

    return op
