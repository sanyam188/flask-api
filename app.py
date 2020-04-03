from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Sanyam '

@app.route('/<int:user>')
def hello1(user):
    return 'User %s' % user 

if __name__=='__main__':
    app.run(debug=True)