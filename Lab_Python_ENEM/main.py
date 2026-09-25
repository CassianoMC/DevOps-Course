import logging
from etl_pipeline import enem_pipeline
from pipeline_gold import executar_pipeline_ouro
from gerar_graficos import gerar_todos_os_graficos

# Configuração global dos Logs para execução principal
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

def rodar_laboratorio():
    logging.info("=== INICIANDO PIPELINE COMPLETO DO LABORATÓRIO (ENEM 2023) ===")
    
    # Etapa Silver: Extração, Transformação e Carga inicial no SQLite
    logging.info("Etapa 1/3: Processando ETL (Bronze -> Silver)...")
    enem_pipeline.extract()
    enem_pipeline.transform()
    enem_pipeline.load()
    
    # Etapa Gold: Execução dos Data Marts no banco
    logging.info("Etapa 2/3: Executando Camada Analítica Gold no SQLite...")
    executar_pipeline_ouro()
    
    # Etapa de Dashboard: Geração dos gráficos
    logging.info("Etapa 3/3: Gerando Relatórios Executivos...")
    gerar_todos_os_graficos()
    
    logging.info("=== PROCESSAMENTO FINALIZADO COM SUCESSO! ===")

if __name__ == "__main__":
    rodar_laboratorio()