#Máquina de venda automática de ingressos de cinema:
#Solicita a idade do cliente

idade = int(input("Por favor, digite sua idade: "))
if idade < 12:
  print("Recomendamos o filme infantil FILME 1.")
elif 12 <= idade <18:
  print("Recomendamos o filme adolescente FILME 2.")
else:
  print("Recomendamos o emocionante FILME 3.")
15
#Verfica a disponibilidade de ingressos

quantidade_de_ingressos = 10
if quantidade_de_ingressos > 0:
  print("INGRESSOS DISPONÍVES. DIVIRTA-SE NO CINEMA!")
else:
  print("DESCULPE, TODOS OS INGRESSOS FORAM VENDIDOS")

  idade = int(input("DIGITE SUA IDADE: "))
if idade < 18:
  print("MENOR DE IDADE")
elif idade >= 18 and idade <= 65:
  print ("ADULTO")
else:
  print("IDOSO")