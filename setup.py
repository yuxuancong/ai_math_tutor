from setuptools import setup, find_packages

setup(
    name="ai-math-tutor",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai",
        "numpy",
        "sympy",  # 数学符号计算
        "matplotlib",  # 数学可视化
        "streamlit",  # Web界面
        "pandas",
        "scipy"
    ],
    author="Your Name",
    description="AI-powered mathematics tutoring system",
)
