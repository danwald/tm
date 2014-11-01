import cPickle as pickle

from bottle import Bottle, run, get, HTTPError

from conf.settings import PORT
from rec_engine import RecEngine

'''Simple RestAPI described http://docs.mrec.apiary.io/'''
app = Bottle()
engine = RecEngine()

@app.get('/ping')
def ping():
    return "pong"

@app.get('/<type:re:movie|user>/<id:int>')
def recommendation(type, id):
    try:
        if type == 'movie':
            return {'id':id, 'data': engine.get_movie(id)}
        else:
            return {'id':id, 'data': engine.get_user(id)}
    except KeyError:
        return HTTPError(status=404)

@app.get('/recommendation/<type:re:movie|user>/<id:int>')
def recommendation(type, id):
    try:
        if type == 'movie':
            return engine.get_movie_recommendation(id)
        else:
            return {'id':id, 'data': engine.get_user(id)}
    except KeyError:
        return HTTPError(status=404)

@app.get('/recommendation/movie/<movie_id:int>/user/<user_id:int>')
def recommendation(movie_id, user_id):
    return {'id':-1, 'data': {'input': {'movie_id': movie_id, 'user_id':user_id}}}

run(app, host='localhost', port=PORT)
