from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('formdata.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("formdata_result.html",result = result)

if __name__ == '__main__':
   app.run('0.0.0.0', 80, debug = True)
