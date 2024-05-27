from funcoes.importa_arquivo import *

def cadastra():

    codigo, nome, marca, categoria, quantidade, preco = adicina()[-1]

    print(int(codigo) + 1)
    return True