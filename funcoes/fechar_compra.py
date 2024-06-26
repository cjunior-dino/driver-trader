from funcoes.adiciona_carrinho import carrinho
from funcoes.atualiza_dados import *
import funcoes.atualiza_dados
import funcoes.atualiza_relatorio
import funcoes.nota_fiscal 
def fechar_compra():
    if len(carrinho) != 0:
        total = 0
        tot_prod = 0
        print(' ')
        print('----------------NF----------------')
        print('CODIGO   | NOME          | MARCA     | CATEGORIA     | QUANTIDADE   | VALOR')
        for posicao in range(0, len(carrinho)):
            print(carrinho[posicao][0] + '\t' + carrinho[posicao][1] + '\t' + carrinho[posicao][2] + '\t' + carrinho[posicao][3] + '\t' + str(carrinho[posicao][4]) + '\t' + carrinho[posicao][5])
        for item in carrinho:
            codigo, nome, marca, categoria, quantidade, preco = item
            tot_prod = tot_prod + int(quantidade)
        print(' ')
        print('QUANTIDADE DE ITENS: ', tot_prod)
        for item in carrinho:
            codigo, nome, marca, categoria, quantidade, preco = item
            total = total + round(float(preco)*int(quantidade),2)
        print(' ')
        print('TOTAL DO CARRINHO: ', round(total,2))
        atualiza()
        print(' ')
        funcoes.atualiza_relatorio.relatorio_prod()
        funcoes.nota_fiscal.nota()
        carrinho.clear()
        return True

    else:
        print(' ')
        print('O CARRINHO ESTA VAZIO')
        print(' ')
        return True
        