""" Prepare the simulation data for Machine Learning procedures 
"""

import json
import operator
import os

import numpy as np
import pandas as pd

import cols_specification as cols


def read_conf_results_files(general_path, config_name='temp_stats'):
    # Walks over directory collecting all files representing each simulation results
    return [os.path.join(dirpath, f)
            for dirpath, dirnames, files in os.walk(general_path)
            for f in files if f.startswith(config_name)]


def associate_config_file(files):
    # Walks over directory collecting all configuration files associated with each simulation results
    return [os.path.join(os.path.dirname(os.path.dirname(f)), 'conf.json')
            for f in files
            if os.path.exists(os.path.join(os.path.dirname(os.path.dirname(f)), 'conf.json'))]


def process_each_file(file_name, output_list, config_list, y=pd.DataFrame(), x=pd.DataFrame()):
    # Extract both parameters from conf.JSON files and results of that given simulation from 'avg' folder
    for i, each in enumerate(output_list):
        y_test = pd.read_csv(each, sep=';', header=None)
        # Testing minimum length of simulation
        if len(y_test) >= 240:
            y = y.append(y_test)
            x = x.append(json_to_dict(read_json(config_list[i])))
    # Provides names for the columns of results of simulation
    try:
        y.columns = cols.OUTPUT_DATA_SPEC[file_name.replace('temp_', '')]['columns']
    except ValueError:
        print('Column inconsistency')
    return x, y


def read_json(p):
    # Interpret JSON file of configuration with simulation given parameters
    return json.load(open(p))


def json_to_dict(json_dict):
    # Transforms JSON data into DataFrame, removing unchanging columns, extracting data from list
    df = pd.DataFrame.from_dict(json_dict, orient='index').drop(labels='RUN', axis=0).dropna(axis=1)
    df = df.drop(['LIST_NEW_AGE_GROUPS', 'TAXES_STRUCTURE', 'SIMPLIFY_POP_EVOLUTION'], axis=1)
    # Unpacking metropolis region info
    df['PROCESSING_ACPS'] = df['PROCESSING_ACPS'].apply(lambda x: x[0])
    return df


def last_month(df):
    return df[df.months == 239].drop('months', axis=1)


def selecting_y(df, col):
    # Selects only results from last month of simulation
    return df[col]


def customizing_target(base, percentile=65, op=operator.gt):
    # Discretizes results for a given percentile and a given operator (greater than or less than)
    return pd.DataFrame({'target': [1 if op.__call__(x, np.percentile(base, percentile)) else 0 for x in base]})


def averaging_targets(df1, df2):
    # Summarizes two target columns into one when both results are one
    return pd.DataFrame({'target': [1 if x == 1 and y == 1 else 0 for x, y in zip(df1['target'], df2['target'])]})


def dummies(data):
    cat, num = [], []
    for i in data.columns:
        if data[i].dtype == object:
            cat.append(i)
        else:
            num.append(i)
    cat = data[cat]
    try:
        cat = cat.drop(['PROCESSING_STATES'], axis=1)
    except:
        pass
    cat = pd.get_dummies(cat)
    num = data[num]
    try:
        num = num.drop(['HIRING_SAMPLE_SIZE'], axis=1)
    except:
        pass
    return pd.concat([num, cat], axis=1)


def main(pathway, selected_col1, selected_col2):
    # Runs the script for a given directory and two given targets
    # Target1 set to percentile 80 and greater than
    # Target2 set to percentile 20 and less than
    file_list = read_conf_files(pathway)
    data_x, data_y = process_each_file(file_list, cols_names)
    # Getting last months' data
    data_y = last_month(data_y)

    # Excluding the binary operation on target and keeping all values

    first_col = customizing_target(selecting_y(data_y, selected_col1))
    second_col = customizing_target(selecting_y(data_y, selected_col2), 35, operator.lt)
    data_y = averaging_targets(first_col, second_col)

    data_x = dummies(data_x)
    name = 'pre_processed_data\\' + pathway[-4:] + '_' + selected_col1 + '_' + selected_col2 + '_x.csv'
    data_x.to_csv(name, index=False, sep=';')
    data_y.to_csv(name.replace('x.csv', 'y.csv'), index=False, sep=';')
    return data_x, data_y


def unique_cols(df):
    a = df.to_numpy()
    return (a[0] == a).all(0)


def main2(path, datafile_name):
    # Get list of files
    print('Reading configuration files...')
    list_of_files = read_conf_results_files(p, output_data_file_name)
    # Get associated conf.json files
    print('Reading data files...')
    list_of_conf_files = associate_config_file(list_of_files)
    print(f'Files of configuration are of the same size: {len(list_of_files) == len(list_of_conf_files)}')
    print('Processing files...')
    x, y = process_each_file(output_data_file_name, list_of_files, list_of_conf_files)
    return x, y


if __name__ == "__main__":
    p = r'\\storage1\carga\MODELO DINAMICO DE SIMULACAO\Exits_python\PS2020'
    # f'temp_' + {stats', 'firms', 'banks', 'construction' and 'regional'} are always saved
    output_data_file_name = 'temp_stats'

    X, Y = main2(p, output_data_file_name)


    # NEXT STEP, REDUCE Y TO LAST LINE BEFORE SAVING.
    # CHECK X FOR COLUMNS WITHOUT VARIATION

    # target1 = 'average_qli'
    # target2 = 'unemployment'

    # x, y = main(path, target1, target2)
