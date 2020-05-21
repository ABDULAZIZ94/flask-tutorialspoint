from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
    return 'Hello world %s !' % name

if __name__ == '__main__':
    app.run('0.0.0.0', 80)
