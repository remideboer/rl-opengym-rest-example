from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    return 'Hello! Hello!'

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html', msg='De Boodschap')

@app.route('/index/<msg>', methods=['GET'])
def indexMsg(msg):
    return render_template('index.html', msg=msg)

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return render_template('hello.html', greeting='De Grote Groet')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
