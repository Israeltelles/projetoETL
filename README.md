# ETL – Dados Históricos do Ibovespa

Projeto de ETL (Extract, Transform, Load) desenvolvido em Python para processamento de dados históricos do Ibovespa a partir dos arquivos oficiais da B3 (COTAHIST).
O script realiza a leitura de arquivos .TXT, tratamento dos dados e consolidação das informações em um único arquivo estruturado.

## Tecnologias

- Python
- Pandas


## Funcionalidades

1. Leitura de arquivos de cotação histórica (read_fwf)
2. Extração de colunas relevantes por posição fixa
3. Filtro de ações (BDI = 2)
4. Conversão de datas e valores monetários
5. Consolidação de múltiplos anos em um único dataset
6. Exportação final em arquivo .csv

## Estrutura do Processo (ETL)

- Extract: leitura dos arquivos COTAHIST_AAAAA.TXT
- Transform: limpeza, padronização de datas e valores
- Load: geração de um arquivo final consolidado (CSV)

📥 Como obter o projeto
git clone https://github.com/seu-usuario/etl-ibovespa-python.git
cd etl-ibovespa-python

▶️ Como executar

## Ajuste o caminho dos arquivos no código:

1. path = 'I:/Python/ibovespa/'
2. Informe os anos desejados:
3. year_date = ['2022', '2023', '2024']
4. Execute o script:
5. python etl_ibovespa.py

O arquivo final será gerado em formato .csv no diretório definido.

# Status

Projeto finalizado e funcional, com possibilidade de melhorias futuras.

# Possíveis Evoluções

- Parametrização por linha de comando
- Tratamento de exceções e logs
- Integração com banco de dados (SQL Server / PostgreSQL)
- Automatização do download dos arquivos da B3
- Criação de análises e visualizações a partir do dataset

# Observação

Este projeto faz parte do meu portfólio e tem como objetivo aplicar conceitos práticos de engenharia de dados, tratamento de dados financeiros e organização de pipelines ETL. 
Aceito opiniões ou melhorias para o sistema, esse foi o primeiro programa funcional que criei, então não me julgem kkk
