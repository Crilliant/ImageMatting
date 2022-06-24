import flask
import os
from flask import Blueprint, request, jsonify
from back.config import image_upload_path, image_download_path
from back.BluePoints.utils import generate_image_name

bp = Blueprint('transfer', __name__, url_prefix='/api/image')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'JPG', 'PNG'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1) in ALLOWED_EXTENSIONS


@bp.route('/upload', methods=['POST'])
def upload_image():
    try:
        img = request.files.get('img')
        file_extension = '.' + img.filename.split('.')[1]
        new_file_name = generate_image_name() + file_extension
        file_path = os.path.join(image_upload_path, new_file_name)
        img.save(file_path)
        return jsonify({'status': 'success', 'message': new_file_name})
    except Exception as err:
        return jsonify({'status': 'failed', 'message': str(err)})


@bp.route('/download', methods=['POST'])
def download_image():
    filename = os.path.join(image_download_path, request.get_json().get('filename'))
    if os.path.exists(filename):
        with open(filename, 'rb') as img:
            resp = flask.make_response(img.read())
            resp.headers['Content-Type'] = 'image/jpeg'
            resp.headers['Process-Type'] = 'test'
            return resp
    else:
        return jsonify({'status': 'wait', 'time': 5})


# TODO: 根据处理类型调用服务
@bp.route('/segment')
def segment_image():
    pass


# TODO: 什么适合删除需要讨论
@bp.route('/delete')
def delete_image():
    filename = request.get_json().get('filename')
    try:
        if os.path.exists(os.path.join(image_upload_path, filename)):
            os.remove(os.path.join(image_upload_path, filename))
        if os.path.exists(os.path.join(image_download_path, filename)):
            os.remove(os.path.join(image_download_path, filename))
        return jsonify({'status': 'success'})
    except Exception as err:
        return jsonify({'status': 'failed', 'message': str(err)})
