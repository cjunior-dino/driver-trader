numero = []
id = 0
with open(r'banco_de_dados\historico\dados_nf.csv', 'r', encoding='utf-8') as arquivo:
    numeros = arquivo.readlines()

    for i in numeros:
        numero.append(i.strip('\n').split(';'))
    