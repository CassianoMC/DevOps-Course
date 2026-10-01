def calcular_area(base, altura):
  area = base * altura
  return area

base = int(input("Digite a base: "))
altura = int(input("Digite a altura: "))
resultado = calcular_area(base, altura)
print(f"O tamanho da área é: {resultado}")