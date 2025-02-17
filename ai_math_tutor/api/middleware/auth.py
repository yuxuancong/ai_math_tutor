from functools import wraps
from flask import request, jsonify
import jwt
from config.settings import API_CONFIG
from core.services.user_service import UserService
from infrastructure.database.connection import get_db_session

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        # 检查请求头中是否有token
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].replace('Bearer ', '')
            
        if not token:
            return jsonify({'error': 'Token is missing'}), 401
            
        try:
            # 验证token
            data = jwt.decode(token, API_CONFIG['secret_key'], algorithms=['HS256'])
            db = get_db_session()
            user_service = UserService(db)
            current_user = user_service.get_user_by_id(data['user_id'])
            
            if not current_user:
                return jsonify({'error': 'Invalid token'}), 401
                
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401
        except Exception as e:
            return jsonify({'error': str(e)}), 401
        finally:
            db.close()
            
        return f(*args, **kwargs)
        
    return decorated 