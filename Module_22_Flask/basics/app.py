from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/login/<username>')

def loging(username):
    return {
        'username' : username,
        'password' : 'Enter your password'
    }

@app.route('/loggedin')

def logged_in():
    return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(debug=True)