import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import groups_cols

tables = dict()
iqr = pd.read_csv('IQR.csv', sep=';')
# iqr = iqr.set_index('ACP')

# tree = pd.read_csv('../pre_processed_data/Tree_gdp_index_75_gini_index_25_1000000_temp_stats.csv', sep=';')

mean_policy_acp = pd.DataFrame(columns=[['MR', 'No policy', 'Buy', 'Rent', 'Wage']])
std_policy_acp = mean_policy_acp.copy()
acps = ['all'] + groups_cols.abm_dummies['acps']

for acp in acps:
    row_mean = [acp]
    row_std = row_mean.copy()
    for policy in ['POLICIES_no_policy', 'POLICIES_buy', 'POLICIES_rent', 'POLICIES_wage']:
        dataframe_mean = iqr.loc[(iqr['ACP'] == acp) & (iqr['pol'] == policy)]['mean'].values[0]
        dataframe_std = iqr.loc[(iqr['ACP'] == acp) & (iqr['pol'] == policy)]['std'].values[0]
        if policy == 'POLICIES_no_policy':
            mean = dataframe_mean * 100
            std = dataframe_std * 100
        else:
            mean = (dataframe_mean * 100 - row_mean[1])
            std = (dataframe_std * 100 - row_std[1])
        row_mean.append(mean)
        row_std.append(std)
    mean_policy_acp.at[acp] = row_mean
    std_policy_acp.at[acp] = row_std

for df in [mean_policy_acp, std_policy_acp]:
    df.reset_index(drop=True, inplace=True)
    df.sort_values(ascending=False, by=('No policy',), inplace=True)
    df.replace({('MR',): groups_cols.abm_dummies_show})

mean_policy_acp = mean_policy_acp.replace({('MR',): groups_cols.abm_dummies_show})
std_policy_acp = std_policy_acp.replace({('MR',): groups_cols.abm_dummies_show})

# No policy is in absolute value (%) and all other columns are in percentage points of difference to the No policy case
# NH-SL: Novo Hamburgo/Sao Leopoldo, SJRP: Sao Jose do Rio Preto, SJC: Sao Jose dos Campos

# Differences in dummies
current = pd.read_csv('../pre_processed_data/counting_Current.csv', sep=';')
current.replace({'Unnamed: 0': groups_cols.abm_dummies_show}, inplace=True)

tree = pd.read_csv('../pre_processed_data/counting_Tree.csv', sep=';')
tree.replace({'Unnamed: 0': groups_cols.abm_dummies_show}, inplace=True)

# Differences in non-acp dummies
SON = pd.DataFrame()
SON_acp = SON.copy()
non_acps = list(range(0, 7)) + list(range(53, 62))

for row in non_acps:
    to_add = {'Dummy': tree.iloc[row, 0],
              'Size: sur': tree.iloc[row, 1] * 100,
              'Size: ABM': current.iloc[row, 1] * 100,
              'Opt: sur': tree.iloc[row, 2] * 100,
              'Opt: ABM': current.iloc[row, 2] * 100,
              'Non-opt: sur': tree.iloc[row, 3] * 100,
              'Non-opt: ABM': current.iloc[row, 3] * 100
              }
    print(to_add)
    SON = SON.append(to_add, ignore_index=True)

SON.sort_values(by='Non-opt: sur', inplace=True)

# differences in acp dummies

for row in range(7, 53):
    to_add = {'Dummy': tree.iloc[row, 0],
              'Size: sur': tree.iloc[row, 1] * 100,
              'Size: ABM': current.iloc[row, 1] * 100,
              'Opt: sur': tree.iloc[row, 2] * 100,
              'Opt: ABM': current.iloc[row, 2] * 100,
              'Non-opt: sur': tree.iloc[row, 3] * 100,
              'Non-opt: ABM': current.iloc[row, 3] * 100
              }
    print(to_add)
    SON_acp = SON_acp.append(to_add, ignore_index=True)

SON_acp.sort_values(by='Non-opt: sur', inplace=True)

# comparison of parameters

comp = pd.read_csv('../pre_processed_data/parameters_comparison.csv', sep=';')
comp.replace({'Unnamed: 0': groups_cols.abm_params_show}, inplace=True)

params = pd.DataFrame()
for row in range(0, len(comp['Unnamed: 0'])):
    to_add = {'Dummy': comp.iloc[row, 0],
              'Surrogate': comp.iloc[row, 1] * 100,
              'ABM': comp.iloc[row, 2] * 100,
              'Difference (p.p.)': comp.iloc[row, 2] * 100 - comp.iloc[row, 1] * 100
              }
    print(to_add)
    params = params.append(to_add, ignore_index=True)

params.sort_values(by='Difference (p.p.)', inplace=True)

tables.update({'mean_policy_acp': mean_policy_acp,
               'std_policy_acp': std_policy_acp,
               "SON": SON,
               "SON_acp": SON_acp,
               "params": params})

for _ in tables:
    table = tables[_]
    print(table.to_latex(index=False))
    name = 'table_csvs/' + _ + '.csv'
    table.to_csv(name, index=False, sep=';')

# # Creating the histogram for the mean and standard deviations per MR
hist_mean = mean_policy_acp.copy()
hist_std = std_policy_acp.copy()

for col in ['Buy', 'Rent', 'Wage']:
    hist_mean[col] = mean_policy_acp.loc[:, ['No policy', col]].sum(axis=1)
    hist_std[col] = std_policy_acp.loc[:, ['No policy', col]].sum(axis=1)

hist_std.sort_values(by=('MR',), inplace=True)
hist_mean.sort_values(by=('MR',), inplace=True)

no_policy, buy, rent, wage = pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
_dict = {'No policy': no_policy,
         'Buy': buy,
         'Rent': rent,
         'Wage': wage}

for acp in range(0, 30):
    for policy in ['No policy', 'Buy', 'Rent', 'Wage']:
        row = {'MR': hist_mean.loc[acp, 'MR'].MR,
               'max': min(100, hist_mean.loc[acp, policy].values[0] + hist_std.loc[acp, policy].values[0]),
               'value': hist_mean.loc[acp, policy].values[0],
               'min': max(0, hist_mean.loc[acp, policy].values[0] - hist_std.loc[acp, policy].values[0])}
        print(row)
        _dict[policy] = _dict[policy].append(row, ignore_index=True)

_dict['Wage'].transpose()

plt.figure(figsize=(8, 8))
plt.ylim((0, 100))
plt.tight_layout()

plt.subplot(4, 1, 1).set_title('No Policy')
_dict['No policy'].set_index('MR').T.boxplot(widths=0.6, labels=None).set(xticklabels=[])

plt.subplot(4, 1, 2).set_title('Policy: Buy')
_dict['Buy'].set_index('MR').T.boxplot(widths=0.6).set(xticklabels=[])

plt.subplot(4, 1, 3).set_title('Policy: Wage')
_dict['Wage'].set_index('MR').T.boxplot(widths=0.6).set(xticklabels=[])

plt.subplot(4, 1, 4).set_title('Policy: Rent')
_dict['Rent'].set_index('MR').T.boxplot(widths=0.6)

plt.xticks(rotation=90)

plt.savefig(f'../text/figures/boxplot.png', bbox_inches='tight', transparent=True)
plt.show()
