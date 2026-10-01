# Exemplo - 2
import pandas as pd

exemplo2 = {'A': 100, 'B': 200, 'C': 300, 'D': 400, 'E': 500}
series2 = pd.Series(data=exemplo2)
print(type,"\n", (series2))

# Métodos prontos para Series
print("Media: ", series2.mean())
print("Soma: ", series2.sum())
print("Máximo: ", series2.max())
print("Mínimo: ", series2.min())