import operator
import sys

import pandas as pd
import numpy as np
from numpy import set_printoptions
from sklearn.model_selection import train_test_split

import choosing_targets
import descriptive_stats
import generating_random_conf
import machines
import preparing_data

set_printoptions(precision=4)

TEST_SIZE = .25


def get_data(path, datafile_name, col1, col2):
    try:
        x, y = preparing_data.read_xy(datafile_name)
        print('Loaded!')
    except FileNotFoundError:
        x, y = preparing_data.main(path, datafile_name)
    target = choosing_targets.getting_target(y, col1, col2)
    target = np.ravel(target)
    return x, target


def check_minimum_presence_parameter(x, y):
    temp_x, x_test, temp_y, temp_y_test = train_test_split(x, y, test_size=TEST_SIZE, random_state=10)
    for col in x_test.columns:
        std = np.std(x_test[col], ddof=1)
        mu = np.mean(x_test[col])
        if mu == 0 or mu is np.nan:
            cv = 0
        else:
            cv = std / mu * 100
        if cv < 5:
            print(f'Dropping {col} from X table...')
            x.drop(col, inplace=True, axis=1)
    return x, y


def main(path, datafile_name, col1, col2):
    x, y = get_data(path, datafile_name, col1, col2)
    x, y = check_minimum_presence_parameter(x, y)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=TEST_SIZE, random_state=10)
    # Running model
    models = machines.run_classifiers(x_train, x_test, y_train, y_test)

    # # Generating random configuration data to test against optimal results
    r = generating_random_conf.compound(x_train)
    print('Generated expanded configuration dataset')
    #
    # # Predicting results using machine on generated set of random parameters
    results = dict()
    for key in models.keys():
        yr = machines.predict(models[key], r[x.columns.tolist()])
        print('Sum of ones {}: {}'.format(key, yr.sum()))
        yr = pd.DataFrame({key: yr.tolist()})
        results[key] = [r, yr]
    #
    # # Output basic descriptive stats
    # # Sending over X and Y as lists in a dictionary for current and each model
    current = {'current': [pd.concat([x_train, x_test], axis=0).reset_index(),
                           pd.concat([y_train, y_test], axis=0, ignore_index=True).to_frame('current')]}
    print('Sum of ones: {}'.format(current['current'][1].sum()))
    current.update(results)
    descriptive_stats.print_conf_stats(current, path)
    return models, x_train, x_test


if __name__ == "__main__":
    p = r'\\storage1\carga\MODELO DINAMICO DE SIMULACAO\Exits_python\PS2020'
    # f'temp_' + {stats', 'firms', 'banks', 'construction' and 'regional'} are always saved
    output_datafile_name = 'temp_stats'
    target1 = 'gdp_index', 65, operator.gt
    target2 = 'gini_index', 35, operator.lt
    ms, xl, xs = main(p, output_datafile_name, target1, target2)
