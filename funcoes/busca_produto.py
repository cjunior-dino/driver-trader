from funcoes.importa_arquivo import *

#import importa_arquivo
resultado = []
def busca_produto(busca):
    resultado.clear()
    if busca == '':
        print(' ')
        print('BUSCA INVALIDA')
        print(' ')
        
    else:
        for pesquisa in produto:
            codigo, nome, marca, categoria, quantidade, preco = pesquisa       
            if busca in nome.lower() or busca == categoria.lower() or busca == codigo.lower():
                    resultado.append(pesquisa)
        
        if len(resultado) == 0:
            print(' ')
            print('PRODUTO NÃO ENCONTRADO')

        else:
            print(' ')
            print('RESULTADOS:')           
            print('CODIGO   | NOME          | MARCA     | CATEGORIA     | ESTOQUE   | VALOR')
            for posicao in range(0, len(resultado)):
                    print(resultado[posicao][0] + '\t' + resultado[posicao][1] + '\t' + resultado[posicao][2] + '\t' + resultado[posicao][3] + '\t' + resultado[posicao][4] + '\t' + resultado[posicao][5])
        print(' ')
    return True