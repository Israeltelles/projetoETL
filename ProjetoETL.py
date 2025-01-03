import pandas as pd

# Importando e renomeando dados


def read_files(path, name_file, year_date, type_file):
    _file = f'{path}{name_file}.{type_file}'
    colspecs = [(2, 10),
                (10, 12),
                (12, 24),
                (27, 39),
                (56, 69),
                (69, 82),
                (82, 95),
                (108, 121),
                (152, 170),
                (170, 188)]

    names = ('data_pregao', 'codbdi', 'sigla_acao', 'nome_acao', 'preco_abertura',
        'preco_maximo', 'preco_minimo', 'preco_fechamento', 'qtd_negocios', 'volume_negocios')
    df = pd.read_fwf('I:\Python\Ibovespa\COTAHIST_A2022.TXT',
                colspecs=colspecs, names=names, skiprows=1)
    return df

# Tratando dados


def filter_stocks(df):
    df = df[df['codbdi'] == 2]
    df = df.drop(columns=['codbdi'])
    return df

# Ajustando campos data


def parse_date(df):
    df['data_pregao'] = pd.to_datetime(df['data_pregao'], format='%Y%m%d')
    return df

# df.dtypes serve para ver o tipo de arquivo na base de dados


def parse_values(df):
    df['preco_abertura'] = (df['preco_abertura'] / 100).astype(float)
    df['preco_maximo'] = (df['preco_maximo'] / 100).astype(float)
    df['preco_minimo'] = (df['preco_minimo'] / 100).astype(float)
    df['preco_fechamento'] = (df['preco_fechamento'] / 100).astype(float)
    return df

# Executando programa de ETL


def concat_files(path, name_file, year_date, type_file, final_file):
    for i, y in enumerate(year_date):
        df = read_files(path, name_file, y, type_file)
        df = filter_stocks(df)
        df = parse_date(df)
        df = parse_values(df)
        if i == 0:
            df_final = df
        else:
            df_final = pd.concat([df_final, df])
    df.to_csv(f'{path}//{final_file}', index=False)


# Executando programa de ETL
year_date = ['2022', '2023', '2024']
path = f'I:\Python\ibovespa'
name_file = 'COTAHIST_A'
type_file = 'txt'
final_file = 'all_ibovespa'

concat_files(path, name_file, year_date, type_file, final_file)
