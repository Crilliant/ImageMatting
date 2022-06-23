from flask import Blueprint, request, jsonify
from back.config import image_upload_path, image_download_path
import os, flask


bp = Blueprint('transfer', __name__, url_prefix='/api/image')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'JPG', 'PNG'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1) in ALLOWED_EXTENSIONS


@bp.route('/upload', methods=['POST'])
def upload_image():
    try:
        img = request.files.get('photo')
        file_path = os.path.join(image_upload_path, img.filename)
        img.save(file_path)
        return jsonify({'message': 'success'})
    except Exception as err:
        return jsonify({'message': str(err)})


@bp.route('/download', methods=['POST'])
def download_image():
    filename = request.get_json().get('filename')
    return flask.send_from_directory(image_download_path, filename)
