import pandas as pd

MR_dict = {
    'Região Administrativa Integrada de Desenvolvimento do Polo Petrolina/PE e Juazeiro/BA': 'Petrolina-Juazeiro',
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
    'Região Metropolitana do Vale do Paraíba e Litoral Norte': 'SJC',
    'Uberlândia': 'Uberlândia',
    'São José do Rio Preto': 'SJRP',
    'Volta Redonda - Barra Mansa': 'Volta Redonda',
    'Campos dos Goytacazes': 'Campos',
    'Ilhéus - Itabuna': "Ilhéus–Itabuna",
    'Juiz de Fora': 'Juiz de Fora',
    'Novo Hamburgo - São Leopoldo': 'NH-SL'}


def dataframe_ready(gini_csv, GDP_csv, pop_csv):
    """
    We have to go to the pib DF, get each região metropolitana's full list of municipalities and produce their
aggregated GDP and gini index, then select for each of the 46 MRs that we analyze and build a ranking for them:
First we sort by GDP and give the first one 46 points, the second 45 and so on, and then we do the same for gini
but inverted in the sorted. Lastly we sum the two (alpha=.5) and
    :return: a dataframe with the information for each municipality of each of the 46 analyzed MRs (gini, population
    and gdp)
    """
    gini = pd.read_csv(gini_csv,
                       sep=';', skiprows=2, encoding='latin-1')
    gdp = pd.read_csv(GDP_csv,
                      sep=';', encoding='latin-1')
    pop = pd.read_csv(pop_csv,
                      sep=';', skiprows=3, encoding='latin-1')

    exit_df = pd.DataFrame(columns=['cod', 'mun', 'MR', 'gini', 'gdp', 'pop'])

    for cod in gdp['Código do Município'].tolist():
        # iterate over municipal codes

        if gdp.loc[gdp['Código do Município'] == cod]['Região Metropolitana'].values[0] in MR_dict:
            # if the municipality is within a certain metropolitan region that we analyze, it enters the dataframe
            try:
                # use the try (there are more municipalities now than in 2010...)
                current_row = {'cod': cod,
                               'mun': gdp.loc[gdp['Código do Município'] == cod]['Nome do Município'].values[0],
                               'MR': MR_dict[
                                   gdp.loc[gdp['Código do Município'] == cod]['Região Metropolitana'].values[0]],
                               'gini': gini.loc[gini['cod'] == cod].values[0][2],
                               'gdp': gdp.loc[gdp['Código do Município'] == cod]['PIB'].values[0],
                               'pop': pop.loc[pop['cod'] == cod]['2021'].values[0]}
                # print(current_row)
                exit_df = exit_df.append(current_row, ignore_index=True)
            except (RuntimeError, TypeError, NameError, IndexError):
                print('no', cod, 'municipality on the database')
                pass

    return exit_df


def MR_ranking(entry_df):
    """
    We have to get the ranking for each MR. First we have to get the weighted average GDP and gini for each MR. Then we
    to give points to them: sort (gini inverted) and for the first we give one point, to the second 2 points and so on.
    Lastly we sum the points for each MR (with the alpha) and produce the index

    :param entry_df:
    :param alpha:
    :return: ranked_MRs
    """

    ranked_MRs = pd.DataFrame(columns=['MR', 'gini_r', 'gdp_r', 'gini_t', 'gdp_t', 'rank'])

    for mr in MR_dict:
        MR = MR_dict[mr]
        temp_df = entry_df.loc[entry_df['MR'] == MR]
        total_pop = temp_df['pop'].sum()
        temp_dict = {'MR': MR,
                     'gdp': temp_df.groupby('gdp').sum(),
                     'gini': 0}
        for cod in temp_df['cod'].tolist():
            temp_dict['gini'] += temp_df.loc[temp_df['cod'] == cod]['gini'].values[0] * \
                                 temp_df.loc[temp_df['cod'] == cod]['pop'].values[0]
        total_gini = temp_dict['gini'] / total_pop
        new_row = {'MR': MR,
                   'gini_r': 0,
                   'gdp_r': 0,
                   'gini_t': total_gini,
                   'gdp_t': temp_df['gdp'].sum(),
                   }
        # print(new_row)
        ranked_MRs = ranked_MRs.append(new_row
                                       , ignore_index=True)

    ranked_MRs.sort_values('gdp_t', inplace=True)
    ranked_MRs['gdp_r'] = list(range(0, 46))  # only solution that I found...

    ranked_MRs.sort_values('gini_t', ascending=False, inplace=True)
    ranked_MRs['gini_r'] = list(range(0, 46))

    ranked_MRs['rank'] = ranked_MRs['gdp_r'] + ranked_MRs['gini_r']
    ranked_MRs.sort_values('rank', inplace=True, ascending=False)

    return ranked_MRs


if __name__ == '__main__':
    ready = dataframe_ready('ginibr.csv', 'PIB dos Municípios - base de dados 2010-2019.csv', 'tabela6579.csv')
    out_df = MR_ranking(ready)
    out_df.to_csv('actual_rank.csv', index=False, sep=';')
