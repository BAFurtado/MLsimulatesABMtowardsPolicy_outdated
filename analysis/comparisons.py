import pandas as pd

import groups_cols
import plot_iqrs


def plotting(data):
    for each in data:
        for key in groups_cols.abm_dummies:
            plot_iqrs.plot_iqrs(data[each], f'{each}_{key}', groups_cols.abm_dummies[key])


if __name__ == '__main__':
    th = pd.read_csv('../pre_processed_data/Tree_gdp_index_75_gini_index_25_1000000_temp_stats_10000.csv', sep=';')
    c = pd.read_csv('../pre_processed_data/current_gdp_index_75_gini_index_25_1000000_temp_stats.csv', sep=';')
    c.rename(columns={'0': 'Tree'}, inplace=True)
    d = {'ABM simulation': c,
         'Automated ML': th}
    plotting(d)

