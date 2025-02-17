# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 基础配置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True

# 数据库配置
DATABASE_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'ai_math_tutor',
    'user': 'postgres',
    'password': '123456'
}

# API配置
API_CONFIG = {
    'version': '1.0',
    'prefix': '/api/v1',
    'secret_key': 'dev-secret-key'
}