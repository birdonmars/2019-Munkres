from sklearn.cluster import KMeans


def k_means(X, k):
    # Number of clusters
    kmeans = KMeans(n_clusters=k)
    # Fitting the input data
    kmeans = kmeans.fit(X)
    # Getting the cluster labels
    labels = kmeans.predict(X)
    # Centroid values
    centroids = kmeans.cluster_centers_

    '''
    # Comparing with scikit-learn centroids
    print("Centroid values")

    print("sklearn")
    print(centroids)  # From sci-kit learn

    print("Labels")
    print(labels)
    '''

    return [centroids, labels]
