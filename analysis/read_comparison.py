
import numpy as np
import pandas as pd

import groups_cols

# 1. Read tables
# 2. Identify process of comparison (criteria to make a decision)
# 3. Output automatic results -- plot (box-plot/distributions)
# Analysis of:
# 4. Cidades
# 5. Policy
# 6. Parameters in general


if __name__ == '__main__':

    csv = pd.read_csv('../pre_processed_data/Tree_gdp_index_75_gini_index_25_1000000_temp_stats.csv', sep=';')

    # All columns are pretty much already explained, but the Tree column means optimal
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
