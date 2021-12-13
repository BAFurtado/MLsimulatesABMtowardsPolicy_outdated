import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea


def plot_iqrs(data1, title, cols, save = True):
    """ Produces a violin plot with seaborn. data1 and data2 are two different pandas dataframes and cols is a list
    with the names of each column within both data that one wishes to produce the figure about.
    Title is a string with the name to be used
    :param data1: pandas DataFrame
    :param title: name of the plot
    :param cols: Columns to plot
    :return: None
    :save : default == True, if False, then the picture is not saved, only shown
    """
    rows, cs = max(1,(len(cols) // 4)), 4
    fig, axes = plt.subplots(nrows=rows, ncols=cs, squeeze=False)
    for i in range(rows):
        for j in range(cs):
            if len(cols) > i * 4 + j:
                sea.violinplot(x=cols[i * 4 + j], y='Tree', data=data1, ax=axes[i, j])
    fig.suptitle(title)

    """
    HOW TO INTERPRET IT: each box represents a policy, with 'one' being every case that had that particular policy used, and 'zero' with every other case. Within a violin, zero represents non-optimal and one represents optimal. Best case is specific policy has a larger plot at one and the options have a larget plot at zero: most of the cases of that policy are optimal and most of the cases that did not use that policy were not optimal
    """


    plt.show()
    fig.savefig(f'../text/figures/{title}.pdf', bbox_inches='tight') if save == True else None
    plt.close()

def test():

    # GOA 13/12/21 moved original main to here

    t = pd.read_csv('../../Tree_gdp_index_75_gini_index_25_1000000_temp_stats.csv', sep=';')
    print(t.shape)
    th = t.head(10000)
    c = pd.read_csv('../../current_gdp_index_75_gini_index_25_1000000_temp_stats.csv', sep=';')
    c.rename(columns={'0': 'Tree'}, inplace=True)
    plot_iqrs(th, 'title', ['POLICIES_buy', 'POLICIES_rent','POLICIES_no_policy', 'POLICIES_wage', ])

    return print('test plot iqr')


if __name__ == '__main__':

    csv = pd.read_csv('../../Tree_gdp_index_75_gini_index_25_1000000_temp_stats.csv',
                      sep=';')

    #first we loop in relation to ACP's
    for ACP in ['all', 'PROCESSING_ACPS_ARACAJU', 'PROCESSING_ACPS_BELEM', 'PROCESSING_ACPS_BELO HORIZONTE',
                'PROCESSING_ACPS_BRASILIA', 'PROCESSING_ACPS_CAMPINA GRANDE', 'PROCESSING_ACPS_CAMPINAS',
                'PROCESSING_ACPS_CAMPO GRANDE', 'PROCESSING_ACPS_CAMPOS DOS GOYTACAZES',
                'PROCESSING_ACPS_CAXIAS DO SUL', 'PROCESSING_ACPS_CRAJUBAR', 'PROCESSING_ACPS_CUIABA',
                'PROCESSING_ACPS_CURITIBA', 'PROCESSING_ACPS_FEIRA DE SANTANA', 'PROCESSING_ACPS_FLORIANOPOLIS',
                'PROCESSING_ACPS_FORTALEZA', 'PROCESSING_ACPS_GOIANIA', 'PROCESSING_ACPS_ILHEUS - ITABUNA',
                'PROCESSING_ACPS_IPATINGA', 'PROCESSING_ACPS_JOAO PESSOA', 'PROCESSING_ACPS_JOINVILLE',
                'PROCESSING_ACPS_JUIZ DE FORA', 'PROCESSING_ACPS_JUNDIAI', 'PROCESSING_ACPS_LONDRINA',
                'PROCESSING_ACPS_MACAPA', 'PROCESSING_ACPS_MACEIO', 'PROCESSING_ACPS_MANAUS',
                'PROCESSING_ACPS_MARINGA', 'PROCESSING_ACPS_NATAL', 'PROCESSING_ACPS_NOVO HAMBURGO - SAO LEOPOLDO',
                'PROCESSING_ACPS_PELOTAS - RIO GRANDE', 'PROCESSING_ACPS_PETROLINA - JUAZEIRO',
                'PROCESSING_ACPS_PORTO ALEGRE', 'PROCESSING_ACPS_RECIFE', 'PROCESSING_ACPS_RIBEIRAO PRETO',
                'PROCESSING_ACPS_RIO DE JANEIRO', 'PROCESSING_ACPS_SALVADOR', 'PROCESSING_ACPS_SANTOS',
                'PROCESSING_ACPS_SAO JOSE DO RIO PRETO', 'PROCESSING_ACPS_SAO JOSE DOS CAMPOS',
                'PROCESSING_ACPS_SAO LUIS', 'PROCESSING_ACPS_SAO PAULO', 'PROCESSING_ACPS_SOROCABA',
                'PROCESSING_ACPS_TERESINA', 'PROCESSING_ACPS_UBERLANDIA', 'PROCESSING_ACPS_VITORIA',
                'PROCESSING_ACPS_VOLTA REDONDA - BARRA MANSA']:

        if ACP == 'all':
            plot_df = csv
        else:
            plot_df = csv.loc[csv[ACP] == 1]

        plot_iqrs(plot_df, str(ACP), ['POLICIES_no_policy', 'POLICIES_buy', 'POLICIES_rent', 'POLICIES_wage', ])

        # for some bizarre reason, if the last policy is 'POLICIES_no_policy', the '1's are ignored. Do not know why


    # with that we have a csv (on this folder) with the combined information per ACP.
    # TODO p-value (yet to find a less cumbersome method)

    # GOA 11/12/12: attempting to get a cities per policy image

    for pol in ['POLICIES_buy', 'POLICIES_no_policy', 'POLICIES_rent', 'POLICIES_wage']:
        print('tbd')
        # plot_iqrs(csv.loc[csv[pol] == 1], pol, ['PROCESSING_ACPS_ARACAJU', 'PROCESSING_ACPS_BELEM']) This first attempt won't work: for everything but that ACP is zero, so the sizes will be all messed up. Need to cut between figures and then add manually (try to do within python)
