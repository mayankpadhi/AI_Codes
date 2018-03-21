import numpy as np


def em(x, n_clusters, eps):
    n_examples, n_features = x.shape
    last_log_estimate = None
    mean = np.random.uniform(np.min(x, axis=0), np.max(x, axis=0), size=(n_clusters, n_features))
    cov = [np.identity(n_features) for _ in range(n_clusters)]
    p = np.full((n_clusters,), 1.0 / n_clusters)

    while True:
        # Expectation
        p_cluster = np.zeros((n_examples, n_clusters))
        for c in range(n_clusters):
            var = np.sum((x - mean[c]).dot(np.linalg.inv(cov[c])) * (x - mean[c]), axis=1)
            p_cluster[:, c] = p[c] * np.exp(-var / 2) / np.sqrt(np.abs(2 * np.pi * np.linalg.det(cov[c])))
        normalized_p_cluster = p_cluster / np.sum(p_cluster, axis=1).reshape((-1, 1))

        # Maximization
        p = np.sum(normalized_p_cluster, axis=0) / n_examples
        for c in range(n_clusters):
            mean[c] = np.average(x, axis=0, weights=normalized_p_cluster[:, c])
            cov[c] = np.cov(x.T, aweights=normalized_p_cluster[:, c])

        # Log estimate
        log_estimate = np.sum(np.log(np.sum(p_cluster, axis=0)))
        if last_log_estimate is not None and np.abs(log_estimate - last_log_estimate) < eps:
            return np.argmax(normalized_p_cluster, axis=1)
        else:
            last_log_estimate = log_estimate


def _main():
    import csv
    import matplotlib.pyplot as plt
    import matplotlib.colors as colors

    def load_data(path, delimiter=','):
        with open(path, 'r') as f:
            reader = csv.reader(f, delimiter=delimiter)
            return np.array([[float(v) for v in x] for x in reader])

    data = load_data('names.csv')
    n_clusters = 6
    idx = em(data, n_clusters, eps=1e-5)
    col = iter(colors.cnames.values())

    for c in range(n_clusters):
        x, y = zip(*data[np.where(idx == c)])
        plt.scatter(x, y, color=next(col))

    plt.show()


if __name__ == '__main__':
    _main()
