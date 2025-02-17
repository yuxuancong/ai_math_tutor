from sqlalchemy.orm import Session
from core.models.user import User
import bcrypt
import jwt
from datetime import datetime, timedelta
from config.settings import API_CONFIG

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, username: str, email: str, password: str) -> User:
        # 检查用户是否已存在
        if self.db.query(User).filter(User.email == email).first():
            raise ValueError("Email already registered")
            
        # 密码加密
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        
        user = User(
            username=username,
            email=email,
            password_hash=password_hash.decode()
        )
        
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def authenticate_user(self, email: str, password: str) -> str:
        user = self.db.query(User).filter(User.email == email).first()
        if not user:
            return None
            
        if not bcrypt.checkpw(password.encode(), user.password_hash.encode()):
            return None
            
        # 生成JWT令牌
        token = jwt.encode(
            {
                'user_id': user.id,
                'exp': datetime.utcnow() + timedelta(days=1)
            },
            API_CONFIG['secret_key'],
            algorithm='HS256'
        )
        
        return token

    def get_user_by_id(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first() 