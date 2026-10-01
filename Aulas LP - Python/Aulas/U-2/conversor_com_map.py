precos_em_dolares = input("Digite o valor em dólar: ")
precos_em_dolares = [float(x) for x in precos_em_dolares.split()]
taxa_de_cambio = 5.25
precos_em_reais = list(map(lambda x:x * taxa_de_cambio, precos_em_dolares))
print(f"Conversão para reais: R${sum(precos_em_reais):.2f}")