import flask


app = flask.Flask(__name__)


@app.route('/api', methods=['GET'])
def get():
    return 'success'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)