import numpy as np
import pandas as pd
import scipy.stats as stats

import parameters_restriction as params

np.random.seed(0)


def to_dict_from_module():
    return {k: getattr(params, k) for k in dir(params) if not k.startswith('_')}


def pre_process(data):
    """
    Function that returns the mean and standard deviation for the data
    :param data: csv to be pre-processed
    :return: dataframe with just mean and stds for each data
    """
    return data.describe().T[['mean', 'std']]


def compound(x, n, omitted_rule=False):
    """
    This function is the main function of this py file. It returns a dataframe with randomly generated parameters (both
    continuous and discrete) for a sample dataset. The parameters follow a normal distribution around the mean and std
    of the sample dataset

    :param x: dataframe with the original data
    :param n: number of
    :param omitted_rule:
    :return:
    """
    # Function will break if n is too small < 1000
    # so that not enough columns will be sampled for PROCESSING_ACPS, for example
    param = to_dict_from_module() #first we get a list of parameters
    samples = pre_process(x)
    df = pd.DataFrame()
    data = dict()
    # Either choice or normal
    for p in param:
        # we have a continuous parameter, with mean and std that are numerical
        if p in samples.index:
            if param[p]['distribution'] == 'normal':
                lower, upper = param[p]['min'], param[p]['max']
                mu, sigma = samples.loc[p, 'mean'], samples.loc[p, 'std'] * 3
                data[p] = stats.truncnorm((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma).rvs(n)
        else:
            # we have a dummy. Dummies do not use the mean and std deviation of the sample <- this may be relevant
            # latter
            choices = [i for i in samples.index if p in i]
            if choices:
                m = len(choices)
                choices_vector = pd.DataFrame(np.random.choice(choices, n, p=[1 / m] * m))
                temp = pd.get_dummies(choices_vector)
                temp.columns = choices
                df = pd.concat([temp, df], axis=1)
    if omitted_rule:
        data['OMITTED_RULE'] = np.random.choice([1, 0], n, p=[.5, .5])
    return pd.concat([df, pd.DataFrame(data)], axis=1)


if __name__ == '__main__':
    path = r'\\storage4\carga\MODELO DINAMICO DE SIMULACAO\Exits_python\JULY'
    file_name = f'pre_processed_data/x_temp_stats.csv' # first we get the csv containing the entries and outputs of
    # the ABM model
    d = compound(pd.read_csv(file_name, sep=';'), 10000) # then we compound them -> go to compound
    print(d.head())
