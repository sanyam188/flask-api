from flask import Flask,render_template,jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello, Sanyam'
    return render_template('api.html')

data=[{'name' : 'Sanyam','contact': '9690459433'
},]

@app.route('/<int:user>')
def hello1(user):
    return 'User %s' % user 

@app.route('/link/')
def link():
    return jsonify(data)

if __name__=='__main__':
    app.run(debug=True)