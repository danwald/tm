if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import os
import cPickle as pickle
import timeit
from conf.settings import *

def gen_movies():
    print "Generating Movies"
    movies={}
    with open(MOVIE_SOURCE) as movie_file:
        count = 0
        error_count = 0
        for movie in movie_file:
            count += 1
            try:
                record = filter(bool, movie.split(':'))
                movies[int(record[0])] = {'title':record[1],'tags': record[2].split('|')}
            except:
                print movie
                error_count += 1
                pass
            print "\rProcessing %d records (errors:%d)"%(count, error_count),
    pickle.dump(movies, open(MOVIE_PICKLE, 'wb'))

def run():
    gen_movies()
    return 0


if __name__ == "__main__":
    run()
