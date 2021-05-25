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


def components_plot(pca, labels):
    map_data = pd.DataFrame(pca.components_, columns=labels)
    plt.figure(figsize=(12, 12))
    sns.heatmap(map_data, cmap='twilight')
    plt.show()


def scatter_pca(pca, labels):
    plt.scatter(pca.components_[0], pca.components_[1], label=y.columns)
    for i, txt in enumerate(len(labels)):
        plt.annotate(labels[i], (pca.components_[0][i], pca.components_[1][i]))


def run_pca(data):
    data = np.array(data)
    sc = StandardScaler()
    data = sc.fit_transform(data)
    pca = PCA(n_components=2).fit(data)
    new_x = pca.transform(data)
    return pca, new_x


if __name__ == '__main__':
    y = pd.read_csv('pre_processed_data/y.csv', sep=';')
    # plot_correlation(y)
    p, new_y = run_pca(y)
