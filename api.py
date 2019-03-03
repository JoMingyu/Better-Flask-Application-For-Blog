from flask import Response


def index():
    return Response('Hello World', mimetype='text/plain')
