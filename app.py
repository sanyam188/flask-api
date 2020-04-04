from flask import Flask,render_template,jsonify,request
app = Flask(__name__)
import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

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
    con=sqlite3.connect('books.db')
    con.row_factory = dict_factory
    cur=con.cursor()
    all_books=cur.execute('select * from books;').fetchall()
    return jsonify(all_books)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/link/')
def api_search():
    query_para=request.args
    id=query_para.get('id')
    pub=query_para.get('published')
    aut=query_para.get('author')

    query="select * from books where "
    filter=[]

    if id:
        query+='id=? AND '
        filter.append(id)
    if aut:
        query+='author=? AND '
        filter.append(aut)
    if pub:
        query+='published=? AND '
        filter.append(pub)


    query=query[:-4]+';'
    con=sqlite3.connect('books.db')
    con.row_factory = dict_factory
    cur=con.cursor()
    res=cur.execute(query, filter).fetchall()
    # if 'id' in request.args:
    #     id=int(request.args['id'])
    # else:
    #     return "Ops Error"

    # res=[]

    # for b in books:
    #     if id==b['id']:
    #         res.append(b)

    return jsonify(res)




if __name__=='__main__':
    app.run(debug=True)