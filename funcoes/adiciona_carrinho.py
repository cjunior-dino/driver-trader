from funcoes.importa_arquivo import *
carrinho = []
qtde = 0
def adiciona_carrinho(cod_prod):
    adiciona_produto = []
    for pesquisa in adicina():
            codigo, nome, marca, categoria, quantidade, preco = pesquisa       
            if cod_prod == codigo.lower():
                    adiciona_produto.clear()
                    print(' ')
                    qtde = int(input('INFORME A QUANTIDADE SOLICITADA: '))
                    if int(quantidade) == 0:
                         print('PRODUTO SEM ESTOQUE')
                         return True
                    if qtde <= int(quantidade) :
                        adiciona = codigo, nome, marca, categoria, qtde, preco
                        adiciona_produto.append(adiciona)
                    else:
                        print(f'TEM APENAS {quantidade} NO ESTOQUE, INFORME O NOVO VALOR')
                        print(' ')
                        
                        adiciona_carrinho()

            if len(adiciona_produto) != 0:
                carrinho.append(adiciona_produto[0])
                print(' ')
                print('PRODUTO ADICIONADO')
                print(' ')
                return True
    else:
        print(' ')
        print('CÓDIGO INVALIDO')
        print(' ')
        return True