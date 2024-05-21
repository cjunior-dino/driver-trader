from funcoes.adiciona_carrinho import carrinho

def remove(): 
    if len(carrinho) != 0:
        prod_cod = str(input('DIGITE O CÓDIGO: '))
        for produto in carrinho:
                codigo, _, _, _, _, _ = produto
                if prod_cod == codigo:
                    carrinho.remove(produto)
                    print('PRODUTO REMOVIDO COM SUCESSO!')
                    return True
        else:
            print(' ')
            print('CÓDIGO INVALIDO')
            print(' ')
            return True
    else:
        print(' ')
        print('CARRINHO VAZIO!!')
        print(' ')    
        return True