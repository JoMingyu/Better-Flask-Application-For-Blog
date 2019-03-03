from flask import Flask, Response

from api import index

app = Flask(__name__)

app.add_url_rule('/', 'index', index.index)


if __name__ == '__main__':
    app.run()
