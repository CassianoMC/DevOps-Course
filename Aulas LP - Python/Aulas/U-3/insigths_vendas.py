import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Conectar ao banco de dados (ou criar se não existir)
conexao = sqlite3.connect('dados_vendas.db')

# Criando cursor
cursor = conexao.cursor()
cursor.execute("DROP TABLE IF EXISTS vendas1")

#Crando uma tabela
cursor.execute("""
CREATE TABLE vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)

""")

# Inserindo os dados
cursor.execute("""
INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
    ('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
    ('2023-01-05', 'Produto B', 'Roupas', 350.00),
    ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
    ('2023-03-15', 'Produto D', 'Livros', 200.00),
    ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
    ('2023-04-02', 'Produto F', 'Roupas', 400),
    ('2023-05-05', 'Produto G', 'Livros', 150.00),
    ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
    ('2023-07-20', 'Produto I', 'Roupas', 600.00),
    ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
    ('2023-09-30', 'Produto K', 'Livros', 300.00),
    ('2023-10-05', 'Produto L', 'Roupas', 450.00),
    ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
    ('2023-12-20', 'Produto N', 'Livros', 250.00);
""")

# Confirmando as mudanças
conexao.commit()
print("Base de dados configurada com sucesso!")


# Abrir o arquivo no banco de dados novamente
conexao = sqlite3.connect('dados_vendas.db')

# Leitura do Pandas e criação do DataFrame
df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)

# Fechando conexão
conexao.close()

# Preparação dos dados
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])
df_vendas['mes'] = df_vendas['data_venda'].dt.month
print("                       ---- TABELA ---- ")
print(df_vendas)

print("\n---- Informações das colunas ----")
df_vendas.info()

# Análise aprfundada dos dados
print("---- RELATÓRIO DE INSIGHTS DA EMPRESA ----\n")

# Receita total
receita_total = df_vendas['valor_venda'].sum()
print(f"1 - Receita Total do Ano: R$ {receita_total:.2f}")

# Tickey médio geral
ticket_medio_geral = df_vendas['valor_venda'].mean()
print(f"2 - Ticket Médio Geral: R$ {ticket_medio_geral:.2f}")

# Faturamento por categoria
faturamento_categoria = df_vendas.groupby('categoria')['valor_venda'].sum().sort_values(ascending=False)
print("\n3 - Faturamento por Categoria:")
print(faturamento_categoria.to_string())

# Quantidade de vendas por categoria
volume_categoria = df_vendas.groupby('categoria')['id_venda'].count().sort_values(ascending=False)
print("\n4 - Volume de Vendas por Categoria: ")
print(volume_categoria.to_string())

# Faturamento mensal
faturamento_mensal = df_vendas.groupby('mes')['valor_venda'].sum()
print("\n5 - Faturamento Mensal (Mês : Valor):")
print(faturamento_mensal.to_string())

# Maior e menor venda
linha_maior_venda = df_vendas.loc[df_vendas['valor_venda'].idxmax()]
linha_menor_venda = df_vendas.loc[df_vendas['valor_venda'].idxmin()]

print(f"\n6 - Extremos do Ano:")
print(f" - Maior Venda: {linha_maior_venda['produto']} (R$ {linha_maior_venda['valor_venda']:.2f}) em {linha_maior_venda['data_venda'].strftime('%d/%m/%Y')}")
print(f" - Menor Venda: {linha_menor_venda['produto']} (R$ {linha_menor_venda['valor_venda']:.2f}) em {linha_menor_venda['data_venda'].strftime('%d/%m/%Y')}")

# Participação percentual por categoria
share_categoria = (faturamento_categoria / receita_total) * 100
print("\n7 - Participação no Faturamento (%):")
for cat, valor in share_categoria.items():
    print(f" - {cat}: {valor:.1f}%")

sns.set_theme(style="whitegrid")

# Gráicos 1 e 2 -> Receita e Ticket
fig, ax = plt.subplots(figsize=(8, 2.5))
ax.axis('off') # Esconde as linhas do gráfico para ficar só o texto
ax.text(0.5, 0.7, f"1. Receita Total do Ano: R$ {receita_total:.2f}",
        fontsize=16, ha='center', fontweight='bold', color='darkblue')
ax.text(0.5, 0.3, f"2. Ticket Médio Geral: R$ {ticket_medio_geral:.2f}",
        fontsize=16, ha='center', fontweight='bold', color='darkgreen')
plt.title("Painel de Indicadores Gerais", fontsize=14, color='gray')
plt.show()

# Gráfico 3 -> Faturamento por categoria
plt.figure(figsize=(8, 4))
sns.barplot(x=faturamento_categoria.index, y=faturamento_categoria.values, palette="viridis")
plt.title('3. Faturamento por Categoria (R$)', fontsize=14, fontweight='bold')
plt.ylabel('Valor (R$)')
plt.xlabel('Categoria')
plt.show()

# Gráfico 4 -> Volume de vendas
plt.figure(figsize=(8, 4))
sns.barplot(x=volume_categoria.index, y=volume_categoria.values, palette="mako")
plt.title('4. Volume de Vendas por Categoria (Qtd)', fontsize=14, fontweight='bold')
plt.ylabel('Número de Notas Fiscais')
plt.xlabel('Categoria')
plt.show()

# Gráfico 5 -> Faturamento mensal
plt.figure(figsize=(8, 4))
sns.lineplot(x=faturamento_mensal.index, y=faturamento_mensal.values, marker='o', color='b', linewidth=2.5)
plt.title('5. Evolução do Faturamento Mensal', fontsize=14, fontweight='bold')
plt.xticks(range(1, 13))
plt.ylabel('Valor (R$)')
plt.xlabel('Mês')
plt.show()

# Gráfico 6 -> Extremos de vendas no ano
plt.figure(figsize=(6, 5))

data_maior = linha_maior_venda['data_venda'].strftime('%d/%m/%Y')
data_menor = linha_menor_venda['data_venda'].strftime('%d/%m/%Y')

labels_extremos = [
    f"Maior Venda\n{linha_maior_venda['produto']}\n({data_maior})",
    f"Menor Venda\n{linha_menor_venda['produto']}\n({data_menor})"
]
valores_extremos = [linha_maior_venda['valor_venda'], linha_menor_venda['valor_venda']]

sns.barplot(x=labels_extremos, y=valores_extremos, palette=['teal', 'indianred'])

plt.title('6. Extremos de Vendas do Ano (R$)', fontsize=14, fontweight='bold')
plt.ylabel('Valor da Venda (R$)')
plt.show()


# Gráfico 7 -> Participação percentual
plt.figure(figsize=(6, 6))
plt.pie(share_categoria.values, labels=share_categoria.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("Set2"))
plt.title('7. Participação no Faturamento (%)', fontsize=14, fontweight='bold')
plt.show()