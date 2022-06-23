from flask import Blueprint


bp = Blueprint('processor', __name__, url_prefix='/api/process')


@bp.route('/human_segmentation')
def segment_human_image():
    pass


@bp.route('/change_backcolor')
def change_backcolor():
    pass


@bp.route('/object_segmentation')
def segment_object_image():
    pass
