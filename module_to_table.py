import pandas as pd

import parameters_restriction as pm

idx = sorted([name.capitalize() for name in vars(pm) if '__' not in name])
idx = [i.replace('_', ' ') for i in idx]

table = pd.DataFrame(columns=['min', 'max', 'distribution'], index=idx)
for name, values in vars(pm).items():
    if '__' not in name:
        name = name.capitalize()
        name = name.replace('_', ' ')
        table.loc[name] = values

table.to_csv('output/table_min_max.csv', sep=';')
