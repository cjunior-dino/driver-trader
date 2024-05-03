from funcoes.adiciona_carrinho import carrinho
def fechar_compra():
    if len(carrinho) != 0:
        total = 0
        print(' ')
        print('----------------NF----------------')
        print('CODIGO   | NOME | CATEGORIA  | VALOR')
        for posicao in range(0, len(carrinho)):
            print(carrinho[posicao][0] + '\t' + carrinho[posicao][1] + '\t' + carrinho[posicao][3] + '\t' + carrinho[posicao][5])
        print('QUANTIDADE DE ITENS: ', len(carrinho))
        for item in carrinho:
            codigo, nome, marca, categoria, quantidade, preco = item
            total = total + float(preco)
        print('TOTAL DO CARRINHO: ', round(total,2))
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
        