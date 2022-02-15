import pandas as pd
import matplotlib.pyplot as plt

import groups_cols

colors = ['tab:blue', 'tab:red']


def plotting(data, name='name'):
    # lbsl = [groups_cols.abm_dummies_show[l] for l in data.index.tolist()]
    fig, ax = plt.subplots(figsize=(8, 6))
    for par in data.index:
        for i, each in enumerate(['simulated_optimal', 'ml_optimal']):
            ax.scatter(data.loc[par, each], par, color=colors[i], alpha=.5, marker='o')
    # plt.vlines(x=range(len(lbsl)), ymin=0, ymax=1, colors='lightgrey', lw=.8, alpha=.3)
    # plt.xticks(range(len(lbsl)), lbsl, rotation='vertical', fontsize=7)
    # ax.legend(['Purchase', 'Rent vouchers', 'Monetary aid', 'no-policy baseline'],
    #           edgecolor='white', loc='upper center', facecolor='white', framealpha=1)
    # plt.ylabel("Percentage of Metropolitan Regions' optimal cases per policy")
    # leg = ax.get_legend()
    # # hl_dict = {handle.get_label(): handle for handle in leg.legendHandles}
    #
    # for i in range(len(colors)):
    #     leg.legendHandles[i].set_color(colors[i])
    plt.tight_layout()
    plt.savefig(f'parameters.png', dpi=300)
    plt.show()


if __name__ == '__main__':
    d = pd.read_csv('../pre_processed_data/parameters_comparison.csv', sep=';')
    d.rename(columns={'Unnamed: 0': 'parameters'}, inplace=True)
    d = d.set_index('parameters')
    plotting(d)

