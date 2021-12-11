import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea


def plot_iqrs(data1, title, cols, data2 = None):
    # produces a violin plot with seaborn. data1 and data2 are two different pandas dataframes and cols is a list with the names of each column within both data that one wishes to produce the figure about. Title is a string with the name to be used
    # TODO GOA 10/12/21: I've put data2 as a None argument since the plot is putting one figure on top of each other, needs to be discussed
    fig, axes = plt.subplots(1, len(cols))
    for i, col in enumerate(cols):
        sea.violinplot(x=col, y='Tree', data=data1, ax=axes[i])
        sea.violinplot(x=col, y='Tree', data=data2, ax=axes[i]) if data2 != None else None
    fig.suptitle(title)
    plt.show()


if __name__ == '__main__':
    t = pd.read_csv('../../Tree_gdp_index_75_gini_index_25_1000000_temp_stats.csv', sep=';')
    print(t.shape)
    th = t.head(10000)
    c = pd.read_csv('../../current_gdp_index_75_gini_index_25_1000000_temp_stats.csv', sep=';')
    c.rename(columns={'0': 'Tree'}, inplace=True)
    plot_iqrs(th, 'title', ['POLICIES_buy', 'POLICIES_rent', 'POLICIES_wage', 'POLICIES_no_policy'])
