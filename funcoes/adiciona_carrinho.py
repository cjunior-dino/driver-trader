from funcoes.importa_arquivo import *
carrinho = []
qtde = 0
def adiciona_carrinho(cod_prod):

    adiciona_produto = []
    for pesquisa in produto:
            codigo, nome, marca, categoria, quantidade, preco = pesquisa       
            if cod_prod == codigo.lower():
                    print(' ')
                    qtde = int(input('INFORME A QUANTIDADE SOLICITADA: '))
                    if qtde <= int(quantidade):
                        adiciona = codigo, nome, marca, categoria, qtde, preco
                        adiciona_produto.append(adiciona)
                    else:
                        print('Quantidade insuficiente')
    if len(adiciona_produto) != 0:
        carrinho.append(adiciona_produto[0])
        print(' ')
        print('PRODUTO ADICIONADO')
        print(' ')
    else:
        print(' ')
        print('CÓDIGO INVALIDO')
        print(' ')
    return True