import os
import pandas as pd


if __name__ == '__main__':
    os.getcwd()
    c1 = pd.read_csv('../pre_processed_data/comparison_analysis_gdp_index_75_gini_index_25_1000000_temp_stats.csv',
                     sep=';')
    c1.rename(columns={'Unnamed: 0': 'params'}, inplace=True)

