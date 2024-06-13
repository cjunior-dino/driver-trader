
from funcoes.adiciona_carrinho import adiciona_carrinho
from funcoes.busca_produto import busca_produto
from funcoes.buscar_nf import buscar_nota
from funcoes.cadastra_produto import cadastra
from funcoes.fechar_compra import fechar_compra
from funcoes.remover_carrinho import remove
from funcoes.ver_carrinho import ver_carrinho


def menu():
    print("BEM-VINDO AO DRIVE TRADE\n")
    print("SELECIONE UMA OPÇÃO\n")
    print("1- GERENCIAL\n")
    print("2- VENDAS\n")
    print("3- SAIR DO SISTEMA\n")

def menu_gerencial():
    prossiga = True
    while prossiga:
        print(' ')
        print('**DIGITE O CODIGO DE ALGUMA DAS OPÇÕES**')
        print('1- CADASTRAR PRODUTO')
        print('2- BUSCAR NOTA')
        print('3- VOLTAR AO MENU ANTERIOR')
        print(' ')
        opcao = input('DIGITE APENAS O NUMERO DA OPÇÃO: ')
        print(' ')
        if opcao == '1':
            prossiga = cadastra()
        elif opcao == '2':
            prossiga = buscar_nota()
        elif opcao == '3':
            print(' ')
            print(' ')
            break
        else:
            print(' ')
            print('OPÇÃO INVALIDA')
            print(' ')
            menu_gerencial()



def menu_vendas():

    while True:
        print(' ')
        print('**DIGITE O CODIGO DE ALGUMA DAS OPÇÕES**')
        print('1- FAZER NOVA BUSCA')
        print('2- ADICIONAR ITEM AO CARRINHO')
        print('3- VISUALIZAR OS ITENS DO CARRINHO')
        print('4- REMOVER PRODUTO DO CARRINHO')
        print('5- FINALIZAR VENDA')
        print('6- VOLTAR AO MENU ANTERIOR')
        print(' ')
        opcao = input('DIGITE APENAS O NUMERO DA OPÇÃO: ')
        print(' ')
        if opcao == '1':
            print(' ')
            print('NOVA BUSCA SOLICITADA: ')
            print(' ')
            busca = input('NFORME NOME DO PRODUTO OU O CÓDIGO DO PRODUTO OU A CATEGORIA DO PRODUTO: ').lower()
            busca_produto(busca)
        elif opcao == '2':
            print(' ')
            cod_prod = str(input('DIGITE O CÓDIGO: ')).lower()
            adiciona_carrinho(cod_prod)
        elif opcao == '3':
            ver_carrinho()
        elif opcao == '4':
            print(' ')
            remove()
        elif opcao == '5':
            fechar_compra()
        elif opcao == '6':
            print(' ')
            print(' ')
            break
        else:
            print(' ')
            print('OPÇÃO INVALIDA')
            print(' ')
            menu_vendas()