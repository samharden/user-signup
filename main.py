from flask import Flask, request
from forms import form
from caesar import encrypt as enc
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=["POST"])
def encrypt():
    rot = int(request.form["rot"])
    text = request.form["text"]
    result = enc(text, rot)

    return form.format(result)


app.run()
