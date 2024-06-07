from funcoes.menu import *

prossiga = True

while prossiga == True:
    
    menu()
    opcao = input('DIGITE APENAS O NUMERO DA OPÇÃO: ')
    print(' ')
    if opcao == '1':
        prossiga = menu_gerencial()
    elif opcao == '2':
        prossiga = menu_vendas()
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