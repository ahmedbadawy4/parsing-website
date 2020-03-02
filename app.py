from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = False

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/p1')
def p1():
    return "P1!!!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
