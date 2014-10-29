if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import os
import cPickle as pickle
import threading

from conf.settings import *

def gen_movies():
    movies={}
    with open(MOVIE_SOURCE) as movie_file:
        count = 0
        error_count = 0
        for movie in movie_file:
            count += 1
            try:
                record = filter(bool, movie.split('::'))
                movies[int(record[0])] = {'title':record[1],'tags': record[2].strip().split('|')}
            except:
                print movie
                error_count += 1
                pass
    pickle.dump(movies, open(MOVIE_PICKLE, 'wb'))
    print "\nGenerated %s. Processed %d records (errors:%d) (len:%d)"%(MOVIE_PICKLE, count, error_count, len(movies)),

def gen_users():
    users = {}
    RATINGS_SOURCE_KEY = 'rating'
    TAGS_SOURCE_KEY = 'tags'
    for data_input in [(TAGS_SOURCE, TAGS_SOURCE_KEY), (RATINGS_SOURCE, RATINGS_SOURCE_KEY)]:
        with open(data_input[0]) as data:
            count = 0
            error_count = 0
            for record in data:
                count += 1
                try:
                    user_id, movie_id, rating_or_tag, _ = filter(bool, record.split('::'))
                    user_data = users[int(user_id)]
                except KeyError:
                    user_data = {int(movie_id): {
                                     RATINGS_SOURCE_KEY: float(rating_or_tag) if data_input[1] == RATINGS_SOURCE_KEY else -1,
                                     TAGS_SOURCE_KEY:[rating_or_tag] if data_input[1] == TAGS_SOURCE_KEY else []
                                     }
                                }
                    users[int(user_id)] = user_data
                except:
                    print record
                    error_count += 1
                    pass
                else:
                    try:
                        movie_data = user_data[int(movie_id)]
                    except KeyError:
                        user_data[int(movie_id)] = {
                                 RATINGS_SOURCE_KEY: float(rating_or_tag) if data_input[1] == RATINGS_SOURCE_KEY else -1,
                                 TAGS_SOURCE_KEY:[rating_or_tag] if data_input[1] == TAGS_SOURCE_KEY else []}
                    else:
                        if data_input[1] == RATINGS_SOURCE_KEY:
                            movie_data[data_input[1]] = float(rating_or_tag)
                        else:
                            movie_data[data_input[1]].append(rating_or_tag)
    pickle.dump(users, open(USER_PICKLE, 'wb'))
    print "\nGenerated %s. Processed %d records (errors:%d) (len:%d)"%(USER_PICKLE, count, error_count, len(users)),

def run():
    threads = []
    for target in [gen_movies, gen_users]:
        threads.append(threading.Thread(target=target))
        threads[-1].start()

    for thread in threads:
        thread.join()

    return 0


if __name__ == "__main__":
    run()
