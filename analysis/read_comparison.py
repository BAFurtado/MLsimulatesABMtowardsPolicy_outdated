import os
import pandas as pd


# 1. Read tables
# 2. Identify process of comparison (criteria to make a decision)
# 3. Output automatic results -- plot (box-plot/distributions)
# Analysis of:
# 4. Cidades
# 5. Policy
# 6. Parameters in general


# TODO do texto
# 1. Finish general model figure
# 2. Finish analysis
# 3. Write text
# 4. Include other analysis, plots, robustness...

if __name__ == '__main__':
    os.getcwd()
    c1 = pd.read_csv('../pre_processed_data/comparison_analysis_gdp_index_75_gini_index_25_1000000_temp_stats.csv',
                     sep=';')
    c1.rename(columns={'Unnamed: 0': 'params'}, inplace=True)

