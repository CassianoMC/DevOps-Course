# Idade média dos clientes
import pandas as pd

# Dados dos clientes
dados = {
    'Nome': ['João', 'Maria', 'José', 'Joana', 'Luisa'],
    'Idade': [25, 30, 22, 35, 28],
}

# Criar uma Series com idades indexadas pelo nome
serie_idades = pd.Series(dados['Idade'], index=dados['Nome'])

print("Série de Idades: ")
print(serie_idades)

# Calculando a média de idades
media_idades = serie_idades.mean()
print(f"\nMédia de idades: {media_idades}")

# Outras estatísticas que ajudam na decisão

print(f"Idade mínima: {serie_idades.min()}")
print(f"Idade máxima: {serie_idades.max()}")