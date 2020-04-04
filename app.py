from flask import Flask,render_template,jsonify,request
app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello, Sanyam'
    return render_template('api.html')

books=[
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/<int:user>')
def hello1(user):
    return 'User %s' % user 

@app.route('/link/all')
def api_all():
    return jsonify(books)

@app.route('/link/')
def api_search():
    if 'id' in request.args:
        id=int(request.args['id'])
    else:
        return "Ops Error"

    res=[]

    for b in books:
        if id==b['id']:
            res.append(b)

    return jsonify(res)




if __name__=='__main__':
    app.run(debug=True)