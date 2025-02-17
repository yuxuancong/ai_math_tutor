# AI 数学助教系统 ?

## ? 项目结构
text
ai_math_tutor/
├── api/ # API接口层
│ └── routes.py # 路由定义
├── core/ # 核心业务层
│ ├── models.py # 数据模型
│ └── services/ # 业务服务
│ ├── user_service.py # 用户服务
│ └── math_problem_service.py # 数学题服务
├── infrastructure/ # 基础设施层
│ └── database/ # 数据库相关
│ └── connection.py # 数据库连接
├── config/ # 配置文件
│ └── settings.py # 系统配置
├── tests/ # 测试目录
│ ├── test_api/ # API测试
│ └── test_services/ # 服务测试
├── .gitignore # Git忽略文件
├── requirements.txt # 项目依赖
├── README.md # 项目说明
└── app.py # 应用入口


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

## ? 安装步骤
1. **克隆项目**
   ```bash
   git clone https://github.com/你的用户名/ai_math_tutor.git
   cd ai_math_tutor
   ```

2. **创建虚拟环境**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

4. **配置数据库**
   ```sql
   CREATE DATABASE ai_math_tutor;
   ```

5. **运行项目**
   ```bash
   python app.py
   ```

## ? API 文档

### 用户接口
| 方法 | 路径 | 描述 |
|------|------|------|
| POST | `/api/v1/auth/register` | 用户注册 |
| POST | `/api/v1/auth/login` | 用户登录 |
| GET | `/api/v1/auth/profile` | 获取用户信息 |

### 数学题接口
| 方法 | 路径 | 描述 |
|------|------|------|
| POST | `/api/v1/problems/generate` | 生成题目 |
| POST | `/api/v1/problems/verify` | 验证答案 |
| GET | `/api/v1/problems/history` | 获取历史记录 |

## ? 团队分工

### 后端开发 (A, B, C)
- 用户系统
- 数学题生成
- 答案验证

### 前端开发 (D, E)
- 页面设计
- 交互实现

### 测试文档 (F, G)
- 功能测试
- 文档编写

## ? 项目进度
- [x] 项目初始化
- [x] 数据库配置
- [ ] 用户系统
- [ ] 数学题模块
- [ ] 前端界面
- [ ] 测试完善

## ? 联系方式
- **项目负责人：** xxx
- **邮箱：** xxx@xxx.com
- **微信群：** xxx

## ? 许可证
MIT License

## ? 贡献指南
1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 发起 Pull Request

## ? 更新日志
### v0.1.0 (2024-02-17)
- 项目初始化
- 基础框架搭建
- 数据库配置完成