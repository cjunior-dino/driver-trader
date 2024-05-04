from funcoes.adiciona_carrinho import *
def ver_carrinho():
    if len(carrinho) != 0:
        total = 0
        print(' ')
        print('CARRINHO:')
        print(' ')
        print('CODIGO   | NOME          | MARCA     | CATEGORIA     | QUANTIDADE   | VALOR')
        for posicao in range(0, len(carrinho)):
            print(carrinho[posicao][0] + '\t' + carrinho[posicao][1] + '\t' + carrinho[posicao][2] + '\t' + carrinho[posicao][3] + '\t' + str(carrinho[posicao][4]) + '\t' + carrinho[posicao][5])
        print(' ')
        print('QUANTIDADE DE ITENS: ', len(carrinho))
        for item in carrinho:
            codigo, nome, marca, categoria, quantidade, preco = item
            total = total + round(float(preco)*int(quantidade),2)
        print(' ')
        print('TOTAL DO CARRINHO: ', round(total,2))
        print(' ')
    else:
        print(' ')
        print('CARRINHO VAZIO!!')
        print(' ')
    return True