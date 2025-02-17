# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

# ���ػ�������
load_dotenv()

# ��������
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True

# ���ݿ�����
DATABASE_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'ai_math_tutor',
    'user': 'postgres',
    'password': '123456'
}

# API����
API_CONFIG = {
    'version': '1.0',
    'prefix': '/api/v1',
    'secret_key': 'dev-secret-key'
}