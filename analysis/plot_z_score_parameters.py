import pandas as pd
import matplotlib.pyplot as plt
from pylab import Circle
import groups_cols

colors = ['tab:blue', 'tab:red']


def plotting(data, col1='z_simulated_optimal', col2='z_ml_optimal', name='name'):
    lbsl = [groups_cols.abm_params_show[l] for l in data.index.tolist()]
    fig, ax = plt.subplots(figsize=(8, 6))
    for par in data.index:
        plt.hlines(par,
                   xmin=min(min(d[col1]), min(d[col2])),
                   xmax=max(max(d[col1]), max(d[col2])),
                   colors='lightgrey', lw=.8, alpha=.5)
        ax.plot([data.loc[par, col1], data.loc[par, col2]], [par, par],
                color=colors[0] if data.loc[par, col1] > data.loc[par, col2]
                else colors[1], lw=1, alpha=.8)
        for i, each in enumerate([col1, col2]):
            ax.scatter(data.loc[par, each], par, color=colors[i], alpha=.9, marker='o')

    plt.yticks(range(len(lbsl)), lbsl, fontsize=10)

    pts = Circle((0, 0))
    ax.legend([pts, pts], ['ABM Simulated optimal', 'ML surrogate optimal'], edgecolor='white', facecolor='white',
              framealpha=1, loc='best')
    plt.ylabel("Model parameters")
    plt.xlabel(f"Z score of optimal results")
    leg = ax.get_legend()
    for i in range(len(colors)):
        # leg.legendHandles[i].set_marker('o')
        leg.legendHandles[i].set_color(colors[i])
    plt.tight_layout()
    plt.savefig(f'parameters.png', dpi=300)
    plt.show()


if __name__ == '__main__':
    # d = pd.read_csv('../pre_processed_data/parameters_comparison.csv', sep=';')
    d = pd.read_csv('../pre_processed_data/parameters_SIM_optimal_v_ML_optimal.csv', sep=';')
    d.rename(columns={'Unnamed: 0': 'parameters'}, inplace=True)
    d = d.set_index('parameters')
    d = d.sort_values(by='difference_optimals')
    plotting(d)

