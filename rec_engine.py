import cPickle as pickle
from itertools import islice
import math

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
        try:
            data = {}
            user = self.user_data[id]
            user_movies = set(user.keys())
            count = 0
            for user_id in self.user_data.iterkeys():
                if user_id == id:
                    continue
                similar_rating = 0
                movies_overlap = user_movies & set(self.user_data[user_id].keys())
                for movie_overlap in movies_overlap:
                    if math.fabs(user[movie_overlap]['rating'] -
                                self.user_data[user_id][movie_overlap]['rating']) <= 1.0:
                        similar_rating += 1
                if similar_rating / float(len(movies_overlap)) > 0.5:
                    data[user_id] = self.user_data[user_id]
                    count += 1
                if count == 10:
                    break
            return data
        except:
            return {}
