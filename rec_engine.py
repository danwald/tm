import cPickle as pickle
from itertools import islice

from conf.settings import *

class RecEngine(object):
    def __init__(self):
        self._get_user_movies_data()
        self._get_tags_data()

    def _get_user_movies_data(self):
        self.user_data = pickle.load(open(USER_PICKLE, 'rb'))
        self.movie_data = pickle.load(open(MOVIE_PICKLE, 'rb'))
    
    def _get_tags_data(self):
        with open(TAGS_PICKLE, 'rb') as tags_file:
            self.classified_movies = pickle.load(tags_file)
            self.movies_by_cluster = pickle.load(tags_file)
            self.movies_tags = pickle.load(tags_file)

    def get_movie(self, id):
        return self.movie_data[id];
        
    def get_user(self, id):
        return self.user_data[id];

    def get_movie_recommendation(self, id):
        try:
            data = {}
            for similar_movie in islice(self.movies_by_cluster[self.classified_movies[id]], 0, 100):
                data[similar_movie] = self.movie_data[similar_movie]
            return data
        except:
            return {}
        
    def get_user_recommendation(self, id):
        return self.user_data[id];
