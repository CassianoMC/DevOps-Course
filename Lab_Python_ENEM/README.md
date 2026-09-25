# 📊 Lab_Python_ENEM (Análise de Microdados 2023)

Este projeto consiste em um pipeline de Engenharia de Dados (ETL) construído em Python para processar, limpar e analisar os microdados do ENEM 2023. O objetivo é extrair insights socioeconômicos e educacionais profundos aplicando a **Arquitetura Medallion** (Bronze, Silver e Gold).

## 🏗️ Arquitetura de Dados e Pipeline

A orquestração completa do projeto ocorre através do script principal `main.py`, que executa o fluxo em três grandes etapas:

1. **Camada Bronze (Dados Brutos)**
   - Ponto de partida: Arquivo original `MICRODADOS_ENEM_2023.csv` (armazenado em `data/raw/`).
   
2. **Camada Silver (Limpeza e Padronização) - `etl_pipeline.py`**
   - Utiliza a classe `EnemETLPipeline` (que herda os métodos de `BaseETLPipeline`).
   - **Extract:** Lê o CSV gigante e seleciona apenas as colunas-chave (Geografia, Tipo de Escola, Notas das 5 competências e Questionário Socioeconômico).
   - **Transform:** Remove candidatos ausentes nas provas de Redação ou Matemática, calcula a `MEDIA_GERAL` (média simples das 5 provas) e traduz dados qualitativos, mapeando faixas de renda (Q006) e tipos de escola (TP_ESCOLA).
   - **Load:** Carrega o DataFrame limpo em um banco de dados local **SQLite** (`data/database/enem_dados.db`), na tabela `desempenho_enem` usando SQLAlchemy.

3. **Camada Gold (Data Marts Analíticos) - `pipeline_gold.py` & `queries_enem.py`**
   - Executa 9 consultas SQL analíticas complexas (`RELATORIOS_SQL`) diretamente no SQLite.
   - Gera tabelas de Data Mart focadas em regras de negócio específicas, salvando os resultados agregados de volta no próprio banco de dados para consumo.

4. **Camada de Visualização (Dashboards) - `gerar_graficos.py`**
   - Consome os Data Marts consolidados gerados pela Camada Gold.
   - Utiliza as bibliotecas Matplotlib e Seaborn (com identidade visual corporativa padronizada e responsiva) para gerar 9 relatórios visuais que são salvos automaticamente na pasta `relatorios_graficos/`.

## 📈 Relatórios Analíticos Gerados

O pipeline de dados cria automaticamente os seguintes gráficos a partir das agregações:
- **Abismo Digital:** Impacto do acesso à internet e posse de computador na nota média.
- **Escola Pública vs Privada:** Disparidade de desempenho de acordo com a rede de ensino.
- **Curva de Renda:** Impacto direto da faixa salarial familiar na pontuação geral.
- **Herança Materna:** Efeito do nível de escolaridade da mãe em alunos de famílias de baixa renda.
- **Ranking de Estados e Regiões:** Extremos de desempenho e variação regional da média geral.
- **Top 15 Cidades:** Municípios com as maiores médias (exigindo amostragem mínima de 100 alunos).
- **Taxa de Inclusão Estadual:** Percentual demográfico de inclusão digital por UF.
- **Extremos de Renda:** Matriz cruzando a proporção de alunos de baixa renda vs. elite por Estado.

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Pandas:** Leitura massiva, limpeza, aplicação de regras de negócio e manipulação em memória.
- **SQLAlchemy & SQLite:** Motor de banco de dados relacional e armazenamento seguro da modelagem dimensional.
- **Matplotlib & Seaborn:** Estilização corporativa e renderização de dados visuais.

## 🚀 Como Executar o Projeto

1. Certifique-se de ter o Python instalado e crie um ambiente virtual na pasta do projeto (`venv`).
2. Instale as dependências: `pip install pandas sqlalchemy matplotlib seaborn`.
3. Baixe os Microdados do ENEM 2023 diretamente do portal do INEP e posicione o arquivo `.csv` extraído no diretório esperado pelo sistema: `data/raw/MICRODADOS_ENEM_2023.csv`.
4. No terminal, estando na raiz do projeto, execute o orquestrador:
   ```bash
   python main.py
