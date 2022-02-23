import pandas as pd
import groups_cols
from groups_cols import abm_dummies as dummies
from groups_cols import abm_params as params
import scipy.stats
import numpy as np
import math


# Replicating excel results for dummies
def getting_counting(data, name):
    """ Produces a csv with information regarding each dummy, i.e., when the dummy is active (=1).
    In the final csv we have three columns: sample size, optimal and non-optimal.
    All columns are in percentage of the total: sample size in relation to the whole sample, and optimal and
    non-optimal in relation to the sample of that specific dummy.

    For example, policies_buy has a sample size of 0.12 meaning that 12% of the sample had that dummy as true, an
    optimal of 2% and a non-optimal of 97%, meaning that, when that dummy is active and policy used is buy, 97% of the
    samples fall under the non-optimal category.

    :param data: base csv
    :param name: name of the file
    :return: returns nothing, but saves the csv
    """
    table = pd.DataFrame(columns=['size', 'optimal', 'non_optimal', 'optimal_count', 'non_optimal_count'])
    for key in dummies:
        for each in dummies[key]:
            sample_size = len(data[data[each] == 1]) / len(data)
            optimal = len(data[(data[each] == 1) & (data['Tree'] == 1)])
            non_optimal = len(data[(data[each] == 1) & (data['Tree'] == 0)])
            total = optimal + non_optimal
            print(f'{each}: size {sample_size:.04f}: optimal {optimal / total:.0f}: '
                  f'non-optimal {non_optimal / total:.04f}: optimal_count {optimal} non-optimal_count {non_optimal}')
            table.loc[each, 'size'] = sample_size
            table.loc[each, 'optimal'] = optimal / total
            table.loc[each, 'non_optimal'] = non_optimal / total
            table.loc[each, 'optimal_count'] = optimal
            table.loc[each, 'non_optimal_count'] = non_optimal
    table.to_csv(f'../pre_processed_data/counting_{name}.csv', sep=';')


# Parameters analysis
def coefficient_variation_comparison(simulated, ml):
    """ This function compares the ABM simulated results to the ML surrogate results in order to identify the
    differences between the two methods. How much of the cases fall under the optimal in relation to the mean?
    Added the column difference

    Using standard-score: (optimal value mean - full sample mean) / full sample standard-deviation

    Added absolute optimal value for simulated and ML

    :param simulated: the simulated database in csv
    :param ml: the ML surrogate database in csv
    :return: returns nothing, but saves the csv
    """
    table = pd.DataFrame(columns=['simulated_optimal', 'ml_optimal', 'difference'])
    for param in params:
        sim_mean = simulated[param].mean()
        sim_std = simulated[param].std()
        sim_optimal_mean = simulated[simulated['Tree'] == 1][param].mean()
        ml_mean = ml[param].mean()
        ml_std = ml[param].std()
        ml_optimal_mean = ml[ml['Tree'] == 1][param].mean()
        print(f'{param}: {(sim_optimal_mean - sim_mean) / sim_std:.06f}')
        print(f'{param}: {(ml_optimal_mean - ml_mean) / ml_std:.06f}')
        table.loc[param, 'simulated_optimal'] = (sim_optimal_mean - sim_mean) / sim_std
        table.loc[param, 'ml_optimal'] = (ml_optimal_mean - ml_mean) / ml_std
        table.loc[param, 'difference'] = table.loc[param, 'simulated_optimal'] - table.loc[param, 'ml_optimal']
        table.loc[param, 'abs_sim_optimal'] = sim_optimal_mean
        table.loc[param, 'abs_ml_optimal'] = ml_optimal_mean
    table.to_csv(f'../pre_processed_data/parameters_comparison.csv', sep=';')
    table.reset_index(inplace=True)
    table['Parameters'] = table['index'].map(groups_cols.abm_params_show)
    to_latex = table[['Parameters', 'abs_sim_optimal', 'abs_ml_optimal']]
    to_latex = to_latex.sort_values(by='Parameters')
    to_latex.set_index('Parameters', inplace=True)
    to_latex.to_latex('../pre_processed_data/parameters_comparison_latex.txt',
                      float_format="{:0.3f}".format)


# Parameters analysis
def normalize_and_optimal(simulated, ml, name, first_variable, second_variable,
                          p_value_threshold=0.05):
    """ With this we have the mean of the ML optimal against the mean of the simulated optimal. It might be adequate for
    determining if the ML is different from the simulation, nevertheless, it would be good for the analysis itself to
    put the mean against the ML optimal mean in order to reject or not the null hypothesis that the parameter matters
    for the municipalities or not.

    z-score = estatística de teste - média observada / desvio padrão/ raiz do número de observações (Gujarati, p. 832)
     <- Internet does not use the square root of observations

    :param second_variable: second variable (standard error draws from this one)
    :param first_variable: first variable to be analyzed (non-optimal, optimal or mean for simulated or surrogate)
    :param name: output name for the csv
    :param p_value_threshold: p-value threshold for the z-test (0.05 by default)
    :param simulated: dataframe, simulated cases
    :param ml: dataframe, Machine-learning cases
    :return: produces a latex table and a csv file
    """
    table = pd.DataFrame(columns=['z_simulated_optimal', 'z_ml_optimal', 'z_simulated_non_optimal', 'z_ml_non_optimal',
                                  'difference_optimals', 'difference', 'p_value', 'reject_null_hypothesis'])
    for param in params:
        # normalize
        simulated.loc[:, f'n_{param}'] = (simulated[param] - simulated[param].min()) / \
                                         (simulated[param].max() - simulated[param].min())
        ml.loc[:, f'n_{param}'] = (ml[param] - ml[param].min()) / (ml[param].max() - ml[param].min())
        sim_optimal_mean = simulated[simulated['Tree'] == 1][f'n_{param}'].mean()
        sim_non_optimal_mean = simulated[simulated['Tree'] == 0][f'n_{param}'].mean()
        ml_optimal_mean = ml[ml['Tree'] == 1][f'n_{param}'].mean()
        ml_optimal_std = np.std(ml[ml['Tree'] == 1][f'n_{param}'])
        ml_non_optimal_mean = ml[ml['Tree'] == 0][f'n_{param}'].mean()
        ml_mean = ml[f'n_{param}'].mean()
        ml_std = np.std(ml[f'n_{param}'])
        ml_non_optimal_std = np.std(ml[ml['Tree'] == 0][f'n_{param}'])
        sim_mean = simulated[f'n_{param}'].mean()
        sim_std = np.std(simulated[f'n_{param}'])
        sim_optimal_std = np.std(simulated[simulated['Tree'] == 1][f'n_{param}'])
        sim_non_optimal_std = np.std(simulated[simulated['Tree'] == 0][f'n_{param}'])
        # print(f'{param}: {sim_optimal_mean:.06f}')
        # print(f'{param}: {ml_optimal_mean:.06f}')
        table.loc[param, 'z_simulated_optimal'] = (sim_optimal_mean - sim_mean) / sim_std
        table.loc[param, 'z_ml_optimal'] = (ml_optimal_mean - ml_mean) / ml_std
        table.loc[param, 'z_simulated_non_optimal'] = (sim_non_optimal_mean - sim_mean) / sim_std
        table.loc[param, 'z_ml_non_optimal'] = (ml_non_optimal_mean - ml_mean) / ml_std
        table.loc[param, 'difference_optimals'] = (table.loc[param, 'z_simulated_optimal'] -
                                                   table.loc[param, 'z_ml_optimal'])

        variable_dict = {"sim_optimal_mean": sim_optimal_mean,
                         "sim_non_optimal_mean": sim_non_optimal_mean,
                         "ml_optimal_mean": ml_optimal_mean,
                         "ml_mean": ml_mean,
                         "ml_non_optimal_mean": ml_non_optimal_mean,
                         "sim_mean": sim_mean}

        std_dict = {"sim_optimal_mean": sim_optimal_std,
                    "sim_non_optimal_mean": sim_non_optimal_std,
                    "ml_optimal_mean": ml_optimal_std,
                    'ml_mean': ml_std,
                    "ml_non_optimal_mean": ml_non_optimal_std,
                    "sim_mean": sim_std}

        if std_dict[second_variable] > 0:
            difference = (variable_dict[first_variable] - variable_dict[second_variable] / std_dict[second_variable])
        else:
            difference = 'STD=0'

        table.loc[param, 'difference'] = difference

        if difference != 'STD=0':
            table.loc[param, 'p_value'] = scipy.stats.norm.sf(abs(table.loc[param, 'difference'])) * 2
            table.loc[param, 'reject_null_hypothesis'] = 'yes' if table.loc[
                                                                      param, 'p_value'] < p_value_threshold else 'no'
        else:
            table.loc[param, 'p_value'] = 'not_applicable'
            table.loc[param, 'reject_null_hypothesis'] = 'not_applicable'
        # print(table.loc[param,'p_value'])
    table.to_csv(f'../pre_processed_data/{name}.csv', sep=';')
    table.reset_index(inplace=True)
    table['Parameters'] = table['index'].map(groups_cols.abm_params_show)
    to_latex = table[['Parameters', 'z_simulated_optimal', 'z_ml_optimal']]
    to_latex = to_latex.sort_values(by='Parameters')
    to_latex.set_index('Parameters', inplace=True)
    to_latex.to_latex(f'../pre_processed_data/{name}.txt',
                      float_format="{:0.3f}".format)


if __name__ == '__main__':
    # th = pd.read_csv('../pre_processed_data/Tree_gdp_index_75_gini_index_25_1000000_temp_stats_10000.csv', sep=';')
    th = pd.read_csv('../pre_processed_data/Tree_gdp_index_75_gini_index_25_1000000_temp_stats.csv', sep=';')
    c = pd.read_csv('../pre_processed_data/current_gdp_index_75_gini_index_25_1000000_temp_stats.csv', sep=';')
    c.rename(columns={'0': 'Tree'}, inplace=True)
    # getting_counting(th, 'Tree')
    # getting_counting(c, 'Current')
    # coefficient_variation_comparison(c, th)

    """ Variables : "sim_optimal_mean",
        "sim_non_optimal_mean",
        "ml_optimal_mean",
        "ml_mean,
        "ml_non_optimal_mean",
        "sim_mean"""

    # second variable is the population mean, so it should at least be the one with more observations

    #New name of the dataframes: parameters_first_variable_v_second_variable

    normalize_and_optimal(c, th, 'parameters_SIM_non_optimal_v_SIM_optimal',
                          "sim_optimal_mean", "sim_non_optimal_mean")
    normalize_and_optimal(c, th, 'parameters_SIM_optimal_v_SIM',
                          "sim_optimal_mean", "sim_mean")
    normalize_and_optimal(c, th, 'parameters_SIM_non_optimal_v_SIM',
                          "sim_non_optimal_mean", "sim_mean")
    normalize_and_optimal(c, th, 'parameters_SIM_optimal_v_ML_optimal',
                          "sim_optimal_mean", "ml_optimal_mean")
    normalize_and_optimal(c, th, 'parameters_SIM_optimal_v_ML',
                          "sim_optimal_mean", "ml_mean")
    normalize_and_optimal(c, th, 'parameters_SIM_v_ML_optimal',
                          "sim_mean", "ml_optimal_mean")
    normalize_and_optimal(c, th, 'parameters_SIM_v_ML_non_optimal',
                          "sim_mean", "ml_non_optimal_mean")
    normalize_and_optimal(c, th, 'parameters_SIM_v_ML',
                          "sim_mean", "ml_mean")
    normalize_and_optimal(c, th, 'parameters_ML_optimal_v_ML_non_optimal',
                          "ml_optimal_mean", "ml_optimal_mean")
    normalize_and_optimal(c, th, 'parameters_ML_optimal_v_ML',
                          "ml_optimal_mean", "ml_mean")
    normalize_and_optimal(c, th, 'parameters_SIM_non_optimal_v_ML_non_optimal',
                          "sim_non_optimal_mean", "ml_non_optimal_mean")  # this one is the best for comparison


    """
    Dummies
    """

    # TBD: dummies use a different type of z-score
