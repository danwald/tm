import os.path

ROOT_PATH=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
DATA_PATH=os.path.join(ROOT_PATH, "data")
MODEL_PATH=os.path.join(ROOT_PATH, "models")
MOVIE_SOURCE=os.path.join(DATA_PATH, "movies.dat")
MOVIE_PICKLE=os.path.join(DATA_PATH, "movies.pickle")
TAGS_SOURCE=os.path.join(DATA_PATH, "tags.dat")
TAGS_PICKLE=os.path.join(DATA_PATH, "tags.pickle")
RATINGS_SOURCE=os.path.join(DATA_PATH, "ratings.dat")
RATINGS_PICKLE=os.path.join(DATA_PATH, "ratings.pickle")

PORT=8000

