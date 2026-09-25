import logging
import time
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, text
from queries_enem import RELATORIOS_SQL

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

# Garantir a criação das pastas se o arquivo for executado isoladamente
PASTA_DB = Path("data/database")
PASTA_DB.mkdir(parents=True, exist_ok=True)

DATABASE_URL = f"sqlite:///{PASTA_DB / 'enem_dados.db'}"
engine = create_engine(DATABASE_URL, echo=False)

def executar_pipeline_ouro():
    """Executa as consultas SQL analíticas e salva os Data Marts no banco."""
    dataframes_resultados = {}
    logging.info("Iniciando processamento da Camada Gold...")

    with engine.connect() as conexao:
        for nome_tabela, query in RELATORIOS_SQL.items():
            tempo_inicio = time.time()
            logging.info(f"Processando Data Mart: {nome_tabela}...")

            try:
                # Executa a query SQL e converte no DataFrame
                df_resultado = pd.read_sql(text(query), con=conexao)
                dataframes_resultados[nome_tabela] = df_resultado

                # Salva a tabela analítica (Gold) no próprio banco SQLite
                df_resultado.to_sql(nome_tabela, con=conexao, if_exists='replace', index=False)

                tempo_decorrido = round(time.time() - tempo_inicio, 2)
                logging.info(f"Sucesso! {nome_tabela} gerada com {len(df_resultado)} linhas em {tempo_decorrido}s")

            except Exception as e:
                logging.error(f"Erro ao gerar a tabela {nome_tabela}: {str(e)}")

    logging.info("Camada Gold concluída!")
    return dataframes_resultados 

if __name__ == "__main__":
    executar_pipeline_ouro()