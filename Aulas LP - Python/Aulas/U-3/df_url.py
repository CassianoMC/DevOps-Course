import pandas as pd

url = 'https://www.fdic.gov/bank-failures/failed-bank-list/'
dfs = pd.read_html(url)

print(type(dfs))
print(len(dfs)) # Quantidade de tabelas encontradas

# Explorando o DataFrame Resultante
df_bancos = dfs[0]

print("Dimensões (linhas, colunas): ", df_bancos.shape)
print("\nTipos de cada coluna: ")
print(df_bancos.dtypes)
print("\nPrimeiras 5 linhas: ")
print(df_bancos.head())