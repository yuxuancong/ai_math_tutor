from flask import Blueprint, request, jsonify
from core.services.user_service import UserService
from infrastructure.database.connection import get_db_session

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    db = get_db_session()
    try:
        service = UserService(db)
        user = service.create_user(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password')
        )
        return jsonify({"message": "User registered successfully", "user_id": user.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    db = get_db_session()
    try:
        service = UserService(db)
        token = service.authenticate_user(
            email=data.get('email'),
            password=data.get('password')
        )
        if token:
            return jsonify({"token": token}), 200
        return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        db.close() 