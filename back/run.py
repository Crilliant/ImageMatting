from flask import Flask, render_template
from BluePeints.image_transfer import bp as transfer
from BluePeints.image_processor import bp as processor

app = Flask(__name__)

app.register_blueprint(transfer)
app.register_blueprint(processor)


@app.route('/')
def index():
    return 'test'


if __name__ == '__main__':
    app.run()
