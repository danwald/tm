import cPickle as pickle

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
            self.genre_centroids = pickle.load(tags_file)
            self.genre_movie_keys = pickle.load(tags_file)
            self.genre_clustered_movies = pickle.load(tags_file)
            self.genre_tags = pickle.load(tags_file)

    def get_movie(self, id):
        return self.movie_data[id];
        
    def get_user(self, id):
        return self.user_data[id];
