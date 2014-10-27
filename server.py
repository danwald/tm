from bottle import Bottle, run, get

from conf.settings import PORT

'''Simple RestAPI described http://docs.mrec.apiary.io/'''
app = Bottle()

@app.get('/ping')
def ping():
    return "pong"

@app.get('/recommendation/<type:re:movie|user>/<id:int>')
def recommendation(type, id):
    return {'id':-1, 'data': {'input': {'type': type, 'id':id}}}

@app.get('/recommendation/movie/<movie_id:int>/user/<user_id:int>')
def recommendation(movie_id, user_id):
    return {'id':-1, 'data': {'input': {'movie_id': movie_id, 'user_id':user_id}}}

run(app, host='localhost', port=PORT)
