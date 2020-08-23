from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "This is my homepage 099"


@app.route('/hello')
def hello():
    return {"message": "Auwat api welcome"}


@app.route('/who')
def anuwat():
    return "My name is anuwat : Anu Wat called me anuwat not anu"


if __name__ == "__main__":
    app.run()
