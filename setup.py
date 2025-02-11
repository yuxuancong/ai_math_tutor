from setuptools import setup, find_packages

setup(
    name="ai-math-tutor",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai",
        "numpy",
        "sympy",  # ��ѧ���ż���
        "matplotlib",  # ��ѧ���ӻ�
        "streamlit",  # Web����
        "pandas",
        "scipy"
    ],
    author="Your Name",
    description="AI-powered mathematics tutoring system",
)
