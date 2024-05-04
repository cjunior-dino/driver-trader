from funcoes.busca_produto import busca_produto
from funcoes.adiciona_carrinho import adiciona_carrinho
from funcoes.ver_carrinho import ver_carrinho
from funcoes.fechar_compra import fechar_compra
from funcoes.menu import menu



prossiga = True

while prossiga == True:
    
    menu()
    opcao = int(input('Digite apenas o numero da opção: '))
    print(' ')
    if opcao == 1:
        print(' ')
        print('NOVA BUSCA SOLICITADA:')
        print(' ')
        busca = input('NFORME NOME DO PRODUTO OU O CÓDIGO DO PRODUTO OU A CATEGORIA DO PRODUTO: ').lower()
        prossiga = busca_produto(busca)
    elif opcao == 2:
        cod_prod = str(input('DIGITE O CÓDIGO:')).lower()
        prossiga = adiciona_carrinho(cod_prod)    
    elif opcao == 3:
        prossiga = ver_carrinho()
    elif opcao == 4:
        prossiga = fechar_compra()
    else:
        print(' ')
        print('OPÇÃO INVALIDA')
        print(' ')








'''
                                            __
                                           /°_)
                                    .-^^^-/ /
                                 __/       /
                                <__.|_|-|_|
                            By: DinoKaminari
                                '''