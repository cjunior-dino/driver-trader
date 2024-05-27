from funcoes.importa_arquivo import *

def cadastra():
    print("INFORME O NOME DO PRODUTO: ")
    nome_prod = input()
    print("INFORME A MARCA: ")
    marca_prod = input()
    
    for pesquisa in adicina():
            codigo, nome, marca, categoria, quantidade, preco = pesquisa       
            if nome_prod.lower() in nome.lower() and marca_prod.lower() in marca.lower():
                    print(f"ESSE PRODUTO EXISTE NO CADASTRO, O SEU CODIGO É {codigo}")
                    print(" ")
                    return True
    else:
            print("INFORME A CATEGORIA: ")
            categoria_prod = input()
            print("INFORME A QUANTIDADE: ")
            quantidade_prod = input()
            print("INFORME O PREÇO: ")
            preco_prod = input()
            cod, nom, mar, cat, quan, pre = adicina()[-1]
            codigo_prod = int(cod) + 1
            with open(r'banco_de_dados\produtos\dados.csv', 'a+',encoding='utf-8') as arquivo:
                    arquivo.write(str(codigo_prod) + ";" + nome_prod + ";" + marca_prod + ";" + categoria_prod + ";" + quantidade_prod + ";" + preco_prod + "\n")
            return True