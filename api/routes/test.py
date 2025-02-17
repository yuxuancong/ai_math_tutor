from flask import Blueprint, jsonify

bp = Blueprint('test', __name__)

@bp.route('/test', methods=['GET'])
def test():
    return jsonify({
        'status': 'success',
        'message': 'API is working!'
    }) 