from flask import Flask, Response

import api

app = Flask(__name__)

app.add_url_rule('/', 'index', api.index)


if __name__ == '__main__':
    app.run()
