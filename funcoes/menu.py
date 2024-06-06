def menu():
    print("BEM-VINDO AO DRIVE TRADE\n")
    print("SELECIONE UMA OPÇÃO\n")
    print("1- GERENCIAL\n")
    print("2- VENDAS\n")
    print("3- SAIR DO SISTEMA\n")

def menu_gerencial():
    print(' ')
    print('**DIGITE O CODIGO DE ALGUMA DAS OPÇÕES**')
    print('5- CADASTRAR PRODUTO')
    print('7- BUSCAR NOTA')
    print('8- VOLTAR AO MENU ANTERIOR')
    print(' ')
    opcao = input('DIGITE APENAS O NUMERO DA OPÇÃO: ')
    print(' ')
    if opcao == '1':
        menu_gerencial()
    

    '''if opcao == '1':
        print(' ')
        print('NOVA BUSCA SOLICITADA: ')
        print(' ')
        busca = input('NFORME NOME DO PRODUTO OU O CÓDIGO DO PRODUTO OU A CATEGORIA DO PRODUTO: ').lower()
        prossiga = busca_produto(busca)
    elif opcao == '2':
        print(' ')
        cod_prod = str(input('DIGITE O CÓDIGO: ')).lower()
        prossiga = adiciona_carrinho(cod_prod)    
    elif opcao == '3':
        prossiga = ver_carrinho()
    elif opcao == '4':
        print(' ')
        prossiga = remove()
    elif opcao == '5':
        prossiga = cadastra()
    elif opcao == '6':
        prossiga = fechar_compra()
    elif opcao == '7':
        prossiga = buscar_nota()
    elif opcao == '8':
        print(' ')
        print('OBRIGADO POR USAR O DRIVER-TRADE !')
        print(' ')
        prossiga = False
    else:
        print(' ')
        print('OPÇÃO INVALIDA')
        print(' ')
'''

def menu_vendas():
    print(' ')
    print('**DIGITE O CODIGO DE ALGUMA DAS OPÇÕES**')
    print('1- FAZER NOVA BUSCA')
    print('2- ADICIONAR ITEM AO CARRINHO')
    print('3- VISUALIZAR OS ITENS DO CARRINHO')
    print('4- REMOVER PRODUTO DO CARRINHO')
    print('6- FINALIZAR VENDA')
    print('8- SAIR DO SISTEMA')
    print(' ')
    opcao = input('DIGITE APENAS O NUMERO DA OPÇÃO: ')
    print(' ')
    if opcao == '1':
        menu_gerencial()
    

    '''if opcao == '1':
        print(' ')
        print('NOVA BUSCA SOLICITADA: ')
        print(' ')
        busca = input('NFORME NOME DO PRODUTO OU O CÓDIGO DO PRODUTO OU A CATEGORIA DO PRODUTO: ').lower()
        prossiga = busca_produto(busca)
    elif opcao == '2':
        print(' ')
        cod_prod = str(input('DIGITE O CÓDIGO: ')).lower()
        prossiga = adiciona_carrinho(cod_prod)    
    elif opcao == '3':
        prossiga = ver_carrinho()
    elif opcao == '4':
        print(' ')
        prossiga = remove()
    elif opcao == '5':
        prossiga = cadastra()
    elif opcao == '6':
        prossiga = fechar_compra()
    elif opcao == '7':
        prossiga = buscar_nota()
    elif opcao == '8':
        print(' ')
        print('OBRIGADO POR USAR O DRIVER-TRADE !')
        print(' ')
        prossiga = False
    else:
        print(' ')
        print('OPÇÃO INVALIDA')
        print(' ')
'''