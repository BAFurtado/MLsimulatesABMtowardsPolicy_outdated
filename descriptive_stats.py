import pandas as pd
import numpy as np
pd.options.display.float_format = '{:,.2f}'.format


def print_conf_stats(kwargs, name):
    # Dict contains X and Y as lists in a dictionary for current and each model
    df = pd.DataFrame()
    for key in kwargs.keys():
        kwargs[key][0].to_csv(f'output/{key}_{name}_0.csv', sep=';', index=False)
        kwargs[key][1].to_csv(f'output/{key}_{name}_1.csv', sep=';', index=False)
        try:
            temp1 = pd.DataFrame(index=np.arange(0, len(kwargs[key][0])),
                                 columns=[kwargs[key][0].columns + [f'{key}_optimal']])
            n_cols = kwargs[key][0].shape[1]
            temp1.iloc[:, 0: n_cols] = kwargs[key][0]
            temp1.iloc[:, n_cols: n_cols + 1] = kwargs[key][1]
            # temp1 = pd.concat([kwargs[key][0], kwargs[key][1]], axis=1)
            # temp1.rename(columns={temp1.columns[-1]: f'{key}_optimal'}, inplace=True)
            temp1.to_csv(f'output/{key}_{name}.csv', sep=';', index=False)
            # temp2 = kwargs[key][0].mean(axis=0)
            # # Averaging by results 1, 0 for each model.
            # temp3 = temp1.groupby([key]).agg('mean')
            # if len(temp3) != 2:
            #     continue
            # res = pd.concat([temp2, temp3.T], axis=1)
            # res.columns = ['tot_' + key, key + '_0', key + '_1']
            # df = pd.concat([df, res], axis=1)
        except MemoryError:
            continue
    # df.to_csv(f'pre_processed_data/comparison_analysis_{name}.csv', sep=';', index=False, float_format='%.6f')


if __name__ == '__main__':
    import os
    import pickle

    n = 'gdp_index_75_gini_index_25_1000000_temp_stats'
    if os.path.exists(n):
        with open(f'{n}', 'rb') as f:
            current = pickle.load(f)
            print_conf_stats(current, n)


