import os
import pandas as pd
import numpy as np
import groups_cols

# 1. Read tables
# 2. Identify process of comparison (criteria to make a decision)
# 3. Output automatic results -- plot (box-plot/distributions)
# Analysis of:
# 4. Cidades
# 5. Policy
# 6. Parameters in general


# TO DO do texto
# DONE # 1. Finish general model figure
# 2. Finish analysis
# 3. Write text
# 4. Include other analysis, plots, robustness...

if __name__ == '__main__':
    os.getcwd()
    """ First attempt, just reading the comparison

    c1 = pd.read_csv('../pre_processed_data/comparison_analysis_gdp_index_75_gini_index_25_1000000_temp_stats.csv',
                     sep=';')
    c1.rename(columns={'Unnamed: 0': 'params'}, inplace=True)"""

    # GOA 7/12/21: trying to combine the csv's at the analysis folder

    """csv1 = pd.read_csv('current_gdp_index_75_gini_index_25_1000000_temp_stats_0.csv',
                     sep=';') # this one is 11076 rows x 86 columns"""

    """csv2 = pd.read_csv('current_gdp_index_75_gini_index_25_1000000_temp_stats_1.csv',
                     sep=';') # this one is 11076 rows x 1 column"""

    # we have to concatenate horizontally

    # GOA 8/12/21: actual table to work with arrived

    csv = pd.read_csv('../../Tree_gdp_index_75_gini_index_25_1000000_temp_stats.csv',
                      sep=';')  # this is the actual table that we have to work with, 999935 rows by 81 columns
    # important note: each ../ serves for one step of going up
    # why were the previous two tables tiny in relation to this one?

    # all columns are pretty much already explained, but the Tree column means optimal: 0 is non-optimal and 1 is optimal

    # script: we have to separate and aggregate, per characteristic and specially by ACP --> for each one we have to get median, q3, q1

    df = pd.DataFrame()

    acps = ['all'] + groups_cols.abm_dummies['acps']

    for ACP in acps:

        if ACP == 'all':
            plot_df = csv
        else:
            plot_df = csv.loc[csv[ACP] == 1]

        for pol in groups_cols.abm_dummies['policies']:

            if ACP == 'all' and pol == 'any':
                rslt_df = csv.loc[csv['POLICIES_no_policy'] == 0]
                plot_df = csv.loc[csv['POLICIES_no_policy'] == 0]
            elif ACP == 'all' and pol != 'any':
                rslt_df = csv.loc[csv[pol] == 1]
            elif ACP != 'all' and pol == 'any':
                rslt_df = csv.loc[(csv[ACP] == 1) & (csv['POLICIES_no_policy'] == 0)]
            else:
                rslt_df = csv.loc[(csv[ACP] == 1) & csv[pol] == 1]

            q3, q1 = np.percentile(rslt_df['Tree'], [75, 25])
            median, mean, count, std = rslt_df['Tree'].median(), rslt_df['Tree'].mean(), rslt_df[
                'Tree'].count(), np.std(rslt_df['Tree'])

            df = df.append(
                {'ACP': ACP,
                 'pol': pol,
                 'q3': q3,
                 'q1': q1,
                 'median': median,
                 'IQR': q3 - q1,
                 'mean': mean,
                 'std': std,
                 'count': count}, ignore_index=True)

    df.to_csv('IQR.csv', sep=';')

    # with that we have a csv (on this folder) with the combined information per ACP.
    # TODO p-value (yet to find a less cumbersome method)
