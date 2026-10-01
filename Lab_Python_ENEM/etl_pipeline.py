import logging
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

# Configuração global de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

# CLASSE-PAI: Define o contrato básico para pipelines ETL
class BaseETLPipeline:
    def __init__(self, data_source):
        self.data_source = data_source
        self.dataframe = None

    def extract(self):
        raise NotImplementedError("Método extract() deve ser implementado na classe-filha.")

    def transform(self):
        raise NotImplementedError("Método transform() deve ser implementado na classe-filha.")

    def load(self):
        raise NotImplementedError("Método load() deve ser implementado na classe-filha.")

    def show_preview(self):
        if self.dataframe is not None:
            logging.info(f"\n{self.dataframe.head()}")
        else:
            logging.warning("Nenhum dado carregado no DataFrame.")


# CLASSE-FILHA: Implementa as regras específicas para o ENEM 2023
class EnemETLPipeline(BaseETLPipeline):
    
    def extract(self):
        logging.info(f"Extraindo dados do arquivo: {self.data_source}...")
        
        # Seleção das colunas necessárias
        colunas_alvo = [
            'NU_INSCRICAO',
            'SG_UF_PROVA', 'NO_MUNICIPIO_PROVA',                                       # Geografia
            'TP_ESCOLA',                                                               # Tipo de Escola
            'NU_NOTA_MT', 'NU_NOTA_REDACAO', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', # Notas
            'Q001', 'Q002', 'Q006', 'Q024', 'Q025'                                     # Socioeconômico
        ]
        
        # Leitura com codificação padrão dos arquivos do INEP
        self.dataframe = pd.read_csv(
            self.data_source,
            sep=';',
            encoding='latin1',
            usecols=colunas_alvo
        )
        logging.info(f"Sucesso! Total de alunos carregados: {len(self.dataframe)}")

    def transform(self):
        logging.info("Iniciando transformações e tratamento de dados...")
        
        # Filtro: Remove candidatos que faltaram na Redação ou Matemática
        self.dataframe = self.dataframe.dropna(subset=['NU_NOTA_REDACAO', 'NU_NOTA_MT'])

        # Média Geral: Média simples entre as 5 notas da prova
        logging.info("Calculando a Média Geral das notas...")
        self.dataframe['MEDIA_GERAL'] = self.dataframe[
            ['NU_NOTA_REDACAO', 'NU_NOTA_MT', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC']
        ].mean(axis=1)

        # Mapeamento Socioeconômico 
        renda_map = {
            'A': '01. Nenhuma Renda', 'B': '02. Até 1 salário', 'C': '03. Até 1.5 salários',
            'D': '04. Até 2 salários', 'E': '05. Até 2.5 salários', 'F': '06. Até 3 salários',
            'G': '07. Até 4 salários', 'H': '08. Até 5 salários', 'I': '09. Até 6 salários',
            'J': '10. Até 7 salários', 'K': '11. Até 8 salários', 'L': '12. Até 9 salários',
            'M': '13. Até 10 salários', 'N': '14. Até 12 salários', 'O': '15. Até 15 salários',
            'P': '16. Até 20 salários', 'Q': '17. Mais de 20 salários'
        }
        self.dataframe['RENDA_DESC'] = self.dataframe['Q006'].map(renda_map)

        # Mapeamento do tipo de escola
        escola_map = {1: 'Não Respondeu', 2: 'Pública', 3: 'Privada'}
        self.dataframe['TIPO_ESCOLA_DESC'] = self.dataframe['TP_ESCOLA'].map(escola_map)

    def load(self):
        logging.info("Iniciando carga no banco SQLite...")
        
        # Garante a criação da estrutura de pastas
        pasta_db = Path("data/database")
        pasta_db.mkdir(parents=True, exist_ok=True)
        
        caminho_db = pasta_db / "enem_dados.db"
        engine = create_engine(f"sqlite:///{caminho_db}")

        # Salva o DataFrame na tabela 'desempenho_enem'
        self.dataframe.to_sql(
            name='desempenho_enem',
            con=engine,
            if_exists='replace',
            index=False
        )
        logging.info(f"Carga concluída com sucesso no banco: {caminho_db}")


# Instanciação global para o pipeline
enem_pipeline = EnemETLPipeline("data/raw/MICRODADOS_ENEM_2023.csv")

# Bloco de segurança para evitar execução automática na importação
if __name__ == "__main__":
    enem_pipeline.extract()
    enem_pipeline.transform()
    enem_pipeline.load()