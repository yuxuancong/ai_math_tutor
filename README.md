# ? AI 数学助教系统

## ? 项目结构
ai_math_tutor/
├── api/                    # API接口层
│   └── routes.py          # 路由定义
├── core/                   # 核心业务层
│   ├── models.py          # 数据模型
│   └── services/          # 业务服务
│       ├── user_service.py        # 用户服务
│       └── math_problem_service.py # 数学题服务
├── infrastructure/         # 基础设施层
│   └── database/          # 数据库相关
│       └── connection.py  # 数据库连接
├── config/                # 配置文件
│   └── settings.py        # 系统配置
├── tests/                 # 测试目录
├── .gitignore            # Git忽略文件
├── requirements.txt       # 项目依赖
└── app.py                # 应用入口

## ? 功能特点
- ? 智能生成数学题
- ? 自动答案验证
- ? 用户进度跟踪
- ? 难度自适应
- ? 历史记录统计

## ? 技术栈
- 后端框架：Python Flask
- 数据库：PostgreSQL
- ORM：SQLAlchemy
- 认证：JWT
- 文档：Swagger/OpenAPI

## ? 环境要求
- Python 3.8+
- PostgreSQL 12+
- 依赖包要求见 requirements.txt