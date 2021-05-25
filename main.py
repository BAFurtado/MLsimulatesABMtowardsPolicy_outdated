import operator
import sys

import pandas as pd
from numpy import set_printoptions
from sklearn.model_selection import train_test_split

import choosing_targets
import descriptive_stats
import generating_random_conf
import machines
import preparing_data

set_printoptions(precision=4)


def get_data(pathways, datafile_name, col1, col2):
    try:
        x, y = preparing_data.read_xy()
        print('Loaded!')
    except FileNotFoundError:
        x, y = preparing_data.main(pathways, datafile_name)
    target = choosing_targets.getting_target(y, col1, col2)
    return train_test_split(x, target, test_size=0.3, random_state=10)


def main(pathways, datafile_name, col1, col2):
    x, xt, y, yt = get_data(pathways, datafile_name, col1, col2)
    # Running model
    models = machines.run_classifiers(x, xt, y, yt)

    # Generating random configuration data to test against optimal results
    r = generating_random_conf.compound(name)
    print('Generated dataset summary')

    # Predicting results using machine on generated set of random parameters
    results = dict()
    for key in models.keys():
        yr = machines.predict(models[key], r[x.columns.tolist()])
        print('Sum of ones {}: {}'.format(key, yr.sum()))
        yr = pd.DataFrame({key: yr.tolist()})
        results[key] = [r, yr]

    # Output basic descriptive stats
    # Sending over X and Y as lists in a dictionary for current and each model
    current = {'current': [pd.concat([x, xt], axis=0).reset_index(),
                         pd.concat([y, yt], axis=0, ignore_index=True).to_frame('current')]}
    print('Sum of ones: {}'.format(current['current'][1].sum()))
    current.update(results)
    descriptive_stats.print_conf_stats(current, name)


if __name__ == "__main__":
    p = r'\\storage1\carga\MODELO DINAMICO DE SIMULACAO\Exits_python\PS2020'
    # f'temp_' + {stats', 'firms', 'banks', 'construction' and 'regional'} are always saved
    output_data_file_name = 'temp_stats'
    target1 = 'gdp_index', 65, operator.gt
    target2 = 'gini_index', 35, operator.lt
    main(p, output_data_file_name, target1, target2)

    file_name = 'pre_processed_data\\' + path[-4:] + '_' + target1 + '_' + target2 + '_x.csv'

    with open('outputs\\scores' + '_' + target1 + '_' + target2 + '.txt', 'w') as f:
        sys.stdout = f
        x_train, x_test, y_train, y_test = get_data(path, target1, target2, file_name)
        main(x_train, x_test, y_train, y_test, file_name)