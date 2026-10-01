import matplotlib.pyplot as plt

# Dados de exemplo
meses = ['Janeiro', 'Fevereiro', 'Marcço', 'Abril', 'Maio', 'Junho']
vendas = [150, 570, 350, 400, 80, 750]

# Criar um gráfico de barras
plt.bar(meses, vendas, color='darkgreen')

# Adicionar rótulos aos eixos
plt.xlabel('Mes')
plt.ylabel('Vendas (em unidades)')

# Adicionar um título ao gráfico
plt.title('Vendas Mensais')

# Mostrar gráfico
plt.show()