from flask import Flask, Response
from BluePoints.image_transfer import bp as transfer

app = Flask(__name__)

app.register_blueprint(transfer)


@app.route('/test', methods=['POST'])
def index():
    return Response('test')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
