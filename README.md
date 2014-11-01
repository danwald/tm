Movie Recommendation Engine
===========================

This is a REST Driven Movie recommendation engine using the movie lens data. The API http://docs.mrec.apiary.io/ allows:

  - Lookup information of a user or movie given an id
  - Gets movie recommendations. Uses K-means clusters for similar movie genres
  - Gets user recommendataion. Finds similar users who have rated movies, similarily
  - Gets a movie recommendation based on a given movie and user [not implemented]


Version
----

1.0


Installation
--------------

```bash
sudo apt-get update
sudo apt-get install python-virtualenv python-dev python ipython build-essential python-setuptools
wget https://github.com/danwald/tm/archive/v1.0.tar.gz
tar xvfz v1.0.tar.gz
virtualenv tm
. ./tm/bin/activate
cd master
pip install -r requirements/requirements.txt
bash scripts/get_data.sh
python scripts/compute_pickled_dicts.py
python scripts/gen_clusters.py
```

Running
-------

```bash
python server.py
```


Testing
-------

```bash
curl localhost:8000/recommendation/movie/1
```

Todo
----

    - implement movie/user recommendation
    - test cases
    - docker file for deployment

License
----

MIT


**Free Software, Hell Yeah!**
