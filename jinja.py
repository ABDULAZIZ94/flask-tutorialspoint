from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('jinja.html', result = dict)

if __name__ == '__main__':
   app.run('0.0.0.0', 80, debug = True)

def a():
    str = "lalalala"
    return str

