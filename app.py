from flask import Flask, jsonify, request, Response

app = Flask(__name__)


class FakeConsumer:
    def json(self):
        return {
            'name': 'Stack Builders',
            'email': 'info@stackbuilders.com'
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
