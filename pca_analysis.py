import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def plot_correlation(data):

    corr = data.corr()
    sns.heatmap(corr,
                xticklabels=corr.columns.values,
                yticklabels=corr.columns.values)

    plt.show()


def run_pca(data):
    data = np.array(data)
    return PCA().fit(data)


if __name__ == '__main__':
    y = pd.read_csv('y.csv', sep=';')
    # plot_correlation(y)
    pca = run_pca(y)
    print(pca.explained_variance_ratio_)
    print(pca.singular_values_)
