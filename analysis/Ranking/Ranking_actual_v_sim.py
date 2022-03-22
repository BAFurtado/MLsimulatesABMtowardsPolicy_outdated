import pandas as pd


def dataframe_ready(gini_csv, GDP_csv, pop_csv):
    """
    We have to go to the pib DF, get each região metropolitana's full list of municipalities and produce their
aggregated GDP and gini index, then select for each of the 46 MRs that we analyze and build a ranking for them:
First we sort by GDP and give the first one 46 points, the second 45 and so on, and then we do the same for gini
but inverted in the sorted. Lastly we sum the two (alpha=.5) and
    :return: a dataframe with the ranking for each of the 46 analyzed MRs: 2010 gini, 2019 GDP and 2021
    """
    gini = pd.read_csv(gini_csv,
                      sep=';')
    gdp = pd.read_xls(GDP_csv,
                      sep=';')
    pop = pd.read_xls(pop_csv,
                      sep=';')

    exit_df = pd.DataFrame(columns=['cod', 'mun', 'MR', 'gini', 'gdp', 'pop'])
    MR_list = {'Região Administrativa Integrada de Desenvolvimento do Polo Petrolina/PE e Juazeiro/BA': 'Petrolina-Juazeiro',
               'Região Integrada de Desenvolvimento da Grande Teresina': 'Teresina',
               'Região Integrada de Desenvolvimento do Distrito Federal e Entorno': 'Brasília',
               'Região Metropolitana da Baixada Santista': 'Santos',
               'Região Metropolitana da Grande São Luís': 'São Luis',
               'Região Metropolitana da Grande Vitória': 'Vitória',
               'Região Metropolitana de Aracaju': 'Aracaju',
               'Região Metropolitana de Belém': 'Belém',
               'Região Metropolitana de Belo Horizonte': 'Belo Horizonte',
               'Região Metropolitana de Campina Grande': 'Campina Grande',
               'Região Metropolitana de Campinas': 'Campinas',
               'Região Metropolitana de Curitiba': 'Curitiba',
               'Região Metropolitana de Feira de Santana': 'Feira de Santana',
               'Região Metropolitana de Florianópolis': 'Florianópolis',
               'Região Metropolitana de Fortaleza': 'Fortaleza',
               'Região Metropolitana de Goiânia': 'Goiânia',
               'Região Metropolitana de João Pessoa': 'João Pessoa',
               'Região Metropolitana de Londrina': 'Londrina',
               'Região Metropolitana de Macapá': 'Macapá',
               'Região Metropolitana de Maceió': 'Maceió',
               'Região Metropolitana de Manaus': 'Manaus',
               'Região Metropolitana de Maringá': 'Maringá',
               'Região Metropolitana de Natal': 'Natal',
               'Região Metropolitana de Porto Alegre': 'Porto Alegre',
               'Região Metropolitana de Recife': 'Recife',
               'Região Metropolitana de Ribeirão Preto': 'Ribeirão Preto',
               'Região Metropolitana de Salvador': 'Salvador',
               'Região Metropolitana de São Paulo': 'São Paulo',
               'Região Metropolitana de Sorocaba': 'Sorocaba',
               'Região Metropolitana do Rio de Janeiro': 'Rio de Janeiro',
               'Região Metropolitana do Norte/Nordeste Catarinense': 'Joinville',
               'Região Metropolitana do Agreste': 'Campo Grande',
               'Aglomeração Urbana do Sul': 'Pelotas',
               'Região Metropolitana do Cariri': 'Crato',
               'Região Metropolitana do Vale do Rio Cuiabá': 'Cuiabá',
               'Região Metropolitana do Vale do Aço': 'Ipatinga',
               'Aglomeração Urbana de Jundiaí': 'Jundiaí',
               'Região Metropolitana da Serra Gaúcha': 'Caxias do Sul',
               'Região Metropolitana do Vale do Paraíba e Litoral Norte': 'SJC'}

    for cod in gdp['Código do Município'].tolist():
        # iterate over municipal codes
        if gdp.loc[gdp['Código do Município'] == cod]['Região Metropolitana'] in MR_list:
            # if the
            current_row = {'cod': cod,
                           'mun': '',
                           'MR': '',
                           'gini': '',
                           'gdp': '',
                           'pop': ''}
            exit_df = exit_df.append(current_row, ignore_index=True)


    return exit_df

def MR_ranking(entry_df, alpha=0.5):
    """

    :param entry_df:
    :param alpha:
    :return:
    """

    return ranked_MRs



if __name__ == '__main__':
    ready = dataframe_ready('ginibr.csv', 'PIB dos Municípios - base de dados 2010-2019.csv', 'tabela6579.csv')

