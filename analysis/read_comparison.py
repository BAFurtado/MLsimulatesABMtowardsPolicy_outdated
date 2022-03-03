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

    """
    IMPORTANT: Must check if the path of the csv is right
    """

    csv = pd.read_csv('../../Tree_gdp_index_75_gini_index_25_1000000_temp_stats.csv',
                      sep=';')  # this is the actual table that we have to work with, 999935 rows by 81 columns
    # important note: each ../ serves for one step of going up

    # all columns are pretty much already explained, but the Tree column means optimal:
    # 0 is non-optimal and 1 is optimal

    # script: we have to separate and aggregate, per characteristic and specially by ACP -->
    #   for each one we have to get median, q3, q1

    df = pd.DataFrame()

    acps = ['all'] + groups_cols.abm_dummies['acps']

    for ACP in acps:

        if ACP == 'all':
            plot_df = csv
        else:
            plot_df = csv.loc[csv[ACP] == 1]

        for pol in groups_cols.abm_dummies['policies']:

            if ACP == 'all':
                # if we are dealing with all acps, we just need to locate the rows in which the pol is the one being
                # analyzed
                results_df = csv.loc[csv[pol] == 1]
                optimal_count = csv.loc[(csv[pol] == 1) &
                                        (csv['Tree'] == 1)].count().values[0]
            else:
                results_df = csv.loc[(csv[ACP] == 1) & (csv[pol] == 1)]
                optimal_count = csv.loc[(csv[ACP] == 1) &
                                        (csv[pol] == 1) &
                                        (csv['Tree'] == 1)].count().values[0]

            q3, q1 = np.percentile(results_df['Tree'], [75, 25])
            median, mean, count, std = results_df['Tree'].median(), results_df['Tree'].mean(), results_df[
                'Tree'].count(), np.std(results_df['Tree'])



            # since the mean is a mean of 0's and 1's, multiplying it by the count itself provides us with

            df = df.append(
                {'ACP': ACP,
                 'pol': pol,
                 'q3': q3,
                 'q1': q1,
                 'median': median,
                 'IQR': q3 - q1,
                 'mean': mean,
                 'std': std,
                 'count': count,
                 'optimal_count': optimal_count},
                ignore_index=True)

    df.to_csv('IQR.csv', sep=';')
