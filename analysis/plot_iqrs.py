import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
import groups_cols
import itertools


def plot_iqrs(data1, title, cols, save=True, format='png', y='Tree'):
    """ Produces a violin plot with seaborn. data1 is a pandas dataframe and cols is a list
    with the names of each column within both data that one wishes to produce the figure about.
    Title is a string with the name to be used
    :param data1: pandas DataFrame
    :param title: name of the plot
    :param cols: Columns to plot
    :param format: default == png, can be changed to pdf or any other type
    :param save: default == True, if False, then the picture is not saved, only shown
    :return: None
    """
    rows, cs = max(1, (len(cols) // 4)), 4
    fig, axes = plt.subplots(nrows=rows, ncols=cs, squeeze=False)
    for i in range(rows):
        for j in range(cs):
            if len(cols) > i * 4 + j:
                sea.violinplot(x=cols[i * 4 + j], y=y, data=data1, ax=axes[i, j])
    fig.set_size_inches(11.69, 8.27) if rows > 1 else None
    # fig.tight_layout()
    fig.suptitle(title)

    """
    HOW TO INTERPRET IT: each box represents a policy, with 'one' being every case that had that particular policy used, and 'zero' with every other case. Within a violin, zero represents non-optimal and one represents optimal. Best case is specific policy has a larger plot at one and the options have a larget plot at zero: most of the cases of that policy are optimal and most of the cases that did not use that policy were not optimal
    """

    plt.show()
    fig.savefig(f'../text/figures/{title}.{format}', bbox_inches='tight') if save == True else None
    plt.close()


if __name__ == '__main__':

    csv = pd.read_csv('../../Tree_gdp_index_75_gini_index_25_1000000_temp_stats.csv',
                      sep=';')

    acps = ['all'] + groups_cols.abm_dummies['acps']

    # first we loop in relation to ACP's
    for ACP in acps:

        if ACP == 'all':
            plot_df = csv
        else:
            plot_df = csv.loc[csv[ACP] == 1]

        plot_iqrs(plot_df, str(ACP),
                  groups_cols.abm_dummies['policies'], save=False)

        # for some bizarre reason, if the last policy is 'POLICIES_no_policy', the '1's are ignored. Do not know why

    # GOA 11/12/12: attempting to get a cities per policy image

    for pol in groups_cols.abm_dummies['policies']:
        plot_iqrs(csv.loc[csv[pol] == 1], pol,
                  groups_cols.abm_dummies['acps'], save=False)

    # It is now working for policies per ACP, but is too squeezed

    dummies = list(itertools.chain.from_iterable(groups_cols.abm_dummies.values()))
    dummies = [elem for elem in dummies if elem not in groups_cols.abm_dummies["policies"]]
    dummies = [elem for elem in dummies if elem not in groups_cols.abm_dummies["acps"]]
    dummies = [elem for elem in dummies if elem != ('ALTERNATIVE0_False' or 'ALTERNATIVE0_True')]

    for dummy in dummies:
        for ACP in acps:
            if ACP == 'all':
                plot_df = csv.loc[csv[dummy] == 1]
            else:
                plot_df = csv.loc[(csv[dummy] == 1) & (csv[ACP] == 1)]

            plot_iqrs(plot_df,
                      str([ACP] + [dummy]),
                      groups_cols.abm_dummies['policies'])

        for pol in groups_cols.abm_dummies['policies']:
            plot_iqrs(csv.loc[(csv[dummy] == 1) & (csv[pol] == 1)],
                      str([pol] + [dummy]),
                      groups_cols.abm_dummies['acps'])

    params = groups_cols.abm_params
    for param in params:
        for ACP in groups_cols.abm_dummies['acps']:
            plot_df = csv.loc[(csv[ACP] == 1)]

            plot_iqrs(plot_df,
                      str([ACP] + [param]),
                      groups_cols.abm_dummies['policies'],
                      y=param)
