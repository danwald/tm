if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import os
import cPickle as pickle
import threading
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
    for movie_key in movie_keys:
        movie_feature_vector = len(tags)*[0]
        for tag in movies[movie_key]['tags']:
            movie_feature_vector[tags[tag]] = 1
        feature_vectors.append(movie_feature_vector)
    feature_vectors = vstack(feature_vectors)
    movies_centroid, min_distorsion = (None, -1)
    for i in xrange(len(tags)):
        centroid, distorsion = kmeans(feature_vectors,i+1) 
        print i, centroid, distorsion
        if distorsion < min_distorsion:
            min_distorsion = distorsion
            movies_centroid = centroid
    print distorsion, movies_centroid


if __name__ == "__main__":
    run()
