import numpy as np
import pandas as pd

import parameters_restriction as params

np.random.seed(0)


def to_dict_from_module():
    return {k: getattr(params, k) for k in dir(params) if not k.startswith('_')}


def pre_process(data):
    return data.describe().T[['mean', 'std']]


def compound(x, n=10000):
    param = to_dict_from_module()
    samples = pre_process(x)
    data = dict()
    # Either choice or normal
    for p in param:
        if p in samples.index:
            if param[p]['distribution'] == 'normal':
                data[p] = np.random.normal(samples.loc[p, 'mean'], samples.loc[p, 'std'] * 2, n)
        else:
            choices = [i for i in samples.index if p in i]
            if choices:
                m = len(choices)
                data[choices[0]] = np.random.choice([1, 0], n, p=[1/m] * m)
                for j in range(1, m):
                    data[choices[j]] = abs(data[choices[0]] - 1)
        return pd.DataFrame(data)


if __name__ == '__main__':
    path = r'\\storage4\carga\MODELO DINAMICO DE SIMULACAO\Exits_python\JULY'
    file_name = 'pre_processed_data\\' + path[-4:] + '_x.csv'
    d = compound(file_name)
    print(d.head())
