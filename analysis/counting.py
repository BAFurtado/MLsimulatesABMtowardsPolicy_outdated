import pandas as pd

from groups_cols import abm_dummies as dummies
from groups_cols import abm_params as params


# Replicating excel results for dummies
def getting_counting(data, name):
    table = pd.DataFrame(columns=['size', 'optimal', 'non-optimal'])
    for key in dummies:
        for each in dummies[key]:
            sample_size = len(data[data[each] == 1])/len(data)
            optimal = len(data[(data[each] == 1) & (data['Tree'] == 1)])
            non_optimal = len(data[(data[each] == 1) & (data['Tree'] == 0)])
            total = optimal + non_optimal
            print(f'{each}: size {sample_size:.04f}: optimal {optimal/total:.04f}: '
                  f'non-optimal {non_optimal/total:.04f}')
            table.loc[each, 'size'] = sample_size
            table.loc[each, 'optimal'] = optimal/total
            table.loc[each, 'non-optimal'] = non_optimal/total
    table.to_csv(f'../pre_processed_data/counting_{name}.csv', sep=';')


# Parameters analysis
def coefficient_variation_comparison(simulated, ml):
    table = pd.DataFrame(columns=['simulated_optimal', 'ml_optimal'])
    for param in params:
        sim_mean = simulated[param].mean()
        sim_optimal_mean = simulated[simulated['Tree'] == 1][param].mean()
        ml_mean = ml[param].mean()
        ml_optimal_mean = ml[ml['Tree'] == 1][param].mean()
        print(f'{param}: {(sim_optimal_mean - sim_mean) / sim_mean:.06f}')
        print(f'{param}: {(ml_optimal_mean - ml_mean) / ml_mean:.06f}')
        table.loc[param, 'simulated_optimal'] = (sim_optimal_mean - sim_mean) / sim_mean
        table.loc[param, 'ml_optimal'] = (ml_optimal_mean - ml_mean) / ml_mean
    table.to_csv(f'../pre_processed_data/parameters_comparison.csv', sep=';')


if __name__ == '__main__':
    # th = pd.read_csv('../pre_processed_data/Tree_gdp_index_75_gini_index_25_1000000_temp_stats_10000.csv', sep=';')
    th = pd.read_csv('../pre_processed_data/Tree_gdp_index_75_gini_index_25_1000000_temp_stats.csv', sep=';')
    c = pd.read_csv('../pre_processed_data/current_gdp_index_75_gini_index_25_1000000_temp_stats.csv', sep=';')
    c.rename(columns={'0': 'Tree'}, inplace=True)
    getting_counting(th, 'Tree')
    getting_counting(c, 'Current')
    coefficient_variation_comparison(c, th)

