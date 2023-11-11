from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def convert():
    celsius = float(request.form['celsius'])
    fahrenheit = (celsius * 9/5) + 32
    return render_template('index.html', fahrenheit=fahrenheit)

if __name__ == '__main__':
    app.run(debug=True)