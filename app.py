from flask import Flask, Response

app = Flask(__name__)


@app.route('/')
def index():
    return Response('Hello World', mimetype='text/plain')


if __name__ == '__main__':
    app.run()
