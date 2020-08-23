from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "This is my homepage 099"


@app.route('/hello')
def hello():
    return {"message": "Auwat api welcome"}


if __name__ == "__main__":
    app.run()
