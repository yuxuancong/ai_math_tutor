# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from api.routes import auth_bp, math_problems_bp
from infrastructure.database.connection import init_db
from config.settings import API_CONFIG, DEBUG

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = API_CONFIG['secret_key']
    app.config['DEBUG'] = DEBUG
    
    # ��ʼ�����ݿ�
    try:
        init_db()
        print("Database initialized successfully!")
    except Exception as e:
        print(f"Database initialization failed: {str(e)}")
        raise
    
    # ע��·��
    app.register_blueprint(auth_bp, url_prefix=f"{API_CONFIG['prefix']}/auth")
    app.register_blueprint(math_problems_bp, url_prefix=API_CONFIG['prefix'])
    
    @app.route('/health')
    def health_check():
        return jsonify({"status": "healthy"})
    
    # ������
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not found'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        print(f"Internal server error: {str(error)}")
        return jsonify({'error': 'Internal server error'}), 500
        
    return app

# ȷ��ֻ��ֱ������ʱ����������
if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000) 