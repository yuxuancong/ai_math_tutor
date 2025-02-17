# AI ��ѧ����ϵͳ ?

## ? ��Ŀ�ṹ
text
ai_math_tutor/
������ api/ # API�ӿڲ�
�� ������ routes.py # ·�ɶ���
������ core/ # ����ҵ���
�� ������ models.py # ����ģ��
�� ������ services/ # ҵ�����
�� ������ user_service.py # �û�����
�� ������ math_problem_service.py # ��ѧ�����
������ infrastructure/ # ������ʩ��
�� ������ database/ # ���ݿ����
�� ������ connection.py # ���ݿ�����
������ config/ # �����ļ�
�� ������ settings.py # ϵͳ����
������ tests/ # ����Ŀ¼
�� ������ test_api/ # API����
�� ������ test_services/ # �������
������ .gitignore # Git�����ļ�
������ requirements.txt # ��Ŀ����
������ README.md # ��Ŀ˵��
������ app.py # Ӧ�����


## ? �����ص�
- ? ����������ѧ��
- ? �Զ�����֤
- ? �û����ȸ���
- ? �Ѷ�����Ӧ
- ? ��ʷ��¼ͳ��

## ? ����ջ
- ��˿�ܣ�Python Flask
- ���ݿ⣺PostgreSQL
- ORM��SQLAlchemy
- ��֤��JWT
- �ĵ���Swagger/OpenAPI

## ? ����Ҫ��
- Python 3.8+
- PostgreSQL 12+
- ������Ҫ��� requirements.txt

## ? ��װ����
1. **��¡��Ŀ**
   ```bash
   git clone https://github.com/����û���/ai_math_tutor.git
   cd ai_math_tutor
   ```

2. **�������⻷��**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **��װ����**
   ```bash
   pip install -r requirements.txt
   ```

4. **�������ݿ�**
   ```sql
   CREATE DATABASE ai_math_tutor;
   ```

5. **������Ŀ**
   ```bash
   python app.py
   ```

## ? API �ĵ�

### �û��ӿ�
| ���� | ·�� | ���� |
|------|------|------|
| POST | `/api/v1/auth/register` | �û�ע�� |
| POST | `/api/v1/auth/login` | �û���¼ |
| GET | `/api/v1/auth/profile` | ��ȡ�û���Ϣ |

### ��ѧ��ӿ�
| ���� | ·�� | ���� |
|------|------|------|
| POST | `/api/v1/problems/generate` | ������Ŀ |
| POST | `/api/v1/problems/verify` | ��֤�� |
| GET | `/api/v1/problems/history` | ��ȡ��ʷ��¼ |

## ? �Ŷӷֹ�

### ��˿��� (A, B, C)
- �û�ϵͳ
- ��ѧ������
- ����֤

### ǰ�˿��� (D, E)
- ҳ�����
- ����ʵ��

### �����ĵ� (F, G)
- ���ܲ���
- �ĵ���д

## ? ��Ŀ����
- [x] ��Ŀ��ʼ��
- [x] ���ݿ�����
- [ ] �û�ϵͳ
- [ ] ��ѧ��ģ��
- [ ] ǰ�˽���
- [ ] ��������

## ? ��ϵ��ʽ
- **��Ŀ�����ˣ�** xxx
- **���䣺** xxx@xxx.com
- **΢��Ⱥ��** xxx

## ? ���֤
MIT License

## ? ����ָ��
1. Fork ��Ŀ
2. �������ܷ�֧
3. �ύ����
4. ���� Pull Request

## ? ������־
### v0.1.0 (2024-02-17)
- ��Ŀ��ʼ��
- ������ܴ
- ���ݿ��������