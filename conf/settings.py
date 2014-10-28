import os.path

ROOT_PATH=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
DATA_PATH=os.path.join(ROOT_PATH, "data")
MODEL_PATH=os.path.join(ROOT_PATH, "models")
MOVIE_SOURCE=os.path.join(DATA_PATH, "movies.dat")
MOVIE_PICKLE=os.path.join(DATA_PATH, "movies.pickle")
TAGS_SOURCE=os.path.join(DATA_PATH, "tags.dat")
RATINGS_SOURCE=os.path.join(DATA_PATH, "ratings.dat")
USER_PICKLE=os.path.join(DATA_PATH, "users.pickle")

PORT=8000

