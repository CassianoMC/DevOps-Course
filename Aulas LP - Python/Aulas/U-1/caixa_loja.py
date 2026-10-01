#Funções definidas por mim.
def calcular_desconto (valor, percentual):
#Calcula o valor final aplicando um desconto percentual.
    if percentual < 0 or percentual > 100:
      return None #marcação inválida
    desconto = valor * (percentual/100)
    return valor - desconto

def registrar_venda(produto, valor_final):
#Imprime registro de venda.
    print(f"Venda registrada: {produto} por R$ {valor_final:.2f}")

#Variáveis principais do PDV
total_vendas = 0
qtd_vendas = 0

#Função lambda para arrendondar
arredondar = lambda v: round(v,2)

#Loop principal do caixa. MINHALOJAPDV
while True:
  print("\n ----- Minha Loja. ----- PDV -----")
  print("1 - Registrar venda.")
  print("2 - Ver relatório de vendas.")
  print("0 - Encerrar caixa.")
  opcao = input("Escolha a opção desejada: ")

  if opcao == "0":
    print("Encerrando o caixa. Até Amanhã")
    break

  elif opcao == "1":
    produto = input("Digite o nome do produto: ")
    valor = float(input("Valor do produto: R$" ))
    percentual = float(input("Desconto (%): "))

    valor_final = calcular_desconto(valor,percentual)

    if valor_final is None:
      print("Desconto inválido! Use um valor entre 0 e 100.")
    else:
      valor_final = arredondar(valor_final)
      registrar_venda(produto, valor_final)
      total_vendas = total_vendas + valor_final
      qtd_vendas = qtd_vendas + 1

  elif opcao == "2":
      print(f"\nVendas hoje: {qtd_vendas}")
      print(f"Total faturado: R$ {arredondar(total_vendas)}")
  else:
    print("Opção inválida. Tente novamente. ")