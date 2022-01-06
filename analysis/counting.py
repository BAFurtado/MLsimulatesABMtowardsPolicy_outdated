import pandas as pd

from groups_cols import abm_dummies as dummies


# Replicating excel results
def getting_counting(data, name):
    for key in dummies:
        for each in dummies[key]:
            sample_size = len(data[data[each] == 1])/len(data)
            optimal = len(data[(data[each] == 1) & (data['Tree'] == 1)])
            non_optimal = len(data[(data[each] == 1) & (data['Tree'] == 0)])
            total = optimal + non_optimal
            print(f'{each}: size {sample_size:.04f}: optimal {optimal/total:.04f}: '
                  f'non-optimal {non_optimal/total:.04f}')


if __name__ == '__main__':
    th = pd.read_csv('../pre_processed_data/Tree_gdp_index_75_gini_index_25_1000000_temp_stats_10000.csv', sep=';')
    c = pd.read_csv('../pre_processed_data/current_gdp_index_75_gini_index_25_1000000_temp_stats.csv', sep=';')
    c.rename(columns={'0': 'Tree'}, inplace=True)
    getting_counting(th, 'Tree')

