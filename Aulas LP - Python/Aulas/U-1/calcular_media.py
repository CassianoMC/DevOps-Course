def calcular_media (soma_notas, num_notas):
    media = soma_notas / num_notas
    return media


Nota1 = int(input("DIGITE A NOTA1: "))
Nota2 = int(input("DIGITE A NOTA2: "))
Nota3 = int(input("DIGITE A NOTA3: "))
Nota4 = int(input("DIGITE A NOTA4: "))
Nota5 = int(input("DIGITE A NOTA5: "))

divisao = 5 # Assuming there are 5 notes for the average
soma_total_notas = Nota1 + Nota2 + Nota3 + Nota4 + Nota5

media = calcular_media(soma_total_notas, divisao)


print(media)
if media >= 7:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print(f'{situacao}')