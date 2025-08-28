from flask import Flask, render_template, session

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

def sum(num1, num2):
    pass



if __name__ == '__main__':
    app.run(debug=True)