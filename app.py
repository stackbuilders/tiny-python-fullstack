from flask import Flask, jsonify, request, Response

app = Flask(__name__)


class FakeConsumer:
    def json(self):
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
def index():
    return Response('{"Hello":"World"}', mimetype='application/json')


@app.route('/info', methods=['POST'])
def user():
    if 'user' in request.form and request.form['user'] != '':
        consumer = FakeConsumer()
        return jsonify(consumer.json())
    return 'Missing `user` parameter', 400


if __name__ == '__main__':
    app.run(debug=True)
