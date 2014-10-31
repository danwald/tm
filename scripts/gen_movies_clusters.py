if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import os
import cPickle as pickle
import math

from numpy import vstack
from scipy.cluster.vq import kmeans,vq

from conf.settings import *


def run():
    movies = pickle.load(open(MOVIE_PICKLE, 'rb'))
    tags = set()
    for movie in movies.values():
        for tag in movie['tags']:
            tags.add(tag)

    tags = { value:index for index, value in enumerate(sorted(tags))}
    movie_keys = sorted(movies.keys())
    feature_vectors = []
    total_tags = 1.0
    for movie_key in movie_keys:
        movie_feature_vector = len(tags)*[0]
        for tag in movies[movie_key]['tags']:
            movie_feature_vector[tags[tag]] = 1
            total_tags += 1.0
        feature_vectors.append(movie_feature_vector)

    clusters = int(math.ceil((total_tags) / len(movie_keys))) * len(tags)
    print "Using %d clusters (%d #total_tags / %d #movies) * %d #tags" % (clusters, int(total_tags), len(movie_keys), len(tags))

    feature_vectors = vstack(feature_vectors)
    centroids, _ = kmeans(feature_vectors,clusters)
    clustered_movies, _ = vq(feature_vectors, centroids)
    pickle.dump(centroids, open(TAGS_PICKLE, 'wb'))
    pickle.dump(movie_keys, open(TAGS_PICKLE, 'wb'))
    pickle.dump(clustered_movies, open(TAGS_PICKLE, 'wb'))
    pickle.dump(tags, open(TAGS_PICKLE, 'wb'))


if __name__ == "__main__":
    run()
