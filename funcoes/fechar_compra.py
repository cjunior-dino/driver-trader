from funcoes.adiciona_carrinho import carrinho
from funcoes.atualiza_dados import *
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
        print('VOCE DESEJA RETORNAR AO MENU?')
        print('1- MENU')
        print('DIGITE QUALQUER TECLA PARA ENCERRAR O SISTEMA')
        option = input()
        if option == '1':
            carrinho.clear()
            return True
        else:
            print(' ')
            print('OBRIGADO POR USAR O DRIVER-TRADE !')
            print(' ')
            return False 
    else:
        print(' ')
        print('OBRIGADO POR USAR O DRIVER-TRADE !')
        print(' ')
        return False
        