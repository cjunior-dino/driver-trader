from funcoes.importa_arquivo import adicina
from funcoes.importa_relatorio import relatorio_prod
from funcoes.menu import *

prossiga = True

while prossiga == True:
    
    menu()
    opcao = input('DIGITE APENAS O NUMERO DA OPÇÃO: ')
    print(' ')
    if opcao == '1':
        relatorio_prod()
        print(adicina())
    elif opcao == '2':
        menu_vendas()
    elif opcao == '3':
        print(' ')
        print('OBRIGADO POR USAR O DRIVER-TRADE !')
        print(' ')
        prossiga = False
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