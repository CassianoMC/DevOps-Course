import logging
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pipeline_gold import executar_pipeline_ouro
 
# CONFIGURAÇÕES GLOBAIS E ESTILIZAÇÃO VISUAL
# Define formatação do log, paletas de cores padrão e configurações de 
# Garantir que todos os gráficos tenham a mesma identidade visual.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

AZUL_CORPORATIVO = "#1f4e78"
AZUL_SECUNDARIO = "#2f5597"
PALETA_CATEGORICA = "Blues_r"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.titleweight": "bold",
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
})
sns.set_theme(style="whitegrid")

# Criação do diretório de saída
PASTA_SAIDA = Path("relatorios_graficos")
PASTA_SAIDA.mkdir(parents=True, exist_ok=True)

def salvar_grafico(nome_arquivo):
    """Função utilitária para padronizar o salvamento dos gráficos e liberar memória."""
    caminho = PASTA_SAIDA / nome_arquivo
    plt.tight_layout()
    plt.savefig(str(caminho), dpi=300, bbox_inches="tight")
    plt.close()
    logging.info(f"Gráfico gerado com sucesso: {caminho}")


# Funções de plotagem

# Abismo Digital
def plotar_abismo_digital(df):
    plt.figure(figsize=(9, 5))
    ax = sns.barplot(
        data=df, x="Acesso_Internet", y="Nota_Media_Geral",
        hue="Posse_Computador", palette=["#8faadc", AZUL_CORPORATIVO]
    )
    plt.title("Acesso à Tecnologia e Desempenho Médio no ENEM 2023")
    plt.xlabel("Acesso à Internet")
    plt.ylabel("Nota Média Geral")
    plt.legend(title="Posse de Computador")
    plt.ylim(0, 1000)
    for container in ax.containers:
        ax.bar_label(container, fmt="%.1f", padding=3, fontweight="bold")
    salvar_grafico("1_abismo_digital.png")

# Escola Pública vs Privada
def plotar_escola_rede(df):
    plt.figure(figsize=(7, 5))
    ax = sns.barplot(
        data=df, x="Tipo_de_Escola", y="Nota_Media_Geral",
        hue="Tipo_de_Escola", palette=[AZUL_SECUNDARIO, AZUL_CORPORATIVO], legend=False
    )
    plt.title("Disparidade de Desempenho: Escola Pública vs Privada")
    plt.xlabel("Tipo de Escola")
    plt.ylabel("Nota Média Geral")
    plt.ylim(0, 1000)
    for container in ax.containers:
        ax.bar_label(container, fmt="%.1f", padding=3, fontweight="bold")
    salvar_grafico("2_escola_rede.png")

# Curva de Renda
def plotar_curva_renda(df):
    plt.figure(figsize=(10, 5))
    # Limpeza dos rótulos para melhor visualização no eixo X
    df['Faixa_Salarial_Curta'] = df['Faixa_Salarial'].str.replace(r'^\d+\.\s*', '', regex=True)
    
    ax = sns.barplot(
        data=df, x="Faixa_Salarial_Curta", y="Nota_Media_Geral",
        hue="Faixa_Salarial_Curta", palette=PALETA_CATEGORICA, legend=False
    )
    plt.title("Impacto da Renda Familiar na Pontuação Geral")
    plt.xlabel("Faixa Salarial")
    plt.ylabel("Nota Média Geral")
    plt.xticks(rotation=45, ha="right", fontsize=8)
    plt.ylim(0, 1000)
    for container in ax.containers:
        ax.bar_label(container, fmt="%.0f", padding=3, size=7)
    salvar_grafico("3_curva_renda.png")

# Herança Materna
def plotar_heranca_materna(df):
    plt.figure(figsize=(8, 4.5))
    ax = sns.barplot(
        data=df, x="Escolaridade_Mae", y="Nota_Media_Geral",
        hue="Escolaridade_Mae", palette=PALETA_CATEGORICA, legend=False
    )
    plt.title("Efeito da Escolaridade Materna (Famílias de Baixa Renda)")
    plt.xlabel("Escolaridade da Mãe")
    plt.ylabel("Nota Média Geral")
    plt.ylim(0, 1000)
    for container in ax.containers:
        ax.bar_label(container, fmt="%.1f", padding=3, size=8, fontweight="bold")
    salvar_grafico("4_heranca_materna.png")

# Ranking Extremos de Estados
def plotar_ranking_estados(df):
    plt.figure(figsize=(10, 5))
    df_ord = df.sort_values("Media_Geral", ascending=False)
    # Seleciona os 5 melhores e os 5 piores estados para contraste
    df_extremos = pd.concat([df_ord.head(5), df_ord.tail(5)])

    ax = sns.barplot(
        data=df_extremos, x="Estado", y="Media_Geral",
        hue="Estado", palette=PALETA_CATEGORICA, legend=False
    )
    plt.title("Top 5 Maiores e Menores Médias por Estado (ENEM 2023)")
    plt.xlabel("Estado (UF)")
    plt.ylabel("Nota Média Geral")
    plt.ylim(0, 1000)
    for container in ax.containers:
        ax.bar_label(container, fmt="%.1f", padding=3, size=8, fontweight="bold")
    salvar_grafico("5_ranking_estados.png")

# Ranking Regiões
def plotar_ranking_regioes(df):
    plt.figure(figsize=(9, 5))
    df_ord = df.sort_values("Media_Geral", ascending=False)
    ax = sns.barplot(
        data=df_ord, x="Regiao", y="Media_Geral",
        hue="Regiao", palette=PALETA_CATEGORICA, legend=False
    )
    plt.title("Desempenho Médio no ENEM 2023 por Região")
    plt.xlabel("Região")
    plt.ylabel("Nota Média Geral")
    plt.ylim(0, 1000)
    for container in ax.containers:
        ax.bar_label(container, fmt="%.1f", padding=3, fontweight="bold")
    salvar_grafico("6_ranking_regioes.png")

# Top 15 Cidades
def plotar_top_cidades(df):
    plt.figure(figsize=(10, 6))
    df_top = df.sort_values("Media_Geral", ascending=False).head(15).copy()
    df_top["Cidade_UF"] = df_top["Cidade"] + " (" + df_top["Estado"] + ")"

    ax = sns.barplot(
        data=df_top, x="Media_Geral", y="Cidade_UF",
        hue="Cidade_UF", palette="Blues_r", legend=False
    )
    plt.title("Top 15 Cidades com Maior Média Geral (Mín. 100 Alunos)")
    plt.xlabel("Nota Média Geral")
    plt.ylabel("Município")
    plt.xlim(0, 1000)
    for container in ax.containers:
        ax.bar_label(container, fmt="%.1f", padding=3, size=8, fontweight="bold")
    salvar_grafico("7_top_cidades.png")

# Taxa de Inclusão Estadual (NOVO)
def plotar_inclusao_estadual(df):
    plt.figure(figsize=(12, 5))
    df_ord = df.sort_values("Taxa_Inclusao_Pct", ascending=False)
    ax = sns.barplot(
        data=df_ord, x="Estado", y="Taxa_Inclusao_Pct",
        hue="Estado", palette=PALETA_CATEGORICA, legend=False
    )
    plt.title("Taxa de Inclusão Digital (Internet + Computador) por Estado (%)")
    plt.xlabel("Estado (UF)")
    plt.ylabel("Inclusão (%)")
    plt.ylim(0, 100)
    salvar_grafico("8_inclusao_estadual.png")

# Extremos de Renda Estadual (NOVO)
def plotar_extremos_renda(df):
    plt.figure(figsize=(12, 5))
    df_ord = df.sort_values("Pct_Baixa_Renda", ascending=False)
    # Reestruturação para plotagem lado a lado das duas métricas
    df_melted = df_ord.melt(
        id_vars="Estado", 
        value_vars=["Pct_Baixa_Renda", "Pct_Elite"], 
        var_name="Classe", value_name="Porcentagem"
    )
    
    ax = sns.barplot(
        data=df_melted, x="Estado", y="Porcentagem", hue="Classe",
        palette=["#e74c3c", "#2ecc71"] # Vermelho (Baixa Renda) e Verde (Elite)
    )
    plt.title("Matriz de Extremos Sociais por Estado (% Baixa Renda vs Elite)")
    plt.xlabel("Estado (UF)")
    plt.ylabel("Proporção (%)")
    plt.legend(title="Segmento Social", labels=["Baixa Renda (Até 1 SM)", "Elite (+20 SM)"])
    salvar_grafico("9_extremos_renda.png")


# Orquestração dos relatórios
def gerar_todos_os_graficos():
    """Garante a execução das 9 queries e faz o roteamento exato para as 9 funções."""
    dfs = executar_pipeline_ouro()
    logging.info(f"Gerando relatórios visuais a partir de {len(dfs)} Data Marts...")

    # Mapeamento das tabelas retornadas pelo pipeline_gold
    mapeamento = {
        "tb_ouro_abismo_digital": plotar_abismo_digital,
        "tb_ouro_escola_rede": plotar_escola_rede,
        "tb_ouro_curva_renda": plotar_curva_renda,
        "tb_ouro_heranca_materna": plotar_heranca_materna,
        "tb_ouro_ranking_estados": plotar_ranking_estados,
        "tb_ouro_ranking_regioes": plotar_ranking_regioes,
        "tb_ouro_ranking_cidades": plotar_top_cidades,
        "tb_ouro_inclusao_estadual": plotar_inclusao_estadual,
        "tb_ouro_extremos_renda_estadual": plotar_extremos_renda
    }

    for tabela, funcao_plot in mapeamento.items():
        if tabela in dfs:
            funcao_plot(dfs[tabela])
        else:
            logging.warning(f"Tabela {tabela} não encontrada no banco de dados!")

    logging.info(f"Relatórios visuais finalizados na pasta: '{PASTA_SAIDA.resolve()}'")

if __name__ == "__main__":
    gerar_todos_os_graficos()