from flask import Flask, render_template
from BluePoints.image_transfer import bp as transfer

app = Flask(__name__)

app.register_blueprint(transfer)


@app.route('/')
def index():
    return 'test'


if __name__ == '__main__':
    app.run()
