import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea


def plot_iqrs(data1, title, cols):
    """ Produces a violin plot with seaborn. data1 and data2 are two different pandas dataframes and cols is a list
    with the names of each column within both data that one wishes to produce the figure about.
    Title is a string with the name to be used
    :param data1: pandas DataFrame
    :param title: name of the plot
    :param cols: Columns to plot
    :return: None
    """
    fig, axes = plt.subplots(1, len(cols))
    for i, col in enumerate(cols):
        sea.violinplot(x=col, y='Tree', data=data1, ax=axes[i])
    fig.suptitle(title)
    plt.show()


if __name__ == '__main__':
    # Let's keep the files inside the pre_processed_data
    # So, it works if you run this file in Console. Or from within the 'analysis' folder!
    t = pd.read_csv('../pre_processed_data/Tree_gdp_index_75_gini_index_25_1000000_temp_stats.csv', sep=';')
    # print(t.shape)
    th = t.head(10000)
    th.to_csv('../pre_processed_data/Tree_gdp_index_75_gini_index_25_1000000_temp_stats_10000.csv',
              sep=';', index=False)
    c = pd.read_csv('../pre_processed_data/current_gdp_index_75_gini_index_25_1000000_temp_stats.csv', sep=';')
    c.rename(columns={'0': 'Tree'}, inplace=True)
    plot_iqrs(th, 'title', ['POLICIES_buy', 'POLICIES_rent', 'POLICIES_wage', 'POLICIES_no_policy'])
