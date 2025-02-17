# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from core.models import Base

def create_db_engine():
    try:
        # �滻Ϊ���ʵ������
        DATABASE_URL = "postgresql+psycopg2://postgres:Congyuxuan0161@localhost:5432/ai_math_tutor"
        
        # �������棬ֻʹ�û�������
        engine = create_engine(
            DATABASE_URL,
            pool_pre_ping=True,
            echo=True  # ���� SQL ��־
        )
        
        # ��������
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