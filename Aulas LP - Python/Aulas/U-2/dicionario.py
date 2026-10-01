#Exemplo 1 - Criação de um dicionário vazio, seguido de adtribiução de chaves e valores
dici_1 = {}
dici_1['nome'] = "Maria"
dici_1['idade'] = 25

#Exemplo 2 - Criação de um dicionário com prares chave valor
dici_2 = {'nome':'Maria', 'idade':25}

#Exemplo 3 - Criação de um dicionário com uma lista de tuplas representando pares chave:valor
dici_3 = dict([('nome', "Maria"),('idade',25)])

#Exemplo 4 - Criação de um dicionário usando a função built-in zip() e duas listas, uma para as chaves e outra para os valores
dici_4 = dict(zip(['nome', 'idade'], ["Maria",25]))

#Teste de todas as contruções resultam em objetos iguais
print(dici_1 == dici_2 == dici_3 == dici_4)
print(dici_1)
