# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from core.models import Base

def create_db_engine():
    try:
        # 替换为你的实际密码
        DATABASE_URL = "postgresql+psycopg2://postgres:Congyuxuan0161@localhost:5432/ai_math_tutor"
        
        # 创建引擎，只使用基本参数
        engine = create_engine(
            DATABASE_URL,
            pool_pre_ping=True,
            echo=True  # 启用 SQL 日志
        )
        
        # 测试连接
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            print("Database connection successful!")
        
        return engine
        
    except Exception as e:
        print(f"Database connection error: {str(e)}")
        raise

def init_db():
    engine = create_db_engine()
    Base.metadata.create_all(bind=engine)

def get_db_session() -> Session:
    engine = create_db_engine()
    SessionLocal = sessionmaker(bind=engine)
    return SessionLocal() 