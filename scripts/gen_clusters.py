if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import os
import cPickle as pickle
import math

from numpy import vstack
from scipy.cluster.vq import kmeans,vq

from conf.settings import *

def gen_movie_clusters():
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
    classified_movies = {record[0]:record[1] for record in zip(movie_keys, clustered_movies)}
    movies_by_cluster = {k:set() for k in xrange(0,clusters)}
    for record in zip(movie_keys, clustered_movies):
        movies_by_cluster[record[1]].add(record[0])
    
    with open(TAGS_PICKLE, 'wb') as data_file:
        pickle.dump(classified_movies, data_file)
        pickle.dump(movies_by_cluster, data_file)
        pickle.dump(tags, data_file)

if __name__ == "__main__":
    gen_movie_clusters()
