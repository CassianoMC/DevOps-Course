#Criando um conjunto vazio

meu_conjunto = set()

#Adicionando elementos ao conjunto

meu_conjunto.add(10)
meu_conjunto.add(15)
meu_conjunto.add(30)

#Imprimindo o conjunto

print("Conjunto após adicionar elementos: ", meu_conjunto)

#Verificando se um elemento está no conjunto

elemento = 20
if elemento in meu_conjunto:
  print(f"{elemento} está no conjunto.")
else:
    print(f"{elemento} não está no conjunto.")

#Removendo elemento do conjunto

meu_conjunto.remove(15)

#Imprimindo o conjunto atualizado

print("Conjunto após remover o elemento 15: ", meu_conjunto)
