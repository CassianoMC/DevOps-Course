
# DICIONÁRIO CENTRALIZADOR DE CONSULTAS SQL (CAMADA GOLD / DATA MARTS)
# Este arquivo reúne as consultas analíticas executadas sobre a tabela 
RELATORIOS_SQL = {
    
    # Abismo digital  
    "tb_ouro_abismo_digital": """
        SELECT 
            CASE 
                WHEN Q025 = 'B' THEN 'Com Internet' 
                ELSE 'Sem Internet' 
            END as Acesso_Internet,
            CASE 
                WHEN Q024 = 'A' THEN 'Sem Computador' 
                ELSE 'Com Computador' 
            END as Posse_Computador,
            COUNT(NU_INSCRICAO) as Total_Alunos,
            ROUND(AVG(MEDIA_GERAL), 2) as Nota_Media_Geral
        FROM desempenho_enem
        GROUP BY Acesso_Internet, Posse_Computador
        ORDER BY Nota_Media_Geral DESC;
    """,

    
    # Tipo de escola
    "tb_ouro_escola_rede": """
        SELECT 
            TIPO_ESCOLA_DESC as Tipo_de_Escola,
            COUNT(NU_INSCRICAO) as Total_Alunos,
            ROUND(AVG(MEDIA_GERAL), 2) as Nota_Media_Geral
        FROM desempenho_enem
        WHERE TIPO_ESCOLA_DESC IN ('Pública', 'Privada')
        GROUP BY TIPO_ESCOLA_DESC
        ORDER BY Nota_Media_Geral DESC;
    """,

    # Curva de renda
    "tb_ouro_curva_renda": """
        SELECT 
            RENDA_DESC as Faixa_Salarial,
            COUNT(NU_INSCRICAO) as Total_Alunos,
            ROUND(AVG(MEDIA_GERAL), 2) as Nota_Media_Geral
        FROM desempenho_enem
        GROUP BY RENDA_DESC
        ORDER BY RENDA_DESC ASC;
    """,


    # Herança Educacional materna
    "tb_ouro_heranca_materna": """
        SELECT 
            CASE 
                WHEN Q002 = 'A' THEN '1. Nunca estudou'
                WHEN Q002 IN ('B', 'C') THEN '2. Ensino Fundamental'
                WHEN Q002 = 'D' THEN '3. Ensino Médio'
                WHEN Q002 IN ('E', 'F', 'G') THEN '4. Ensino Superior / Pós'
                ELSE '5. Não Sabe'
            END as Escolaridade_Mae,
            COUNT(NU_INSCRICAO) as Total_Alunos,
            ROUND(AVG(MEDIA_GERAL), 2) as Nota_Media_Geral
        FROM desempenho_enem
        WHERE RENDA_DESC IN ('01. Nenhuma Renda', '02. Até 1 salário', '03. Até 1.5 salários', '04. Até 2 salários') 
        GROUP BY Escolaridade_Mae
        ORDER BY Escolaridade_Mae;
    """,

    
    # Ranking completo por Estados (UF)
    # Maior e menor nota alcançada no estado e média da redação
    "tb_ouro_ranking_estados": """
        SELECT 
            SG_UF_PROVA as Estado,
            COUNT(NU_INSCRICAO) as Total_Alunos,
            ROUND(AVG(MEDIA_GERAL), 2) as Media_Geral,
            ROUND(MAX(MEDIA_GERAL), 2) as Maior_Nota_Geral,
            ROUND(MIN(MEDIA_GERAL), 2) as Menor_Nota_Geral,
            ROUND(AVG(NU_NOTA_REDACAO), 2) as Media_Redacao
        FROM desempenho_enem
        GROUP BY SG_UF_PROVA
        ORDER BY Media_Geral DESC;
    """,

    # Desempenho por regiões geográficas   
    "tb_ouro_ranking_regioes": """
        SELECT 
            CASE 
                WHEN SG_UF_PROVA IN ('AM', 'RR', 'AP', 'PA', 'TO', 'RO', 'AC') THEN 'Norte'
                WHEN SG_UF_PROVA IN ('MA', 'PI', 'CE', 'RN', 'PE', 'PB', 'SE', 'AL', 'BA') THEN 'Nordeste'
                WHEN SG_UF_PROVA IN ('MT', 'MS', 'GO', 'DF') THEN 'Centro-Oeste'
                WHEN SG_UF_PROVA IN ('SP', 'RJ', 'ES', 'MG') THEN 'Sudeste'
                WHEN SG_UF_PROVA IN ('PR', 'RS', 'SC') THEN 'Sul'
            END as Regiao,
            COUNT(NU_INSCRICAO) as Total_Alunos,
            ROUND(AVG(MEDIA_GERAL), 2) as Media_Geral,
            ROUND(MAX(MEDIA_GERAL), 2) as Maior_Nota_Geral,
            ROUND(MIN(MEDIA_GERAL), 2) as Menor_Nota_Geral,
            ROUND(AVG(NU_NOTA_REDACAO), 2) as Media_Redacao
        FROM desempenho_enem
        GROUP BY Regiao
        ORDER BY Media_Geral DESC;
    """,


    # Ranking de cidades
    "tb_ouro_ranking_cidades": """
        SELECT 
            NO_MUNICIPIO_PROVA as Cidade,
            SG_UF_PROVA as Estado,
            COUNT(NU_INSCRICAO) as Total_Alunos,
            ROUND(AVG(MEDIA_GERAL), 2) as Media_Geral,
            ROUND(MAX(MEDIA_GERAL), 2) as Maior_Nota_Geral,
            ROUND(AVG(NU_NOTA_REDACAO), 2) as Media_Redacao
        FROM desempenho_enem
        GROUP BY NO_MUNICIPIO_PROVA, SG_UF_PROVA
        HAVING COUNT(NU_INSCRICAO) >= 100
        ORDER BY Media_Geral DESC;
    """,

    # Taxa de inclusão digital por Estado
    "tb_ouro_inclusao_estadual": """
        SELECT 
            SG_UF_PROVA as Estado,
            COUNT(NU_INSCRICAO) as Total_Alunos,
            SUM(CASE WHEN Q025 = 'B' AND Q024 != 'A' THEN 1 ELSE 0 END) as Alunos_Conectados,
            ROUND((SUM(CASE WHEN Q025 = 'B' AND Q024 != 'A' THEN 1 ELSE 0 END) * 100.0) / COUNT(NU_INSCRICAO), 2) as Taxa_Inclusao_Pct
        FROM desempenho_enem
        GROUP BY SG_UF_PROVA
        ORDER BY Taxa_Inclusao_Pct DESC;
    """,

    # Matriz de extremos sociais
    "tb_ouro_extremos_renda_estadual": """
        SELECT 
            SG_UF_PROVA as Estado,
            COUNT(NU_INSCRICAO) as Total_Alunos,
            SUM(CASE WHEN RENDA_DESC IN ('01. Nenhuma Renda', '02. Até 1 salário') THEN 1 ELSE 0 END) as Qtd_Baixa_Renda,
            ROUND((SUM(CASE WHEN RENDA_DESC IN ('01. Nenhuma Renda', '02. Até 1 salário') THEN 1 ELSE 0 END) * 100.0) / COUNT(NU_INSCRICAO), 2) as Pct_Baixa_Renda,
            SUM(CASE WHEN RENDA_DESC = '17. Mais de 20 salários' THEN 1 ELSE 0 END) as Qtd_Elite,
            ROUND((SUM(CASE WHEN RENDA_DESC = '17. Mais de 20 salários' THEN 1 ELSE 0 END) * 100.0) / COUNT(NU_INSCRICAO), 2) as Pct_Elite
        FROM desempenho_enem
        GROUP BY SG_UF_PROVA
        ORDER BY Pct_Elite DESC;
    """
}