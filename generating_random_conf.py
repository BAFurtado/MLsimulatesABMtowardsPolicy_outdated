import numpy.random
import pandas as pd

import parameters_restriction as params
import preparing_data

numpy.random.seed(0)


def to_dict_from_module():
    return {k: getattr(params, k) for k in dir(params) if not k.startswith('_')}


def pre_process(data):
    return data.describe().T[['mean', 'std']]


def handling_choices_keys(param):
    n_param = dict()
    for p in param:
        if param[p]['distribution'] == 'choice':
            for a in param[p]['alternatives']:
                # Adding transformed key to original parameters dictionary
                n_param[f"{p}_{a}"] = {'alternatives': [True, False], 'distribution': 'choice'}
        else:
            n_param[p] = param[p]
    return n_param


def compound(x, n=10000):
    param = to_dict_from_module()
    samples = pre_process(x)
    param = handling_choices_keys(param)
    data = dict()
    # Either choice or normal
    for p in param:
        if p in samples.index:
            if param[p]['distribution'] == 'normal':
                data[p] = numpy.random.normal(samples.loc[p, 'mean'], samples.loc[p, 'std'] * 2, n)
    data['PROCESSING_ACPS'] = numpy.random.choice(d_acps, n)
    for each in d_bool:
        data[each] = numpy.random.choice(['True', 'False'], n)
    df = pd.DataFrame(data)
    temp1 = df[d_bool + ['PROCESSING_ACPS']]
    temp2 = df[df.columns.difference(d_bool + ['PROCESSING_ACPS'])]
    temp2 = temp2.fillna(0)
    for col in temp2.columns:
        temp2[col] = temp2[col].apply(lambda x: temp2[col].mean() if x < 0 else x)
    return preparing_data.dummies(pd.concat([temp1, temp2], axis=1))


if __name__ == '__main__':
    path = r'\\storage4\carga\MODELO DINAMICO DE SIMULACAO\Exits_python\JULY'
    file_name = 'pre_processed_data\\' + path[-4:] + '_x.csv'
    d = compound(file_name)
    print(d.head())
