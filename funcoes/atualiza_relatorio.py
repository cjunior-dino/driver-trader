from funcoes.adiciona_carrinho import *
from funcoes.importa_relatorio import *
def atualiza_relatorio():
    
    with open(r'banco_de_dados\relatorio\relatorio.csv', 'w',encoding='utf-8') as arquivo_dois:
        arquivo_dois.write('codigo' + ';' + 'nome' + ';' + 'marca' + ';' + 'categoria' + ';' + 'quantidade' + ';' + 'preco' + ';'+ 'total' +'\n')
        for i in relatorio:
            print(relatorio)
            for j in carrinho:
                print("entrou j")
                codigo, nome, marca, categoria, quantidade, preco = i
                codigo2, nome2, marca2, categoria2, quantidade2, preco2 = j
                if codigo2 == codigo:
                    total = int(quantidade) + int(quantidade2)
                    arquivo_dois.write(codigo + ';' + nome + ';' + marca + ';' + categoria + ';' + str(total) + ';' + preco + '\n')
                    break
            else:
                arquivo_dois.write(codigo + ';' + nome + ';' + marca + ';' + categoria + ';' + quantidade + ';' + preco + '\n')
        