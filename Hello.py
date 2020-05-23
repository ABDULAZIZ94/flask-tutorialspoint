#!/usr/bin/python
#converters
from flask import Flask
app = Flask(__name__)

@app.route('/blog/<int:postID>')
def hello_world(postID):
    return 'Hello world %d !' % postID

@app.route('/rev/<float:revNO>')
def revision(revNO):
    return 'Revision number %f' % revNO

if __name__ == '__main__':
    app.run('0.0.0.0', 80)


