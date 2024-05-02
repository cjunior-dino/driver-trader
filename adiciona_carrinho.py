import importa_arquivo
carrinho = []
def adiciona_carrinho(cod_prod):

    adiciona_produto = []
    for pesquisa in importa_arquivo.produto:
            codigo, nome, marca, categoria, quantidade, preco = pesquisa       
            if cod_prod == codigo.lower():
                    adiciona_produto.append(pesquisa)
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