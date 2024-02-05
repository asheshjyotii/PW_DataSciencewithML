from flask import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/secret', methods=['POST'])
def secret():
    message_ = request.form['msg']
    key_ = int(request.form['key'])

    operation = request.form['operation']
    if operation == 'encrypt':
        msg = message_
        key = key_
        msg = msg.rsplit()
        encrypt = ""
        for i in msg:
            for j in i:
                encrypt = encrypt + (chr(ord(j) + key))
            encrypt = encrypt + " "
        return f"Your Encrypted message is:\n{encrypt}"
    elif operation == 'decrypt':
        key = key_
        msg = message_
        msg = msg.rsplit()
        decrypted = ""
        for i in msg:
            for j in i:
                decrypted = decrypted + chr(ord(j) - key)
            decrypted = decrypted + " "
        return f"Your Decrypted message is:\n{decrypted}"
    else:
        return "wrong function"


app.run(debug=True, port=10)
