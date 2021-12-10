import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea


def plot_iqrs(data1, data2, cols):
    fig, axes = plt.subplots(1, len(cols))
    for i, col in enumerate(cols):
        sea.violinplot(x=col, y='Tree', data=data1, ax=axes[i])
        sea.violinplot(x=col, y='Tree', data=data2, ax=axes[i])
    plt.show()


if __name__ == '__main__':
    t = pd.read_csv('Tree_gdp_index_75_gini_index_25_1000000_temp_stats.csv', sep=';')
    print(t.shape)
    th = t.head(10000)
    c = pd.read_csv('current_gdp_index_75_gini_index_25_1000000_temp_stats.csv', sep=';')
    c.rename(columns={'0': 'Tree'}, inplace=True)
    plot_iqrs(th, c, ['POLICIES_buy', 'POLICIES_rent', 'POLICIES_wage', 'POLICIES_no_policy'])
