from funcoes.adiciona_carrinho import carrinho

def remove(): 
    if len(carrinho) != 0:
        prod_cod = str(input('DIGITE O CÓDIGO: ')).lower()
        for i, pesquisa in enumerate(carrinho):
                codigo, nome, marca, categoria, quantidade, preco = pesquisa       
                if prod_cod == codigo.lower():
                    del carrinho[i]
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