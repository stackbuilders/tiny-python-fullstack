from flask import Flask, jsonify, request, Response
from typing import Dict, Tuple, Union

FlaskResponse = Union[
    Response,
    Tuple[str, int]
]

app: Flask = Flask(__name__)


class FakeConsumer:
    def json(self) -> Dict:
        return {
            'login': 'stackbuilders',
            'name': 'Stack Builders',
            'email': 'info@stackbuilders.com',
            'location': 'New York',
            'public_repos': 179,
            'public_gists': 0,
            'followers': 0,
            'following': 0
        }


@app.route('/')
def index() -> FlaskResponse:
    return Response('{"Hello":"World"}', mimetype='application/json')


@app.route('/info', methods=['POST'])
def user() -> FlaskResponse:
    if 'user' in request.form and request.form['user'] != '':
        consumer = FakeConsumer()
        return jsonify(consumer.json())
    return 'Missing `user` parameter', 400


if __name__ == '__main__':
    app.run(debug=True)
