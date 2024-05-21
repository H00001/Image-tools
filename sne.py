import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

def t_sne(embeds, labels, sample_num, title):
    """
    Visualize embedding by t-SNE algorithm.
    :param embeds: Embedding of the data.
    :param labels: Labels.
    :param sample_num: The number of samples.
    :param show_fig: If True, show the figure.
    :return: fig: The figure.
    """
    
    # Sampling
    sample_index = np.random.randint(0, embeds.shape[0], sample_num)
    sample_embeds = embeds[sample_index]
    sample_labels = labels[sample_index]

    # t-SNE
    ts = TSNE(n_components=2, init='pca', random_state=0)
    ts_embeds = ts.fit_transform(sample_embeds)

    # Remove outliers
    mean, std = np.mean(ts_embeds, axis=0), np.std(ts_embeds, axis=0)
    inliers = (np.abs(ts_embeds - mean) < 3 * std).all(axis=1)
    ts_embeds = ts_embeds[inliers]
    sample_labels = sample_labels[inliers]

    # Normalization
    x_min, x_max = np.min(ts_embeds, axis=0), np.max(ts_embeds, axis=0)
    norm_ts_embeds = (ts_embeds - x_min) / (x_max - x_min)

    # Plot
    plt.rcParams["font.family"] = "Times New Roman"
    fig, ax = plt.subplots()
    scatter = ax.scatter(norm_ts_embeds[:, 0], norm_ts_embeds[:, 1], c=sample_labels, cmap=plt.cm.get_cmap('Set1', np.unique(sample_labels).size), s=10)
    legend1 = ax.legend(*scatter.legend_elements(), title="Classes")
    ax.add_artist(legend1)
    plt.xticks([])
    plt.yticks([])
    plt.title(title, fontsize=14)
    plt.axis('off')
    return fig

if __name__ == '__main__':
    name = "hhar"
    sv = t_sne(np.load(f"./sne/{name}.npy"),np.loadtxt(f"./sne/{name}_label.txt"),10300,f"{name}")
    sv.savefig(f"sne/{name}.png")