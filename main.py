import busca_produto
import adiciona_carrinho
import ver_carrinho
import fechar_compra
import menu

prossiga = True

while prossiga == True:
    
    menu.menu()
    opcao = int(input('Digite apenas o numero da opção: '))
    print(' ')
    if opcao == 1:
        print(' ')
        print('NOVA BUSCA SOLICITADA:')
        print(' ')
        busca = input('NFORME NOME DO PRODUTO OU O CÓDIGO DO PRODUTO OU A CATEGORIA DO PRODUTO: ').lower()
        prossiga = busca_produto.busca_produto(busca)
    elif opcao == 2:
        cod_prod = str(input('DIGITE O CÓDIGO:')).lower()
        prossiga = adiciona_carrinho.adiciona_carrinho(cod_prod)    
    elif opcao == 3:
        prossiga = ver_carrinho.ver_carrinho()
    elif opcao == 4:
        prossiga = fechar_compra.fechar_compra()
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